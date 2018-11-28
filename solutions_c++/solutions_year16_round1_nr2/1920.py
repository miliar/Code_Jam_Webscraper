#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define vi vector<ll>
#define vvi vector<vi>
#define pb push_back
#define forn(i,n) for( i = 0; i < n; i++ )
#define s(n) scanf("%lld",&n);
int main()
{
	ll i, ii, t, n;
	s(t);
	for( ii = 1 ; ii <= t; ii++ )
	{
		s(n);
		
		vi hash(2505,0); vi ans(60, 0);
		ll j, k, inp, cnt = 0;
		
		for( j = 0; j < 2*n-1; j++ ) {
			for( k = 0 ; k < n; k++ ){
				s(inp);
				hash[inp] = hash[inp] + 1;
			}
		}
		for( j = 0; j < 2505; j++ ) {
			if( hash[j] & 1 ) {
				ans[cnt] = j;
				cnt = cnt + 1;
			}
		}
        printf("Case #%lld: ", ii);
		for( i = 0 ; i < n ; i++ ) printf("%lld ",ans[i]);
		printf("\n");
	}
    return 0;
}