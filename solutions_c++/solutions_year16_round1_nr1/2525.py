#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <assert.h>
#include <string>
#include <deque>


std::string solve_brute_rec( const std::string &cur, std::deque< char > s )
{
	if ( s.empty() ) return cur;
	else
	{
		char c = s[ 0 ];
		s.erase( s.begin() );
		std::string s1 = solve_brute_rec( cur + c, s );
		std::string s2 = solve_brute_rec( c + cur, s );
		if ( s1 >= s2 ) return s1;
		else return s2;
	}
}

std::string solve_brute( const std::string &s )
{
	std::deque< char > sd( s.begin(), s.end() );
	return solve_brute_rec( std::string(), sd );
}

std::string solve_fast( std::string s )
{
	std::string result;
	result.push_back( s.front() );
	s.erase( s.begin() );

	while ( !s.empty() )
	{
		char c = s.front();
		if ( c > result[ 0 ] )
			result.insert( result.begin(), c );
		else if ( c == result[ 0 ] )
		{
			if ( c < result.back() )
				result.push_back( c );
			else result.insert( result.begin(), c );
		}
		else result.push_back( c );
		s.erase( s.begin() );
	}

	return result;
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
		std::string s;
		while ( true )
		{
			char c = fgetc( fin );
			if ( c == '\n' || c == -1 ) break;
			assert( c >= 'A' && c <= 'Z' );
			s.push_back( c );
		}

		std::string result1 = solve_fast( s );
//		std::string result2 = solve_brute( s );
//		assert( result1 == result2 );
		fprintf( fout, "Case #%d: %s\n", iCase, result1.c_str() );
	}

	fclose( fin );
	fclose( fout );
/*
	for ( int i = 0; i < 100000; i++ )
	{
		std::string s;
		int size = rand() * 5 / RAND_MAX + 1;
		s.resize( size );
		for ( int j = 0; j < size; j++ )
			s[ j ] = 'A' + rand() * 20 / RAND_MAX;

		std::string result1 = solve_fast( s );
		std::string result2 = solve_brute( s );
		assert( result1 == result2 );
	}*/
}
