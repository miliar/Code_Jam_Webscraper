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
		freopen( "B-large.in", "r", stdin ); freopen( "B-large.out", "w", stdout );
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
		ll n, m;
		cin >> n >> m;
		if( ( 1LL << ( n - 2 ) ) < m ) {
			cout << "Case #" << t + 1 << ": " << "IMPOSSIBLE" << endl;
			continue;
		}
		vector< vector< bool > > b( n, vector< bool >( n, false ) );
		for( ll i = 1; i < n; i ++ ) {
			b[0][i] = true;
		}
		m --;
		vector< ll > a( n );
		a[n - 1] = 1;
		for( ll i = n - 2; i > 0; i -- ) {
			for( ll j = i + 1; j < n; j ++ ) {
				if( m >= a[j] ) {
					m -= a[j];
					a[i] += a[j];
					b[i][j] = true;
				}
			}
		}
		cout << "Case #" << t + 1 << ": " << "POSSIBLE" << endl;
		forn( i, n ) {
			forn( j, n ) {
				cout << b[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}
