// Shalin
#include <bits/stdc++.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>
using namespace std;
#define si(x) scanf("%d",&x)
#define slli(x) scanf("%lld",&x);
#define sc(x) scanf("%c",&x);
#define ss(x) scanf("%s",x);
#define sd(x) scanf("%lf",&x);
#define bitcount __builtin_popcount
#define gcd __gcd
#define llu long long unsigned int
#define lli long long int
#define fi first
#define se second
#define pb push_back
#define mod 1000000007
#define mp make_pair
#define vi vector<int>
#define vlli vector<long long int>
#define pii pair<int,int>
#define nn 100000000
bool isprime[100000010];vlli primes;
lli fp(lli a,lli n,lli m)
{
    if(n==0) return 1;
    if(n==1) return a;
    
    lli half=fp(a,n/2,m);
    if(n%2==0)
        return (half*half)%m;
    else return (a*((half*half)%m))%m;
}

void sieve()
{
	lli i,j,k,root=10000;
	isprime[1]=0;
	for(i=2;i<=root;i++)
	{
		if(isprime[i])
		{
			for(j=2*i;j<=nn;j+=i)
			{
				isprime[j]=0;
			}
		}
	}
	for(i=2;i<=nn;i++)
	{
		if(isprime[i])
			primes.pb(i);
	}
}
int main()
{
	//freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    memset(isprime,1,sizeof(isprime));
	sieve();					
	lli len=primes.size();
	lli i,j,k;
	lli cnt=0;
	lli end=(1<<15)*(1<<15);
	printf("Case #1:\n");
	//cout<<"len : "<<len<<endl;
	//cout<<"end : "<<end<<endl;
	//return 0;
	for(i=0;i<end;i++)
	{
	//	cout<<"i : "<<i<<endl;
		lli temp=i;
		bool bits[32];
		bits[0]=1;
		for(j=31;j>0;j--)
		{
			bits[j]=temp%2;
			temp/=2;
		}
		bool ok=1;
		if(bits[0]==1 and bits[31]==1)
		{
			//cout<<"i : "<<i<<endl;
			vlli ans;
			for(lli base=2;base<=10;base++)
			{
				lli lenn=primes.size();
				lli divisor=-1;
				for(lli ii=0;ii<len;ii++)
				{
					lli m=primes[ii];
					lli num=0,power=0;
					for(lli jj=31;jj>=0;jj--)
					{
						if(bits[jj])
						{
							num=(num+fp(base,power,m))%m;
						}
						power++;
					}
					if(num==0)
					{
						divisor=m;
						break;
					}
				}
				//lli divisor=check(bits,base);
				//cout<<"divisor : "<<divisor<<endl;
				if(divisor==-1)
				{
					ok=0;
					break;
				}
				ans.pb(divisor);
			}
			if(ok)
			{
				for(j=0;j<=31;j++)
					printf("%d",bits[j]);
				printf(" ");
				for(j=0;j<9;j++)
					printf("%lld ",ans[j]);
				printf("\n");
				cnt++;
			}
			if(cnt==500)
				break;
		}
	}
	//cout<<"cnt : "<<cnt<<endl;
	return 0;
}