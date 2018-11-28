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
		freopen( "A-large.in", "r", stdin ); freopen( "A-large.out", "w", stdout );
		if( OJ ) { ios_base::Init i; cin.sync_with_stdio( 0 ); cin.tie( 0 ); }
	} ~__s() {
		if( !OJ ) TIMESTAMP;
		ll n; cin >> n;
	}
} __S;

bool check( vector< ll > p ) {
	ll sum = 0;
	ll m = 0;
	forn( i, p.size() ) {
		sum += p[i];
		m = max( m, p[i] );
	}
	return ( sum - m ) < m;
}

int main( void ) {
	ll T;
	cin >> T;
	forn( t, T ) {
		ll n;
		cin >> n;
		vector< ll > p( n );
		ll sum = 0;
		forn( i, n ) {
			cin >> p[i];
			sum += p[i];
		}
		cout << "Case #" << t + 1 << ": ";
		if( n == 2 ) {
			forn( i, p[0] ) {
				cout << "AB ";
			}
			cout << endl;
			continue;
		}
		while( sum != 2 ) {
			ll idx = 0;
			forn( i, n ) {
				if( p[i] > p[idx] ) {
					idx = i;
				}
			}
			p[idx] --;
			sum --;
			char c = ( idx + 'A' );
			cout << c << " ";
		}
		ll i = 0;
		while( p[i] == 0 )
			i ++;
		ll j = i + 1;
		while( p[j] == 0 )
			j ++;
		char a = ( i + 'A' );
		char b = ( j + 'A' );
		cout << a << b << endl;
	}
	return 0;
}
