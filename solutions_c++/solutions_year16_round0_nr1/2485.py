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
int main()
{
	//freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
	lli t,i,j,k;slli(t);
	for(j=1;j<=t;j++)
	{
		lli n;slli(n);
		bool done[11];
		memset(done,0,sizeof(done));
		bool ok=0;
		for(i=1;i<=1000000;i++)
		{
			lli temp=n*i;
			while(temp!=0)
			{
				done[temp%10]=1;
				temp/=10;
			}
			bool flag=1;
			for(k=0;k<=9;k++)
			{
				if(done[k]==0)
				{
					flag=0;
					break;
				}
			}
			if(flag==1)
			{
				printf("Case #%lld: %lld\n",j,n*i);
				ok=1;
				break;
			}
		}
		if(ok==0)
			printf("Case #%lld: INSOMNIA\n",j);
	}	
	return 0;			
}