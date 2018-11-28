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
		freopen( "D-small-attempt0.in", "r", stdin );
		freopen( "D-small-attempt0.out", "w", stdout );
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
        ll x, r, c;
        cin >> x >> r >> c;
        if( r > c )
            swap( r, c );
        bool ans;
        if( r * c % x )
            ans = false;
        else if( x > r && x > c )
            ans = false;
        else if( x > 2 && ( x - 1 > c || 2 > r ) )
            ans = false;
        else if( x == 4 && r == 2 && c == 4 )
            ans = false;
        else
            ans = true;
        cout << "Case #" << t + 1 << ": " << ( ans ? "GABRIEL" : "RICHARD" ) << endl;
    }
	return 0;
}

