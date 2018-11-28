#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define vi vector<ll>
#define vvi vector<vi>
#define pb push_back
#define forn(i,n) for( i = 0; i < n; i++ )
#define s(n) scanf("%lld",&n);

ll fpow(ll a, ll b)
{
    if(b == 0) return 1;
    ll c =fpow(a, b / 2);
    if(b % 2 == 0) return (c * c);
    else return ((c * c) * a);
}
int main()
{
	ll i, ii, t, n, k, c , cnt, ans;
	s(t);
	for( ii = 1 ; ii <= t; ii++ )
	{
		ans = 1;
        s(k);s(c);s(cnt);
		ll add = fpow(k,c-1);
		printf("Case #%lld: ", ii);
		for( i = 0; i < k; i++ ){
			printf("%lld ", ans);
			ans += add;
		}
		printf("\n");
	}
    return 0;
}