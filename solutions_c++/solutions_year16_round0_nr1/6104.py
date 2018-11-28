#include<bits/stdc++.h>

using namespace std;

typedef long long int ll;

int main()
{
	ll nt;
	scanf(" %lld",&nt);
	for(ll t=1; t<=nt; t++)
	{
		ll n0,n;
		set<ll> s;
		printf("Case #%lld: ",t);
		scanf(" %lld",&n0);
		n = n0;
		if(n0) while(s.size()<10)
		{
			ll c = n;
			while(c) { s.insert(c%10); c/=10; }
			n+=n0;
		}
		else { printf("INSOMNIA\n"); continue; }
		printf("%lld\n",n-n0);
	}
	return 0;
}
