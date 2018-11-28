#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<cstdlib>
#include<algorithm>
#include<ctime>
using namespace std;

#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define FORD(i,h,l) for(int i=(h);i>=(l);--i)

const int max_prime=1000;

set<unsigned> S;

bool b[max_prime+10];
int prime[max_prime];
int Nprime;

void get_prime()
{
	FOR(i,2,max_prime)
	{
		if (!b[i])
		{
			prime[++Nprime]=i;
			for(int j=i+i;j<=max_prime;j+=i)
				b[j]=true;
		}
	}
}

unsigned sample(int n)
{
	int n1=(n-2)/2;
	int n2=(n-2)-n1;
	unsigned num_part1=rand()%(1<<n1);
	unsigned num_part2=rand()%(1<<n2);
	return (1<<(n-1))+(num_part1<<n2)+(num_part2<<1)+1;
}

bool check(unsigned num,int base,int factor)
{
	int ans=0;
	int base_temp=1;
	while (num)
	{
		if (num&1)
			ans=(ans+base_temp)%factor;
		base_temp=(base_temp*base)%factor;
		num>>=1;
	}
	if (ans) return false; else return true;
}

int out[100];

void print(unsigned num)
{
	int len=0;
	while (num)
	{
		out[++len]=num&1;
		num>>=1;
	}
	FORD(i,len,1)
		printf("%d",out[i]);
	printf(" ");
}

bool check(unsigned num,bool flag_print=false)
{
	if (flag_print) print(num);
	FOR(i,2,10)
	{
		bool is_prime=true;
		FOR(j,1,Nprime)
		{
			if (check(num,i,prime[j]))
			{
				is_prime=false;
				if (flag_print) printf("%d%c",prime[j]," \n"[i==10?1:0]);
				break;
			}
		}
		if (is_prime) return false;
	}
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	srand((unsigned)time(NULL));
	
	get_prime();
	
	int T;
	scanf("%d",&T);
	FOR(Tcase,1,T)
	{
		printf("Case #%d:\n",Tcase);
		int n,m;
		scanf("%d%d",&n,&m);
		while (m)
		{
			unsigned num=sample(n);
			if (S.count(num)==0 && check(num))
			{
				check(num,true);
				S.insert(num);
				m--;
			}
		}
	}
	return 0;
}

