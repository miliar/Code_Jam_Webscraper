#include<stdio.h>
#include<string.h>
#include<iostream>
#include<math.h>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long lld;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
bool isprime[100010];
lld prime[100010];
int total;
void init()
{
	total=0;
	memset(isprime,true,sizeof(isprime));
	for(int i=2;i<100010;i++)
		if(isprime[i])
		{
			prime[total++]=i;
			for(int j=i+i;j<100010;j+=i)
				isprime[j]=false;
		}
}
lld pp[110];
lld qq;
bool solve(lld s,lld base)
{
//	cout << s << " " << base << endl;
	lld val=0;
	lld add=1;
	while(s)
	{
		if(s%2)
			val+=add;
		add*=base;
		s/=2;
	}
//	cout << val << endl;
	for(int i=0;prime[i]*prime[i] <= val && i < total;i++)
		if(val%prime[i] == 0)
		{
			pp[qq++]=prime[i];
			return true;
		}
	return false;
}
int ff[110];
int gg;
void out(lld s)
{
	gg=0;
	while(s)
	{
		ff[gg++]=s%2;
		s/=2;
	}
	for(int i=gg-1;i>=0;i--)
		printf("%d",ff[i]);
	for(int i=2;i<=10;i++)
		printf(" %I64d",pp[i]);
	printf("\n");
}
int main()
{
//	freopen("B-large.in","r",stdin);
	freopen("C_small.out","w",stdout);
	init();
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		printf("Case #%d:\n",cc);
		int n,need;
		scanf("%d %d",&n,&need);
		n--;
		lld start=(1LL)<<n;
		for(lld i=start+1;need;i+=2)
		{
			qq=2;
			bool flag=true;
			for(int j=2;j<=10;j++)
				if(!solve(i,j))
					flag=false;
			if(flag)
			{
				need--;
				out(i);
			}
		}
	}
    return 0;
}
/*
1
6 3

 */
