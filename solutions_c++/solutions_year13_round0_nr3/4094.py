#include <stdio.h>
#include <math.h>


bool isPalin( long long a ) {
	long long t = 0;
	long long b = a;

	while( a ) {
		t *= 10;
		t += ( a % 10 );
		a /= 10;
	}

	if( b == t ) {
		return true;
	}
	return false;
}

int getCount( long long a, long long b ) {
	long long i;
	int res = 0;

	for( i = sqrt( (long double) a ); i * i <= b; i ++ ) {
		if( i * i < a ) {
			continue;
		}

		if( isPalin( i ) && isPalin( i * i ) ) { 
			res ++;
		}
	}
	return res;
}

int main() {
	int T;
	scanf( "%d", &T );

	for( int tt = 1; tt <= T; tt ++ ) {
		long long a, b;

		scanf( "%lld %lld", &a, &b );

		printf( "Case #%d: %d\n", tt, getCount( a, b ) );
	}

	return 0;
}
