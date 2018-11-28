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


int main( void ) {
	ll T;
	cin >> T;
	forn( t, T ) {
		string s;
		ll k;
		cin >> s >> k;
		ll cnt = 0;
		forn( i, s.size() - k + 1 ) {
			if( s[i] == '+' )
				continue;
			forn( j, k ) {
				s[i + j] = ( s[i + j] == '+' ? '-' : '+' );
			}
			cnt ++;
		}
		bool ok = true;
		forn( i, s.size() ) {
			if( s[i] == '-' )
				ok = false;
		}
		if( ok )
			cout << "Case #" << t + 1 << ": " << cnt << endl;
		else
			cout << "Case #" << t + 1 << ": " << "IMPOSSIBLE" << endl;
	}
	return 0;
}
