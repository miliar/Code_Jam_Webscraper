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
		freopen( "C-small-attempt0.in", "r", stdin ); freopen( "C-small-attempt0.out", "w", stdout );
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
		ll j, p, s, k;
		cin >> j >> p >> s >> k;
		ll n = j * p * s;
		vector< pair< ll, pair< ll, ll > > > v;
		forn( i, ( 1 << n ) ) {
			map< pair< ll, ll >, ll > jp, js, ps;
			bool ok = true;
			vector< pair< ll, pair< ll, ll > > > w;
			forn( m, n ) {
				if( i & ( 1 << m ) ) {
					ll jj = m % j;
					ll pp = ( m / j ) % p;
					ll ss = ( m / j / p ) % s;
					w.pb( mp( jj, mp( pp, ss ) ) );
					jp[mp( jj, pp )] ++;
					js[mp( jj, ss )] ++;
					ps[mp( pp, ss )] ++;
					if( jp[mp( jj, pp )] > k || js[mp( jj, ss )] > k || ps[mp( pp, ss )] > k ) {
						ok = false;
						break;
					}
				}
			}
			if( ok ) {
				if( w.size() > v.size() ) {
					v = w;
				}
			}
		}
		cout << "Case #" << t + 1 << ": " << v.size() << endl;
		forn( i, v.size() ) {
			cout << v[i].X + 1 << " " << v[i].Y.X + 1 << " " << v[i].Y.Y + 1 << endl;
		}
	}
	return 0;
}
