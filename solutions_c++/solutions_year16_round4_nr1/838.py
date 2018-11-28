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

map< pair< pair< ll, ll >, pair< ll, ll > >, string > m[13];

pair< pair< ll, ll >, pair< ll, ll > > f( ll win, ll r, ll p, ll s ) {
	return mp( mp( win, r ), mp( p, s ) );
}

ll winner( ll x, ll y ) {
	if( x > y )
		return winner( y, x );
	if( x == 0 && y == 1 )
		return 1;
	if( x == 0 && y == 2 )
		return 0;
	if( x == 1 && y == 2 )
		return 2;
}

int main( void ) {
	m[0][f( 0, 1, 0, 0 )] = "R";
	m[0][f( 1, 0, 1, 0 )] = "P";
	m[0][f( 2, 0, 0, 1 )] = "S";
	for( ll i = 1; i <= 12; i ++ ) {
		for( map< pair< pair< ll, ll >, pair< ll, ll > >, string >::iterator j = m[i - 1].begin(); j != m[i - 1].end(); j ++ ) {
			for( map< pair< pair< ll, ll >, pair< ll, ll > >, string >::iterator k = m[i - 1].begin(); k != m[i - 1].end(); k ++ ) {
				if( j->X.X.X == k->X.X.X )
					continue;
				ll win = winner( j->X.X.X, k->X.X.X );
				ll r = j->X.X.Y + k->X.X.Y;
				ll p = j->X.Y.X + k->X.Y.X;
				ll s = j->X.Y.Y + k->X.Y.Y;
				string res = ( j->Y + k->Y );
				if( m[i].find( f( win, r, p, s ) ) != m[i].end() )
					m[i][f( win, r, p, s )] = min( m[i][f( win, r, p, s )], res );
				else
					m[i][f( win, r, p, s )] = res;
			}
		}
	}
	ll T;
	cin >> T;
	forn( _, T ) {
		ll n, r, p, s;
		cin >> n >> r >> p >> s;
		cout << "Case #" << _ + 1 << ": ";
		bool ok = false;
		forn( i, 3 ) {
			if( m[n].find( f( i, r, p, s ) ) != m[n].end() ) {
				cout << m[n][f( i, r, p, s )] << endl;
				ok = true;
				break;
			}
		}
		if( !ok ) {
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
