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
		freopen( "D-small-attempt0.in", "r", stdin ); freopen( "D-small_attempt0.out", "w", stdout );
		if( OJ ) { ios_base::Init i; cin.sync_with_stdio( 0 ); cin.tie( 0 ); }
	} ~__s() {
		if( !OJ ) TIMESTAMP;
		ll n; cin >> n;
	}
} __S;

ll cnt( ll x ) {
	ll res = 0;
	while( x ) {
		res += x % 2;
		x /= 2;
	}
	return res;
}

void add( vector< vector< bool > > &b, ll n, ll x, bool val ) {
	forn( i, n ) {
		forn( j, n ) {
			if( x & ( 1LL << ( i * n + j ) ) )
				b[n - 1 - i][n - 1 - j] = val;
		}
	}
}

bool check( vector< vector< bool > > &b, ll n ) {
	vector< vector< ll > > a( n );
	forn( j, n ) {
		forn( i, n ) {
			if( b[i][j] )
				a[j].pb( i );
		}
	}
	forn( i, n ) {
		bool ok = false;
		ll res = 0;
		set< ll > s;
		forn( j, n ) {
			res += b[i][j];
			if( b[i][j] && a[j].size() == 1 )
				ok = true;
			if( b[i][j] ) {
				forn( k, a[j].size() ) {
					s.insert( a[j][k] );
				}
			}
		}
		if( !ok && res != s.size() || res == 0 )
			return false;
	}
	return true;
}

int main( void ) {
	ll T;
	cin >> T;
	forn( _, T ) {
		ll n;
		cin >> n;
		vector< vector< bool > > b( n, vector< bool >( n, false ) );
		ll sum = 0;
		forn( i, n ) {
			string s;
			cin >> s;
			forn( j, s.size() ) {
				b[i][j] = ( s[j] == '1' );
				sum *= 2;
				sum += ( s[j] == '1' );
			}
		}
		ll ans = 1e9;
		forn( i, ( 1LL << ( n * n ) ) ) {
			if( ( i + sum ) != ( i ^ sum ) )
				continue;
			add( b, n, i, true );
			if( check( b, n ) )
				ans = min( ans, cnt( i ) );
			add( b, n, i, false );
		}
		cout << "Case #" << _ + 1 << ": " << ans << endl;
	}
	return 0;
}
