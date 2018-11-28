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
	int t,i,j,k;si(t);
	for(i=1;i<=t;i++)
	{
		string str;
		cin>>str;
		int ans=0;
		int len=str.size();
		int cntpre=0;
		for(j=0;j<len;j++)
		{
			if(str[j]=='-')
				cntpre++;
			else
				break;
		}
		int start=j;
		if(cntpre!=0)
			ans++;
		int cnt=0;
		for(j=start;j<len;j++)
		{
			if(str[j]=='-' and str[j-1]=='+')
				cnt++;
		}
		ans=ans+cnt*2;
		printf("Case #%d: %d\n",i,ans);
	}					
	return 0;
}