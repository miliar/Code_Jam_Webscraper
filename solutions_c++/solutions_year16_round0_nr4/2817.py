#include<bits/stdc++.h>
#define ll long long int
#define pb push_back
#define MOD 1000000007
using namespace std;

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("out3.out","w",stdout);
	ll t,k,c,s,x;
	scanf("%lld",&t);
	for(ll x=1;x<=t;++x)
	{
		scanf("%lld%lld%lld",&k,&c,&s);
		printf("Case #%lld: ",x);
		for(ll i=1;i<=s;++i)
		printf("%lld ",i);
		printf("\n");
	}
	return 0;
}
