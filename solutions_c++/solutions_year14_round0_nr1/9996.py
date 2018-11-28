//

#include <stdlib.h>
#include <inttypes.h>

#include <iostream>
#include <sstream>
#include <vector>
#include <set>


typedef std::set< uint64_t > s_t;


int main()
{
	size_t count( 0 );
	std::cin >> count;
	
	for( size_t n( 0 ); n != count; ++n )
	{
		s_t s;

		size_t a( 0 );
		std::cin >> a;
		
		for( size_t i( 1 ); i != 5; ++i )
		{
			size_t x1, x2, x3, x4;
			std::cin >> x1 >> x2 >> x3 >> x4;
			if( i == a )
			{
				s.insert( x1 );
				s.insert( x2 );
				s.insert( x3 );
				s.insert( x4 );
			}
		}

		size_t b( 0 );
		std::cin >> b;
		size_t c( 0 ), r( 0 );
		
		for( size_t i( 1 ); i != 5; ++i )
		{
			size_t x[ 4 ];
			std::cin >> x[ 0 ] >> x[ 1 ] >> x[ 2 ] >> x[ 3 ];
			if( i == b )
				for( size_t j( 0 ); j != 4; ++j )
					if( s.find( x[ j ] ) != s.end() )
					{
						++c;
						r = x[ j ];
					}
		}
		
		if( c == 0 )
			std::cout << "Case #" << ( n + 1 ) << ": " << "Volunteer cheated!" << std::endl;
		else if( c == 1 )
			std::cout << "Case #" << ( n + 1 ) << ": " << r << std::endl;
		else
			std::cout << "Case #" << ( n + 1 ) << ": " << "Bad magician!" << std::endl;
	}

	return 0;
}