#include <stdlib.h>
#include <map>
#include <vector>
#include <string>
#include <iostream>

int main()
{
	int T;
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );
	std::cin >> T;
	std::vector<std::string> base = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

	for( int t = 1; t <= T; t++ )
	{
		std::string letters;
		std::cin >> letters;
		std::map<char, int> charMap;
		for( size_t i = 0; i < base.size(); i++ )
			for( size_t j = 0; j < base[ i ].length(); j++ )
				charMap[ base[ i ][ j ] ] = 0;
		for( size_t i = 0; i < letters.length(); ++i )
			charMap[ letters[ i ] ]++;
		std::vector<int> numbers;
		numbers.resize( 10 );
		numbers[ 0 ] = charMap[ 'Z' ];
		numbers[ 2 ] = charMap[ 'W' ];
		numbers[ 4 ] = charMap[ 'U' ];
		numbers[ 3 ] = charMap[ 'R' ] - numbers[ 4 ] - numbers[ 0 ];
		numbers[ 6 ] = charMap[ 'X' ];
		numbers[ 7 ] = charMap[ 'S' ] - numbers[ 6 ];
		numbers[ 5 ] = charMap[ 'V' ] - numbers[ 7 ];
		numbers[ 8 ] = charMap[ 'G' ];
		numbers[ 1 ] = charMap[ 'O' ] - numbers[ 0 ] - numbers[ 2 ] - numbers[ 4 ];
		numbers[ 9 ] = charMap[ 'I' ] - numbers[ 5 ] - numbers[ 6 ] - numbers[ 8 ];
		std::cout << "Case #" << t << ": ";
		for( size_t i = 0; i < numbers.size(); i++ )
			for( size_t j = 0; j < numbers[ i ]; j++ )
				std::cout << i;
			std::cout << std::endl;
	}
}