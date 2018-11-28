#include <stdio.h>
#include <assert.h>
#include <vector>
#include <set>


__int64 solveBrute( int a, int b, int k )
{
	__int64 res = 0;
	for( int ia = 0; ia < a; ia++ )
		for( int ib = 0; ib < b; ib++ )
		{
			if ( ( ia & ib ) < k ) res++;
		}
	return res;
}
/*
__int64 solveForFullBits( int nbits )
{
	if ( nbits > 0 )
	{
		__int64 res = 3;
		for( int i = 1; i < nbits; i++ )
			res *= 3;
		return res;
	}
	else return 0;
}

int lastBit( int n )
{
	assert( n > 0 );
	int res = 0;
	while( n )
	{
		res++;
		n >>= 1;
	}
	return res;
}

__int64 solveGood( int a, int b, int k )
{
	int lastBitA = lastBit( a );
	int lastBitB = lastBit( b );
	int lastBitK = lastBit( k );
	int minLastBit = std::min( lastBitA, std::min( lastBitB, lastBitK ) );
	__int64 res = solveForFullBits( minLastBit - 1 );
}
*/
int main( int argc, char **args )
{
	const char *szInFile;
	if ( argc >= 2 )
		szInFile = args[1];
	else szInFile = "test.txt";

	FILE *fin = NULL, *fout = NULL;
	fin = fopen( szInFile, "r" );
	if ( !fin ) return -1;

	fout = fopen( "res.txt", "w" );
	if ( !fout ) return -1;

	int nCases;
	if ( fscanf( fin, "%d", &nCases ) != 1 )
		return -1;

	for( int iCase = 1; iCase <= nCases; iCase++ )
	{
		int a, b, k;
		int n = fscanf( fin, "%d %d %d", &a, &b, &k );
		assert( n == 3 );

		__int64 res = solveBrute( a, b, k );
		fprintf( fout, "Case #%d: %I64d\n", iCase, res );
	}

	if ( fin ) fclose( fin );
	if ( fout ) fclose( fout );
}
