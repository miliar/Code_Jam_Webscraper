#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <assert.h>
#include <vector>
#include <algorithm>


class Erato
{
public:
	uint32_t process( uint32_t n )
	{
		if ( n <= m_lastProcessed )
		{
			bool b = std::binary_search( m_vPrime.begin(), m_vPrime.end(), n );
			if ( b ) return 0;

			for ( auto d : m_vPrime )
				if ( n % d == 0 ) return d;

			assert( false );
			return 0;
		}
		else
		{
			uint32_t res = 0;
			while ( m_lastProcessed < n )
				res = pvtProcess( ++m_lastProcessed );
			return res;
		}
	}

	Erato()
	{
		m_vPrime.reserve( 10000 );
		m_vPrime.push_back( 2 );
		m_vPrime.push_back( 3 );
		m_lastProcessed = 3;
	}

	auto size() const { return m_vPrime.size(); }
	auto operator [] ( size_t index ) const { return m_vPrime[ index ]; }
	void dump()
	{
		for ( auto i : m_vPrime )
			printf( "%d\t", i );
	}

	auto back() const { return m_vPrime.back(); }
protected:
	std::vector< uint32_t > m_vPrime;

	uint32_t pvtProcess( uint32_t n )
	{
		if ( n <= 3 ) return 0;

		for ( size_t i = 0; i < m_vPrime.size(); i++ )
			if ( n % m_vPrime[ i ] == 0 ) return m_vPrime[ i ];

		m_vPrime.push_back( n );

		return 0;
	}

	uint32_t m_lastProcessed;
} g_erato;


struct Coin
{
	bool digits[ 50 ];
	int size;
	Coin( int s )
	{
		size = s;
		memset( digits, 0, sizeof( digits ) );
		digits[ 0 ] = true;
		digits[ size - 1 ] = true;
	}

	bool next()
	{
		int p = size - 2;
		while ( p > 0 )
		{
			if ( !digits[ p ] )
			{
				digits[ p ] = true;
				break;
			}
			else
			{
				digits[ p ] = false;
				p--;
			}
		}

		return p > 0;
	}

	__int64 number( int base )
	{
		__int64 res = 0;
		__int64 dom = 1;
		for ( int p = size - 1; p >= 0; p-- )
		{
			res += (__int64)( digits[ p ] ) * dom;
			dom *= base;
		}
		return res;
	}

	void printf()
	{
		for ( int i = 0; i < size; i++ )
			::printf( "%c", digits[ i ] ? '1' : '0' );
	}

	void fprintf( FILE *f )
	{
		for ( int i = 0; i < size; i++ )
			::fprintf( f, "%c", digits[ i ] ? '1' : '0' );
	}
};

int main()
{
/*	FILE *fin, *fout;
	if ( !( fin = fopen( "B-large.in", "r" ) ) ) return -1;

	if ( !( fout = fopen( "res.txt", "w" ) ) ) return -1;

	int nCases;
	fscanf( fin, "%d\n", &nCases );
	for ( int iCase = 1; iCase <= nCases; iCase++ )
	{
	}

	fclose( fin );
	fclose( fout );*/


/*	int needCount = 50;
	int count = 0;
	Coin coin( 16 );
	while ( true )
	{
		bool ok = true;
		__int64 divisors[ 9 ];
		for ( int base = 2; base <= 10; base++ )
		{
			auto v = coin.number( base );
			auto d = g_erato.process( v );
			if ( !d )
			{
				ok = false;
				break;
			}
			
			assert( d != v );
			divisors[ base - 2 ] = d;
		}

		if ( ok )
		{
			int n2 = coin.number( 2 );
			coin.printf();
			for ( int i = 0; i < 9; i++ )
				printf( " %I64d", divisors[ i ] );
			printf( "\n" );
			count++;
			if ( count == needCount ) break;
		}

		bool bNext = coin.next();
		assert( bNext );
	}
*/

	FILE *fout;
	if ( !( fout = fopen( "res.txt", "w" ) ) ) return -1;

	fprintf( fout, "Case #1:\n" );

	int needCount = 50;
	int count = 0;
	Coin coin( 16 );

	while ( true )
	{
		bool ok = true;
		__int64 divisors[ 9 ] = { 0 };
		for ( int base = 2; base <= 10; base++ )
		{
			auto v = coin.number( base );
			for ( int td = 2; td < 100; td++ )
			{
				if ( v % td == 0 && td != v )
				{
					divisors[ base - 2 ] = td;
					break;
				}
			}
			if ( !divisors[ base - 2 ] )
			{
				ok = false;
				break;
			}
		}

		if ( ok )
		{
			coin.fprintf( fout );
			for ( int i = 0; i < 9; i++ )
				fprintf( fout, " %I64d", divisors[ i ] );
			fprintf( fout, "\n" );
			count++;
			if ( count == needCount ) break;
		}
		bool bNext = coin.next();
		assert( bNext );
	}


	fclose( fout );
}
