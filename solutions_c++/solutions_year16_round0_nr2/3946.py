#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <assert.h>
#include <limits.h>
#include <memory.h>


class stack
{
public:
	bool c[ 100 ];
	int size;

	stack() : size( 0 ) {}
	stack& operator = ( const stack &s )
	{
		size = s.size;
		memcpy( c, s.c, sizeof( c[ 0 ] ) * size );
		return *this;
	}

	void flip( int n )
	{
		assert( n >= 0 && n <= size );
		for ( int i = 0; i < n / 2; i++ )
		{
			bool t = c[ i ];
			c[ i ] = !( c[ n - i - 1 ] );
			c[ n - i - 1 ] = !t;
		}
		if ( n % 2 )
			c[ n / 2 ] = !c[ n / 2 ];
	}

	bool isValid() const
	{
		for ( auto i = 0; i < size; i++ )
			if ( !c[ i ] ) return false;
		return true;
	}
};


int solve_brute( const stack &s, int step )
{
	if ( s.isValid() ) return step;
	if ( step == s.size ) return -1;
	int best = INT_MAX;
	for ( auto cs = 1; cs <= s.size; cs++ )
	{
		stack s1 = s;
		s1.flip( cs );
		int res = solve_brute( s1, step + 1 );
		if ( res >= 0 && ( res < best ) )
			best = res;
	}
	return best < INT_MAX ? best : -1;
}

int solve_fast( const stack &s )
{
	int res = 0;
	bool cur = true;
	for ( int i = s.size - 1; i >= 0; i-- )
	{
		if ( s.c[ i ] != cur )
		{
			res++;
			cur = s.c[ i ];
		}
	}
	return res;
}

int main()
{
	FILE *fin, *fout;
	if ( !( fin = fopen( "B-large.in", "r" ) ) ) return -1;

	if ( !( fout = fopen( "res.txt", "w" ) ) ) return -1;

	int nCases;
	fscanf( fin, "%d\n", &nCases );
	for ( int iCase = 1; iCase <= nCases; iCase++ )
	{
		stack s;
		while ( true )
		{
			char c = fgetc( fin );
			if ( c == '+' ) s.c[ s.size++ ] = true;
			else if ( c == '-' ) s.c[ s.size++ ] = false;
			else
			{
				assert( s.size > 0 && s.size <= 100 );
				int res = solve_fast( s );
				fprintf( fout, "Case #%d: %d\n", iCase, res );
				assert( c == '\n' || ( c == -1 && iCase == nCases ) );
				break;
			}
		}
	}

	fclose( fin );
	fclose( fout );

/*

	for ( int i = 2; i < 1000; i++ )
	{
		stack s;
		s.size = 0;
		int x = i;
		while ( x )
		{
			s.c[ s.size++ ] = x % 2 ? true : false;
			x /= 2;
		}

		int sb = solve_brute( s, 0 );
		assert( sb >= 0 );
		int sf = solve_fast( s );
		assert( sf == sb );
		printf( "%d: %d\n", i, sb );
	}*/
}
