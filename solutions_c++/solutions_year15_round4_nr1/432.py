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
		freopen( "A-large.in", "r", stdin );
		freopen( "A-large.out", "w", stdout );
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
        ll r, c;
        cin >> r >> c;
        string s[111];
        forn( i, r ) {
            cin >> s[i];
        }
        ll ans = 0;
        bool res = false;
        forn( i, r ) {
            forn( j, c ) {
                if( s[i][j] == '.' )
                    continue;
                vector< char > a;
                ll ii, jj;
                ii = i + 1, jj = j;
                while( ii < r && s[ii][jj] == '.' ) {
                    ii ++;
                }
                if( ii != r )
                    a.pb( 'v' );
                ii = i - 1, jj = j;
                while( ii >= 0 && s[ii][jj] == '.' ) {
                    ii --;
                }
                if( ii != -1 )
                    a.pb( '^' );
                ii = i, jj = j + 1;
                while( jj < c && s[ii][jj] == '.' ) {
                    jj ++;
                }
                if( jj != c )
                    a.pb( '>' );
                ii = i, jj = j - 1;
                while( jj >= 0 && s[ii][jj] == '.' ) {
                    jj --;
                }
                if( jj != -1 )
                    a.pb( '<' );
                if( a.size() == 0 ) {
                    res = true;
                    break;
                }
                bool b = true;
                forn( k, a.size() ) {
                    if( a[k] == s[i][j] )
                        b = false;
                }
                ans += b;
            }
            if( res )
                break;
        }
        if( res ) {
            cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << t + 1 << ": " << ans << endl;
        }
    }
	return 0;
}

