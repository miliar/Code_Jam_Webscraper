#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;


int t, ti;
int choose;
int card[17];
int grid[5][5];

int main( void )
{
	freopen( "A-small-attempt2.in", "r", stdin );
	freopen( "a.out", "w", stdout );

	int i, j;
	bool hasAns;
	int maxV;

	scanf( "%d", &t );

	for( ti = 1; ti <= t; ++ti ) {
		memset( card, 0, sizeof(card) );

		scanf( "%d", &choose );
		for( i = 1; i <= 4; ++i ) for( j = 1; j <= 4; ++j ) scanf( "%d", &grid[i][j] );
		for( i = 1; i <= 4; ++i ) ++card[grid[choose][i]];

		scanf( "%d", &choose );
		for( i = 1; i <= 4; ++i ) for( j = 1; j <= 4; ++j ) scanf( "%d", &grid[i][j] );
		for( i = 1; i <= 4; ++i ) ++card[grid[choose][i]];

		maxV = 0;
		hasAns = false;
		for( i = 1; i <= 16; ++i ) {
			if( card[i] == 2 ) {
				if( !hasAns ) {
					hasAns = true;
					maxV = i;
				} else {
					hasAns = false;
					break;
				}
			}
		}

		printf( "Case #%d: ", ti );
		if( hasAns ) printf( "%d\n", maxV );
		else puts( maxV ? "Bad magician!" : "Volunteer cheated!" );
	}

	return 0;
}
