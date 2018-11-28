#include <bits/stdc++.h>

using namespace std;

#ifdef ONLINE_JUDGE
#define OJ 1
#else
#define OJ 0
#endif

#define dd				double
#define ll 				long long
#define pb 				push_back
#define mp 				make_pair
#define X				first
#define Y				second
#define forn( i, n ) 	for( ll i = 0; i < (ll) (n); i ++ )
#define endl 			'\n'

#define TIMESTAMP fprintf(stderr, "Execution time: %.3lf s.\n", (double)clock()/CLOCKS_PER_SEC)

struct __s { __s() {
		//srand( time( NULL ) );
		freopen( "B-small-attempt0.in", "r", stdin );
		freopen( "B-small-attempt0.out", "w", stdout );
		if( OJ ) { ios_base::Init i; cin.sync_with_stdio( 0 ); cin.tie( 0 ); }
	} ~__s() {
		if( !OJ ) TIMESTAMP;
		ll n; cin >> n;
	}
} __S;

int main( void ) {
    ll T;
    cin >> T;
    forn( t, T ) {
        ll r, c, n;
        cin >> r >> c >> n;
        ll ans = 200;
        forn( i, 1 << ( r * c ) ) {
            ll m = 0;
            forn( j, r * c ) {
                if( i & ( 1 << j ) )
                    m ++;
            }
            if( n != m )
                continue;
            bool a[r][c];
            forn( j, r * c ) {
                a[j / c][j % c] = ( i & ( 1 << j ) );
            }
            ll res = 0;
            forn( j, r ) {
                forn( k, c - 1 ) {
                    if( a[j][k] && a[j][k + 1] )
                        res ++;
                }
            }
            forn( j, r - 1 ) {
                forn( k, c ) {
                    if( a[j][k] && a[j + 1][k] )
                        res ++;
                }
            }
            ans = min( ans, res );
        }
        cout << "Case #" << t + 1 << ": " << ans << endl;
    }
	return 0;
}
