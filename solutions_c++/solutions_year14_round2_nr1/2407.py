#include <stdio.h>
#include <assert.h>
#include <vector>
#include <set>
#include <algorithm>


struct Code_t
{
	std::vector< char > chars;
	std::vector< int > nums;
};

void decode( const char *str, Code_t &code )
{
	char cur = *str;
	int nCur = 1;
	str++;
	while( *str )
	{
		if ( *str == cur )
			nCur++;
		else
		{
			code.chars.push_back( cur );
			code.nums.push_back( nCur );
			cur = *str;
			nCur = 1;
		}
		str++;
	}
	code.chars.push_back( cur );
	code.nums.push_back( nCur );
}

bool compatible( const Code_t &c1, const Code_t &c2 )
{
	if ( c1.chars.size() != c2.chars.size() ) return false;
	for( size_t i = 0; i < c1.chars.size(); i++ )
		if ( c1.chars[i] != c2.chars[i] ) return false;
	return true;
}

int findTurns( int target, const std::vector< int > &nums )
{
	int res = 0;
	for( size_t i = 0; i < nums.size(); i++ )
		res += std::abs( target - nums[i] );
	return res;
}

int numTurns( const std::vector< int > &nums )
{
	int nmin = nums[0], nmax = nums[0];
	for( size_t i = 0; i < nums.size(); i++ )
	{
		nmin = std::min( nmin, nums[i] );
		nmin = std::min( nmin, nums[i] );
	}

	int best = findTurns( nmin, nums );
	for( int i = nmin + 1; i <= nmax; i++ )
	{
		int t = findTurns( i, nums );
		best = std::min( best, t );
	}
	return best;
}

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
	if ( fscanf( fin, "%d\n", &nCases ) != 1 )
		return -1;

	for( int iCase = 1; iCase <= nCases; iCase++ )
	{
		int nStrings;
		int n = fscanf( fin, "%d", &nStrings );
		assert( n == 1 );

		bool bCanSolve = true;
		std::vector< Code_t > codes;
		for( int i = 0; i < nStrings; i++ )
		{
			char str[256];
			fscanf( fin, "%s\n", str );
			Code_t code;
			decode( str, code );
			codes.push_back( code );
			if ( !compatible( code, codes[0] ) )
				bCanSolve = false;
		}

		fprintf( fout, "Case #%d: ", iCase );
		if ( !bCanSolve )
		{
			fprintf( fout, "Fegla Won\n" );
			continue;
		}

		Code_t &code0 = codes[0];
		std::vector< int > nums;
		nums.resize( nStrings );

		int res = 0;
		for( size_t cc = 0; cc < code0.chars.size(); cc++ )
		{
			for( int istr = 0; istr < nStrings; istr++ )
				nums[istr] = codes[istr].nums[cc];
			res += numTurns( nums );
		}

		fprintf( fout, "%d\n", res );
	}

	if ( fin ) fclose( fin );
	if ( fout ) fclose( fout );
}
