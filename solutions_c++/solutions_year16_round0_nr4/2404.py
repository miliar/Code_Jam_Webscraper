#include <bits/stdc++.h>

using namespace std;
#define ll long long


ll power(ll a,ll b)
{
	ll ret=1;
	while(b)
	{
		if(b%2)
		 ret = ret * a;
		a= a*a;
		b = b/2;
	}
	return ret;
}
int main()
{
	long long n,t,J;
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
	
	scanf("%lld",&t);
	int tst=0;
	
	while(t--)
	{
		tst++;
		ll k,s,c;
		
		scanf("%lld %lld %lld",&k,&c,&s);
		
		printf("Case #%d: ",tst);
		ll sum=1;
		for(int i=1;i<=s;i++)
		{
		   printf("%lld ",sum);
		   sum += power(k,c-1);	
		}
		printf("\n");	
	}
	
	return 0;
}

