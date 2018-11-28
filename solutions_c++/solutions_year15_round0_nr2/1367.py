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
        ll n;
        cin >> n;
        vector< ll > a( n );
        vector< ll > b( n );
        set< pair< ll, ll > > s;
        forn( i, n ) {
            ll x;
            cin >> x;
            a[i] = x;
            b[i] = 1;
            s.insert( mp( -x, i ) );
        }
        ll ans = - s.begin()->X;
        for( ll i = 1; i <= 1000; i ++ ) {
            ll j = s.begin()->Y;
            s.erase( s.begin() );
            b[j] ++;
            ll c = a[j] / b[j] + !!( a[j] % b[j] );
            s.insert( mp( -c, j ) );
            ans = min( ans, - s.begin()->X + i );
        }
        cout << "Case #" << t + 1 << ": " << ans << endl;
    }
	return 0;
}

