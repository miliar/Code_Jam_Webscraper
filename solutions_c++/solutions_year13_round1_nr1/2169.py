#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <limits.h>
#include <assert.h>
#include <math.h>


typedef unsigned __int64 uint64;

int dotest( uint64 r0, uint64 ntint )
{
	int count = 0;
	long double tt = 0;
	long double r = r0;


	while( true )
	{
		tt += ( r + 1 ) * ( r + 1 ) - r * r;
		r += 2;
		if ( tt > ntint ) break;
		count++;
	}

	return count;
}

void main()
{
	FILE *fin = fopen( "in.txt", "r" );
	assert( fin );

	FILE *fout = fopen( "out.txt", "w" );
	assert( fout );



	int nCases;
	int nRead = fscanf( fin, "%d\n", &nCases );
	assert( nRead == 1 );

	for( int iCase = 0; iCase < nCases; iCase++ )
	{
		uint64 r0;
		uint64 ntint;

		nRead = fscanf( fin, "%I64d %I64d", &r0, &ntint );
		assert( nRead == 2 );

		long double ldR0 = r0;
		long double ldTint = ntint;

		long double ldn = ( - ( 2 * ldR0 - 1 ) + sqrt( ( 2 * ldR0 - 1 ) * ( 2 * ldR0 - 1 ) + 8 * ntint ) ) / 2;
//		long double ldn = ( -1 + sqrt( 1 - 8 * ldR0 + 4 * ntint ) ) / 2;
		uint64 n = floor( ldn );
		n /= 2;

//		assert( n == dotest( r0, ntint ) );

		fprintf( fout, "Case #%d: %I64u\n", iCase + 1,  n );
	}

	fclose( fin );
	fclose( fout );
}
