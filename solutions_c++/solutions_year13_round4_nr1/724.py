#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const long long mod = 1000002013;

struct event{
	
	bool type; // {} = 01
	int s, p;	
	
	event () {}
	
	event ( int _type, int _s, int _p ){
		type = _type; s = _s; p = _p;
	}

	friend bool operator < ( const event &A, const event &B ){
		if ( A.s == B.s ) return A.type < B.type;
		return A.s < B.s;
	}
	
} niz[2000 + 1];

int T, N, M, cnt;

inline long long calc ( int lo, int hi, int p ){
	long long k = ( long long ) hi - lo;
	long long sum = ( long long ) N * k - (long long) k * (k - 1) / 2;
	sum %= mod; sum = ( long long ) sum * p;
	return sum % mod;  
}
	
inline void solve( int t ){

	long long init = 0, final = 0;

	cnt = 0;
	scanf( "%d%d", &N, &M );
	
	for ( int i = 0; i < M; ++i ){
		int lo, hi, p; scanf( "%d%d%d", &lo, &hi, &p );
		niz[cnt++] = event( 0, lo, p );
		niz[cnt++] = event( 1, hi, p );	
		init += calc( lo, hi, p ); init %= mod;
	}

	//printf( "%lld\n", init );
	//printf( "cnt: %d\n", cnt );
	
	sort( niz, niz + cnt );
	for ( int i = 0; i < cnt; ++i ){
		if ( !niz[i].type ) continue;
		for ( int j = i - 1; j >= 0 && niz[i].p > 0; --j ){
			if ( niz[j].type || niz[j].p == 0 ) continue;
			if ( niz[j].p >= niz[i].p ){
				final += calc( niz[j].s, niz[i].s, niz[i].p ); final %= mod;
				niz[j].p -= niz[i].p; niz[i].p = 0;
			} else {
				final += calc( niz[j].s, niz[i].s, niz[j].p ); final %= mod;	
				niz[i].p -= niz[j].p; niz[j].p = 0;
			}
	//		printf( "-- %lld\n", final );
		}
	}
	
	//printf( "%lld %lld\n", init, final );
	long long sol = init - final + 2 * mod; sol %= mod;
	printf( "Case #%d: %lld\n", t, sol );
	
}

int main( void ){

	scanf( "%d", &T );
	for ( int i = 0; i < T; ++i ) solve( i + 1 );

	return 0;
	
}
