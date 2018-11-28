#include <bits/stdc++.h>
#define D(x) cout << ">> " << #x << " = >" << x << "<" << endl
#define FOR(i,a,b) for ( int i = int(a); i < int(b); ++i )
using namespace std;
typedef long long ll;

const int LIM = 5*1e7;
const int N = 16;
const int J = 50;

int prime[LIM];
vector<int>  primes;

int cnt;
char num[N+1] = "1";

bool isPrime( ll n ) {
	for ( ll pf = 2; pf * pf <= n; ++pf )
		if ( n % pf == 0 )
			return false;
	return true;
}

ll divisor( ll n ) {
	for ( ll pf = 2; pf * pf <= n; ++pf )
		if ( n % pf == 0 )
			return pf;
	return 0;
}

bool check( const string & num, int base, ll divisor ) {
	ll x = 0;
	for ( char c : num )
		x = x * base + c - '0';
	if ( x % divisor )
		return false;
	return true;
}

void solve( int n, vector<ll> b ) {
	if ( n == N ) {
		if ( all_of( b.begin( ) + 2, b.begin( ) + 11, [&] ( ll x ) {
			/*return !all_of( primes.begin( ), primes.end( ), [&] ( int p ) {
				return x == p || (x % p != 0);
			} );*/
			return !isPrime( x );
		} ) ) {
			cout << num;
			FOR( i, 2, 11 ) {
				assert( check( num, i, divisor( b[i] ) ) );
				cout << " " << divisor( b[i] );
				//cout << " (" << b[i] << ")" << prime[ b[i] ];
			}
			cout << endl;
			if ( ++cnt == J )
				throw "done";
		}
		return ;
	}
	FOR( j, 0, 2 ) {
		num[n] = j + '0';
		if ( n == N - 1 && !j )
			continue;
		vector<ll> base = b;
		FOR( i, 2, 11 )
			base[i] = base[i] * i + j;
		solve( n + 1, base );
	}
}

void sieve( ) {
	for ( ll i = 2; i < LIM; ++i ) {
		if ( !prime[i] ) {
			for ( ll j = i * i; j < LIM; j += i )
				prime[j] = i;
			primes.push_back( i );
		}
	}
}

int main( ) {
	sieve( );
	cout << "Case #1:" << endl;
	try {
		solve( 1, vector<ll> ( 11, 1 ) );
	} catch ( const char * ex ) {

	};
	return 0;
}