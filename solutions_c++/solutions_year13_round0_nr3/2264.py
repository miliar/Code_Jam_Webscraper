#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <math.h>
#include <algorithm>


struct BigNumber
{
	char digits[124];
	size_t nDigits;

	BigNumber()
	{
		nDigits = 0;
		memset( digits, 0, sizeof( digits ) );
	}

	BigNumber( const char *szDigits )
	{
		nDigits = strlen( szDigits );
		assert( nDigits <= 100 );
		for( size_t i = 0; i < nDigits; i++ )
		{
			char d = szDigits[ nDigits - i - 1 ];
			assert( d >= '0' && d <= '9' );
			digits[i] = d - '0';
		}
	}

	BigNumber( FILE *f )
	{
		nDigits = 0;
		while( true )
		{
			char c = fgetc( f );
			if ( c >= '0' && c <= '9' )
				digits[nDigits++] = c - '0';
			else break;
			assert( nDigits <= 100 );
		}
		assert( nDigits > 0 );

		for( size_t i = 0; i < nDigits / 2; i++ )
		{
			std::swap( digits[i], digits[nDigits - i - 1 ] );
		}
	}

	BigNumber operator * ( const BigNumber &b )
	{
		BigNumber result;

		for( size_t row = 0; row < b.nDigits; row++ )
		{
			int nup = 0;
			int ncur = b.digits[row];
			for( size_t i = 0; i < nDigits; i++ )
			{
				int mul = ncur * digits[i] + nup;
				int add = result.digits[row + i] + mul;
				result.digits[row+i] = add % 10;
				
				int ca = 1;
				while( add >= 10 )
				{
					add = add / 10 + result.digits[row+i+ca];
					result.digits[row+i+ca] = add % 10;
					ca++;
				}
			}
		}

		result.nDigits = 120;
		while( result.digits[result.nDigits] == 0 ) result.nDigits--;
		result.nDigits++;

		return result;
	}

	bool operator == ( const BigNumber &b ) const
	{
		if ( nDigits != b.nDigits ) return false;
		return memcmp( digits, b.digits, nDigits ) == 0;
	}

	bool operator < ( const BigNumber &b ) const
	{
		if ( nDigits < b.nDigits ) return true;
		else if ( nDigits > b.nDigits ) return false;
		for( size_t i = 0; i < nDigits; i++ )
		{
			if ( digits[ nDigits - i - 1 ] < b.digits[ nDigits - i - 1 ] ) return true;
			else if ( digits[ nDigits - i - 1 ] > b.digits[ nDigits - i - 1 ] ) return false;
		}
		return false;
	}

	void inc()
	{
		size_t pos = 0;
		while( true )
		{
			digits[pos] += 1;
			if ( digits[pos] == 10 )
			{
				digits[pos] = 0;
				pos++;
			}
			else break;
		}
		if ( pos == nDigits ) nDigits++;
		assert( nDigits <= 100 );
	}

	BigNumber( size_t n )
	{
		nDigits = 0;
		memset( digits, 0, sizeof( digits ) );
		while( n )
		{
			digits[ nDigits++ ] = n % 10;
			n /= 10;
		}
	}

	operator size_t()
	{
		assert( nDigits <= 8 && "too many digits" );
		size_t deg = 1;
		size_t result = 0;
		for( size_t i = 0; i < nDigits; i++ )
		{
			result += digits[i] * deg;
			deg *= 10;
		}

		return result;
	}

	bool isFair()
	{
		for( size_t i = 0; i <= nDigits / 2; i++ )
		{
			if ( digits[i] != digits[ nDigits - i - 1] )
				return false;
		}

		return true;
	}

	void nextFair()
	{
		assert( isFair() );
		int mid = nDigits / 2;
		int pos = mid;
		while( true )
		{
			digits[pos]++;
			if ( digits[pos] != 10 ) break;
			digits[pos] = 0;
			pos++;
		}
		if ( pos == nDigits )
			nDigits++;
		mid = nDigits / 2;
		for( pos = 0; pos < mid; pos++ )
			digits[pos] = digits[ nDigits - pos - 1];
	}

	void print( FILE *f )
	{
		for( size_t i = 0; i < nDigits; i++ )
		{
			fprintf( f, "%d", digits[ nDigits - i - 1 ] );
		}
	}
};

size_t test2( int a, int b )
{
	size_t result = 0;
	int i = (int)floor( sqrt( (double)a ) );
	if ( i * i < a ) i++;
	assert( i * i >= a );
	while( i * i <= b )
	{
		BigNumber n1( i );
		if ( n1.isFair() )
		{
			BigNumber n2( i * i );
			if ( n2.isFair() )
				result++;
		}
		i++;
	}

	return result;
}

void main()
{
/*	BigNumber biga( 1 );
	for( size_t a = 1; a < 10000; a++, biga.inc() )
	{
		BigNumber bigb( 1 );
		for( size_t b = 1; b < 1000; b++, bigb.inc() )
		{
			BigNumber bigc = biga * bigb;
			assert( (int) bigc == a * b );
		}
	}
*/
	FILE *fin  = fopen( "in.txt", "r" );
	assert( fin );

	int nCases;
	int ns = fscanf( fin, "%d\n", &nCases );
	assert( ns == 1 );

	FILE *fout = fopen( "out.txt", "w" );

	for( int iCase = 0; iCase < nCases; iCase++ )
	{
		BigNumber a( fin );
		BigNumber b( fin );
		BigNumber x, xsq;

		x.nDigits = a.nDigits / 2 + 1;
		x.digits[x.nDigits-1] = 1;

		while( true )
		{
			while( !x.isFair() ) x.inc();

			xsq = x * x;
			if ( !( xsq < a ) ) break;
			x.inc();
		}

		size_t count = 0;

		__int64 cnt = 0;
		int curDigits = 0;
		while( true )
		{
			cnt++;
			if ( !( xsq < b ) )
			{
				if ( !( xsq == b ) ) break;
			}

			if ( xsq.isFair() )
			{
				count++;
			}
/*
			BigNumber nf = x;
			nf.nextFair();
			do
			{
				x.inc();
			}
			while( !x.isFair() );
			assert( nf == x );
*/
			x.nextFair();
			xsq = x * x;

			if ( xsq.nDigits > curDigits )
			{
				curDigits = xsq.nDigits;
				printf( "curDigits: %d", curDigits ); 
			}
		}

		assert ( test2( a, b ) == count );
		fprintf( fout, "Case #%d: %d\n", iCase + 1, count );
	}

	fclose( fout );
	fclose( fin );
}

