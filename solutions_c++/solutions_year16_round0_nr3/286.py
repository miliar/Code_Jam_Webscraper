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
		freopen( "C-large.in", "r", stdin ); freopen( "C-large.out", "w", stdout );
		if( OJ ) { ios_base::Init i; cin.sync_with_stdio( 0 ); cin.tie( 0 ); }
	} ~__s() {
		if( !OJ ) TIMESTAMP;
		ll n; cin >> n;
	}
} __S;

ll mod[11] = { 0, 0, 3, 2, 3, 2, 7, 2, 3, 2, 3 };

ll isPrime( ll x ) {
	for( ll i = 2; i * i <= x; i ++ ) {
		if( x % i == 0 )
			return i;
	}
	return 0;
}

string bin( ll x ) {
	string res;
	while( x ) {
		char c = x % 2 + '0';
		res += c;
		x /= 2;
	}
	reverse( res.begin(), res.end() );
	return res;
}

ll dec( string x, ll y, ll mod ) {
	ll res = 0;
	forn( i, x.size() ) {
		res *= y;
		res += x[i] - '0';
		res %= mod;
	}
	return res;
}

bool check( ll x ) {
	string y = bin( x );
	for( ll i = 2; i <= 10; i ++ ) {
		if( i == 6 )
			continue;
		ll z = dec( y, i, mod[i] );
		if( z )
			return false;
	}
	return true;
}

int main( void ) {
	ll n = 32;
	ll m = 500;
	ll l = ( 1LL << ( n - 1 ) ) + 1;
	ll r = ( 1LL << n ) - 1;
	vector< ll > v;
	for( ll i = l; i <= r; i += 2 ) {
		if( check( i ) ) {
			v.pb( i );
			if( v.size() == m )
				break;
		}
	}
	cout << "Case #1:" << endl;
	forn( i, v.size() ) {
		cout << bin( v[i] ) << " ";
		for( ll i = 2; i <= 10; i ++ ) {
			cout << mod[i] << " ";
		}
		cout << endl;
	}
	return 0;
}
