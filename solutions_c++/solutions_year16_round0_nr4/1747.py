#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll fpow(ll x, ll y)
{
	if (y == 0)
		return 1;
	if (y&1)
		return x*fpow(x, y-1);
	ll tmp = fpow(x, y/2);
	return tmp*tmp;
}

int main()
{
	int T, casecnt = 0;
	scanf("%d", &T);
	
	while(T--)
	{
		ll k, c, s;
		scanf("%lld %lld %lld", &k, &c, &s);
		ll nsz = fpow(k, c-1);
		printf("Case #%d:", ++casecnt); 
		for (ll i = 0; i < s; i++)
			printf(" %lld", (nsz*i)+1);
		printf("\n");
	}
	return 0;	
}
