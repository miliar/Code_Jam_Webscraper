/**
 * Tittle:	2015 Google Code Jam Round2 - PA
 * Author:	Cheng-Shih, Wong
 * Date:	2015/05/30
 */

// include files
#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

// definitions
#define FOR(i,a,b) for( int i=(a),_n=(b); i<=_n; ++i )
#define clr(x,v) memset( x, v, sizeof(x) )
#define N 105

// declarations
int t;
char grid[N][N];
int RhasA[N];
int ChasA[N];
int r, c;
int d[4][2] = {
	{ -1,  0 },
	{  0,  1 },
	{  1,  0 },
	{  0, -1 }
};


// functions
int c2d( char op )
{
	switch( op ) {
	case '^': return 0;
	case '>': return 1;
	case 'v': return 2;
	case '<': return 3;
	default: return -1;
	}
}

inline bool valid( int x, int y )
{
	return (1<=x && x<=r && 1<=y && y<=c);
}

// main function
int main( void )
{
	int ans;
	int x, y;
	bool possible;
	bool found;
	int dir;

	// input
	scanf( "%d", &t );

	FOR( ti, 1, t ) {
		scanf( "%d%d", &r, &c );
		FOR( i, 1, r ) 
			scanf( "%s", grid[i]+1 );

		// solve
		clr( RhasA, 0 );
		clr( ChasA, 0 );
		FOR( i, 1, r ) FOR( j, 1, c ) if( grid[i][j] != '.' ) {
			++RhasA[i];
			++ChasA[j];
		}

		ans = 0;
		possible = true;
		FOR( i, 1, r ) FOR( j, 1, c ) if( grid[i][j] != '.' ) {
			x = i; y = j;
			dir = c2d( grid[i][j] );
			found = false;
			
			x += d[dir][0]; y += d[dir][1];
			while( valid(x,y) ) {
				if( grid[x][y] != '.' ) {
					found = true;
					break;
				}
				x += d[dir][0]; y += d[dir][1];
			}

			if( !found ) {
				if( RhasA[i]>=2 || ChasA[j]>=2 )
					++ans;
				else possible = false;
			}

			if( !possible ) break;
		}

		// output
		printf( "Case #%d: ", ti );
		if( possible ) printf( "%d\n", ans );
		else puts("IMPOSSIBLE");
	}
	
	return 0;
}
