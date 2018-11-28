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
		srand( time( NULL ) );
		freopen( "D-large.in", "r", stdin ); freopen( "D-large.out", "w", stdout );
		if( OJ ) { ios_base::Init i; cin.sync_with_stdio( 0 ); cin.tie( 0 ); }
	} ~__s() {
		if( !OJ ) TIMESTAMP;
		ll n; cin >> n;
	}
} __S;

ll k, c, s;

ll rec( ll x, ll y, ll n ) {
	if( n == c ) {
		return x;
	}
	y = min( y + 1, k );
	x = ( x - 1 ) * k + y;
	return rec( x, y, n + 1 );
}

int main( void ) {
	ll T;
	cin >> T;
	forn( t, T ) {
		cin >> k >> c >> s;
		if( k > c * s ) {
			cout << "Case #" << t + 1 << ": " << "IMPOSSIBLE" << endl;
			continue;
		}
		vector< ll > v;
		for( ll i = 1; i <= k; i += c ) {
			v.pb( rec( i, i, 1 ) );
		}
		cout << "Case #" << t + 1 << ": ";
		forn( i, v.size() ) {
			cout << v[i] << " ";
		}
		cout << endl;
	}
	return 0;
}
