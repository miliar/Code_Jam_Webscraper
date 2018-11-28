//

#include <stdlib.h>
#include <inttypes.h>

#include <iostream>
#include <sstream>
#include <vector>
#include <set>


typedef std::set< uint64_t > s_t;


bool is_ps( char const * s, size_t const ll )
{
	size_t const l( ll - 1 );
	size_t const d( ll >> 1 );
	
	for( size_t i( 0 ); i != d; ++i )
	{
		if( s[ i ] != s[ l - i ] )
			return false;
	}

	return true;
}

bool is_p( uint64_t const x )
{
	std::stringstream ss;
	ss << x;
	std::string const & s( ss.str() );
	
	return is_ps( s.c_str(), s.length() );
}

bool is_pfs( uint64_t const x )
{
	return is_p( x ) && is_p( x*x );
}


int main()
{
	s_t q;
	
	for( int x( 1 ); x != 32; ++x )
	{
		uint64_t xx( x * x );
		
		if( is_p( x ) && is_p( xx ) )
			q.insert( xx );
	}
	
	size_t count( 0 );
	std::cin >> count;
	
	for( size_t n( 0 ); n != count; ++n )
	{
		uint64_t a( 0 ), b( 0 );
		std::cin >> a >> b;
		
		size_t c( 0 );
		for( s_t::const_iterator i( q.begin() ), i_end( q.end() ); i != i_end; ++i )
		{
			if( ( *i >= a ) && ( *i <= b ) )
				++c;
		}

		std::cout << "Case #" << ( n + 1 ) << ": " << c << std::endl;
	}

	return 0;
}