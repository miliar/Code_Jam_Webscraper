#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int T, A, B, K, ans;

bool f( int a, int b ) {
	return ( (a & b) < K );
}

int main( ) {

	scanf( "%d", &T );

	for ( int t = 0; t < T; ++t ) {

		ans = 0;

		scanf( "%d %d %d", &A, &B, &K );

		ans = 0;

		for ( int i = 0; i < A; ++i ) {
			int j = 0;			
			for ( ; j < B; ++j )
				if ( f(i,j) ) {
					++ans;
				}
		}

		printf( "Case #%d: %d\n", t+1, ans );

	}

	return 0;

}
