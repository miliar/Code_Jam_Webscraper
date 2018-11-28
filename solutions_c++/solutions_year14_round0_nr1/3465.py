#include <iostream>
#include <cstdio>

using namespace std;

const int MAXN = 8;

int first, second;
int a[MAXN][MAXN], b[MAXN][MAXN];

void read() {
	int i, j;

	scanf ( "%d", &first );

	for ( i = 0; i < 4; ++ i ) {
		for ( j = 0; j < 4; ++ j ) {
			scanf ( "%d", &a[i][j] );
		}
	}

	scanf ( "%d", &second );

	for ( i = 0; i < 4; ++ i ) {
		for ( j = 0; j < 4; ++ j ) {
			scanf ( "%d", &b[i][j] );
		}
	}

}

void solve( int test ) {
	int i, j, cnt = 0, num = 0;

	first --;
	second --;

	for ( i = 0; i < 4; ++ i ) {
		for ( j = 0; j < 4; ++ j ) {
			if ( a[first][i] == b[second][j] ) {
				cnt ++;
				num = a[first][i];
				break;
			}
		}
	}

	if ( cnt == 0 ) printf ( "Case #%d: Volunteer cheated!\n", test );
	else if ( cnt == 1 ) printf ( "Case #%d: %d\n", test, num );
	else printf ( "Case #%d: Bad magician!\n", test );

}

int main() {
	int i, tests;

	scanf ( "%d", &tests );

	for ( i = 1; i <= tests; ++ i ) {
		read();
		solve( i );
	}

	return 0;

}