#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
	ll t,k,c,s,j;
	scanf("%lld",&t);
	j = t;
	while(t--)
	{
		scanf("%lld%lld%lld",&k,&c,&s);
		ll p = 1;
		for(ll l = 1 ; l <= c - 1 ; l++ )
		{
			p *= k;
		}
		ll i = 1;
		printf("Case #%lld: ", j - t);
		for(ll l = 1 ; l <= s ; l++ )
		{
			printf("%lld ", i);
			i += p;
		}
		printf("\n");
	}
	return 0;
}
