#include <cstdio>

int main() {
	int cas, t, x, r, c, temp;
	scanf( "%d", &t );
	for( cas=1;cas<=t;cas++ ) {
		scanf( "%d%d%d", &x, &r, &c );
		if( r > c ) {
			temp = r;
			r = c;
			c = temp;
		}
		if( x == 1 ) {
			printf( "Case #%d: GABRIEL\n", cas);

		} else if( x == 2 ) {
			if( r % x == 0 || c % x == 0 ) {
				printf( "Case #%d: GABRIEL\n", cas);
			} else {
				printf( "Case #%d: RICHARD\n", cas);
			}

		} else if( x == 3 ) {
			if( r == 1 ) {
				printf( "Case #%d: RICHARD\n", cas);	
			} else if( r == 2 ) {
				if( c == 3 ) {
					printf( "Case #%d: GABRIEL\n", cas);
				} else {
					printf( "Case #%d: RICHARD\n", cas);
				}
			} else if( r == 3 ) {
				printf( "Case #%d: GABRIEL\n", cas);
			} else {
				printf( "Case #%d: RICHARD\n", cas);
			}

		} else {
			if( r < 3 ) {
				printf( "Case #%d: RICHARD\n", cas);
			} else if( r == 3 ) {
				if( c == 3 ) {
					printf( "Case #%d: RICHARD\n", cas);
				} else {
					printf( "Case #%d: GABRIEL\n", cas);
				}
			} else {
				printf( "Case #%d: GABRIEL\n", cas);
			}
		}
	}
	return 0;
}