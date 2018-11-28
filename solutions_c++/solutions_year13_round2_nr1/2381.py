#include <stdio.h>
#include <cmath>

#define FOR( i, i0, n ) for( int i = i0; i < n; i++ )

int main() {
	freopen( "A-small-attempt4.in", "r", stdin );
	freopen( "A-small-attempt4.out", "w", stdout );
	// freopen( "run.in", "r", stdin );
	// freopen( "run.out", "w", stdout );

	int T;
	scanf( "%d", &T );
	FOR( k, 0, T ) {
		int a, n, m[100], count = 0;
		scanf( "%d%d", &a, &n );
		FOR ( i, 0, n )
				scanf( "%d", &m[i] );

		if( a > 1 ) {
			FOR( i, 0, n - 1 ) {
				int q = i;
				FOR( j, i + 1, n )
					if( m[j] < m[q] )
						q = j;
				int c = m[q];
				m[q] = m[i];
				m[i] = c;
			}
			FOR( i, 0, n ) {
				int w = 0, r = count;
				while( m[i] >= a ) {
					a += a - 1;
					// printf("%d\n", a);
					count++;
					if( count - r > n - i - 1 )
						goto exit;
				}
				a += m[i];
			}
		} else
			count = n;

exit:	if( count > n )
			count = n;
		printf( "Case #%d: %d\n", k + 1, count);
	}
	return 0;
}