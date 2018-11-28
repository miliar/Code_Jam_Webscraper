#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <assert.h>

void main()
{
	FILE *fin  = fopen( "in.txt", "r" );
	assert( fin );

	int nCases;
	int ns = fscanf( fin, "%d\n", &nCases );
	assert( ns == 1 );

	FILE *fout = fopen( "out.txt", "w" );

	for( int iCase = 0; iCase < nCases; iCase++ )
	{
		int ysize, xsize;
		ns = fscanf( fin, "%d %d\n", &ysize, &xsize );
		assert( ns == 2 );
		assert( ysize >= 1 && ysize <= 100 );
		assert( xsize >= 1 && xsize <= 100 );

		char board[100][100];

		int y, x;
		for( y = 0; y < ysize; y++ )
		{
			for( x = 0; x < xsize; x++ )
			{
				int h;
				ns = fscanf( fin, "%d", &h );
				assert( ns == 1 );
				assert( h >= 1 && h <= 100 );
				board[y][x] = h;
			}
		}

		bool ok = true;
		for( y = 0; y < ysize; y++ )
		{
			for( x = 0; x < xsize; x++ )
			{
				int h = board[y][x];

				bool oky = true, okx = true;
				for( int t = 0; t < ysize; t++ )
				{
					if ( board[t][x] > h )
						oky = false;
				}
				for( int t = 0; t < xsize; t++ )
				{
					if ( board[y][t] > h )
						okx = false;
				}
				if ( !okx && !oky )
				{
					ok = false;
					break;
				}
			}
		}

		fprintf( fout, "Case #%d: %s", iCase + 1, ok ? "YES\n" : "NO\n" );
	}

	fclose( fin );
	fclose( fout );
}
