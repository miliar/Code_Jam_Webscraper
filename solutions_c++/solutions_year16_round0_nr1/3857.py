#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <assert.h>
#include <algorithm>


__int64 solve( __int64 n )
{
	if ( n == 0 ) return -1;

	bool visit[ 10 ];
	std::fill( visit, visit + 10, false );
	int numVisit = 0;
	int res = 1;
	__int64 mul = 1;
	while ( true )
	{
		__int64 x = n * mul;
		while ( x )
		{
			int d = x % 10;
			if ( !visit[ d ] )
			{
				visit[ d ] = true;
				numVisit++;
			}
			x /= 10;
		}

		if ( numVisit == 10 )
			return n * mul;
		mul++;

		assert( mul < 1000 );
	}
}

int main()
{
	FILE *fin, *fout;
	if ( !( fin = fopen( "A-large.in", "r" ) ) ) return -1;

	if ( !( fout = fopen( "res.txt", "w" ) ) ) return -1;

	int nCases;
	fscanf( fin, "%d\n", &nCases );
	for ( int iCase = 1; iCase <= nCases; iCase++ )
	{
		int n;
		fscanf( fin, "%d", &n );
		__int64 s = solve( n );

		fprintf( fout, "Case #%d: ", iCase );
		if ( s >= 0 ) fprintf( fout, "%I64d\n", s );
		else fprintf( fout, "INSOMNIA\n" );
	}

	fclose( fin );
	fclose( fout );

/*
	for ( int i = 1; i < 2000000; i++ )
	{
		__int64 s = solve( i );
		if ( i % 1000 == 0 )
			printf( "%d: %I64d\n", i, s );
	}
*/
}
