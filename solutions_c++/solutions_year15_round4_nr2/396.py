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
        ll n;
        dd v, x;
        cin >> n >> v >> x;
        dd r[111], c[111];
        forn( i, n ) {
            cin >> r[i] >> c[i];
        }
        cout << "Case #" << t + 1 << ": ";
        if( n == 1 ) {
            if( c[0] != x )
                cout << "IMPOSSIBLE" << endl;
            else
                cout << fixed << setprecision( 10 ) << v / r[0] << endl;
        } else {
            if( ( c[0] > x && c[1] > x ) || ( c[0] < x && c[1] < x ) ) {
                cout << "IMPOSSIBLE" << endl;
                continue;
            }
            if( c[0] == x && c[1] == x ) {
                cout << fixed << setprecision( 10 ) << v / ( r[0] + r[1] ) << endl;
                continue;
            }
            dd lll = 0.0;
            dd rrr = v;
            if( c[0] > c[1] ) {
                swap( c[0], c[1] );
                swap( r[0], r[1] );
            }
            forn( _, 555 ) {
                dd s = ( lll + rrr ) / 2.0;
                dd s2 = v - s;
                dd tt = ( s * c[0] + s2 * c[1] ) / v;
                if( tt > x )
                    lll = s;
                else
                    rrr = s;
            }
            dd s = lll;
            dd s2 = v - s;
            cout << fixed << setprecision( 10 ) << max( s / r[0], s2 / r[1] ) << endl;
        }
    }
	return 0;
}

