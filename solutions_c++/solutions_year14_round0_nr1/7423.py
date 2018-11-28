#include <iostream>
#include <cstring>
using namespace std;

int TC, cnt[20], ans[20], n, r;

int main() {
	// your code goes here
	scanf( "%d", &TC );
	for( int cas = 1; cas <= TC; cas++ ) {
		memset( cnt, 0, sizeof( cnt ) );
		scanf( "%d", &r );
		for( int i = 1; i <= 4; i++ ) {
			for( int j = 1; j <= 4; j++ ) {
				int tmp;
				scanf( "%d", &tmp );
				if ( i == r ) {
					cnt[tmp]++;
				}
			}
		}
		scanf( "%d", &r );
		for( int i = 1; i <= 4; i++ ) {
			for( int j = 1; j <= 4; j++ ) {
				int tmp;
				scanf( "%d", &tmp );
				if ( i == r ) {
					cnt[tmp]++;
				}
			}
		}
		
		n = 0;
		for( int i = 1; i <= 16; i++ ) {
			if ( cnt[i] == 2 ) ans[n++] = i;
		}
		
		printf( "Case #%d: ", cas );
		if ( n == 0 ) {
			printf( "Volunteer cheated!\n");
		} else if ( n > 1 ) {
			printf( "Bad magician!\n" );
		} else {
			printf( "%d\n", ans[0] );
		}
	}
	return 0;
}