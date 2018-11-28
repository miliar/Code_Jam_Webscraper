#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

const int MAX_N = 100+10;
int mat[MAX_N][MAX_N];
int rowMax[MAX_N], colMax[MAX_N];

int main ( )
{
	freopen ( "B-large.in", "r", stdin );
	freopen ( "B.out", "w", stdout );

	int nCases;
	scanf ( "%d", &nCases );
	for ( int curCase = 1; curCase <= nCases; ++curCase )
	{
		int h, w;
		scanf ( "%d%d", &h, &w );
		
		fill ( rowMax, rowMax+MAX_N, -1 );
		fill ( colMax, colMax+MAX_N, -1 );
		for ( int i = 0; i < h; ++i )
			for ( int j = 0; j < w; ++j )
			{
				scanf ( "%d", &mat[i][j] );
				rowMax[i] = max ( rowMax[i], mat[i][j] );
				colMax[j] = max ( colMax[j], mat[i][j] );
			}
		
		bool ok = true;
		for ( int i = 0; i < h; ++i )
			for ( int j = 0; j < w; ++j )
				ok &= ( mat[i][j] >= min ( rowMax[i], colMax[j] ) );
		
		printf ( "Case #%d: ", curCase );
		if ( ok ) printf ( "YES\n" );
		else printf ( "NO\n" );
	}
	
	return 0;
}
