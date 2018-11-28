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
		freopen( "B-small-attempt1.in", "r", stdin ); freopen( "B-small_attempt1.out", "w", stdout );
		if( OJ ) { ios_base::Init i; cin.sync_with_stdio( 0 ); cin.tie( 0 ); }
	} ~__s() {
		if( !OJ ) TIMESTAMP;
		ll n; cin >> n;
	}
} __S;

bool check( ll x, ll k ) {
	ll res = 0;
	while( x ) {
		res += x % 2;
		x /= 2;
	}
	return res == k;
}

int main( void ) {
	ll T;
	cin >> T;
	forn( _, T ) {
		ll n, k;
		cin >> n >> k;
		vector< dd > a( n );
		forn( i, n ) {
			cin >> a[i];
		}
		dd ans = 0.0;
		forn( i, ( 1LL << n ) ) {
			if( !check( i, k ) )
				continue;
			vector< dd > p;
			forn( j, n ) {
				if( i & ( 1LL << j ) ) {
					p.pb( a[j] );
				}
			}
			dd sum = 0.0;
			forn( j, ( 1LL << k ) ) {
				if( !check( j, k / 2 ) )
					continue;
				dd res = 1.0;
				forn( l, k ) {
					if( j & ( 1LL << l ) )
						res *= p[l];
					else
						res *= ( 1 - p[l] );
				}
				sum += res;
			}
			ans = max( ans, sum );
		}
		cout << "Case #" << _ + 1 << ": ";
		cout << fixed << setprecision( 10 ) << ans << endl;
	}
	return 0;
}
