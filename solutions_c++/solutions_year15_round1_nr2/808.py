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
		freopen( "B-large.in", "r", stdin );
		freopen( "B-large.out", "w", stdout );
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
        ll b, n;
        cin >> b >> n;
        vector< ll > m( b );
        ll a = 100000LL;
        forn( i, b ) {
            cin >> m[i];
            a = min( a, m[i] );
        }
        ll l = 0LL;
        ll r = a * n;
        while( r != l ) {
            ll s = ( r + l ) / 2;
            ll res = 0;
            forn( i, b ) {
                res += s / m[i] + 1;
            }
            if( res >= n - 1 )
                r = s;
            else
                l = s + 1;
        }
        ll res = 0;
        set< pair< ll, ll > > s;
        forn( i, b ) {
            ll n = l / m[i];
            res += n;
            s.insert( mp( n * m[i], i ) );
        }
        while( res != n - 1 ) {
            ll t = s.begin()->X, i = s.begin()->Y;
            s.erase( s.begin() );
            s.insert( mp( t + m[i], i ) );
            res ++;
        }
        cout << "Case #" << t + 1 << ": " << s.begin()->Y + 1 << endl;
    }
	return 0;
}

