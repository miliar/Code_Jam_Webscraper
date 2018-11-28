#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>
#include <stdlib.h>

// https://code.google.com/codejam/contest/11254486/dashboard#s=p0

// ZERO		E           O R   T       Z
// TWO                  O           W
// FOUR       F         O R     U
// FIVE     E F     I             V
// ONE      E         N O
// THREE    E+    H       R   T
// SEVEN    E+        N     S     V
// SIX              I       S
// EIGHT    E   G H I         T
// NINE     E       I N+

void addCount( const std::string &message, int target[256] ) {
	for( const char c : message ) {
		++ target[(unsigned char) c];
	}
}

int accountFor( int target[256], const std::string &token, const char identifier ) {
	int chars[256] = {};
	addCount( token, chars );
	const int found = target[(unsigned char) identifier] / chars[(unsigned char) identifier];
	for( int i = 0; i < 256; ++ i ) {
		target[i] -= chars[i] * found;
	}
	return found;
}

std::vector<int> countDigits( const std::string &message ) {
	int remaining[256] = {};
	addCount( message, remaining );
	std::vector<int> result( 10 );
	result[0] = accountFor( remaining, "ZERO", 'Z' ); // Z is unique to Zero
	result[2] = accountFor( remaining, "TWO", 'W' );  // etc.
	result[4] = accountFor( remaining, "FOUR", 'U' );
	result[5] = accountFor( remaining, "FIVE", 'F' );
	result[1] = accountFor( remaining, "ONE", 'O' );
	result[3] = accountFor( remaining, "THREE", 'R' );
	result[7] = accountFor( remaining, "SEVEN", 'V' );
	result[6] = accountFor( remaining, "SIX", 'S' );
	result[8] = accountFor( remaining, "EIGHT", 'G' );
	result[9] = accountFor( remaining, "NINE", 'I' );
	for( int i = 0; i < 256; ++ i ) {
		if( remaining[i] != 0 ) {
			std::cerr << "Failed: " << result[i] << " of " << i << " remain" << std::endl;
			throw std::invalid_argument( "Cannot perfectly match message" );
		}
	}
	return result;
}

int main( int argc, const char *const *const argv ) {
	if( argc != 1 ) {
		std::cerr
			<< "Usage: " << argv[0] << std::endl
			<< std::endl
			<< "Takes input on stdin" << std::endl;
		return EXIT_FAILURE;
	}

	long totalTests;
	std::cin >> totalTests;

	for( long n = 0; n < totalTests; ++ n ) {
		std::string input;
		std::cin >> input;
		const std::vector<int> result = countDigits( input );
		std::cout << "Case #" << (n + 1) << ": ";
		for( int i = 0; i < 10; ++ i ) {
			for( int j = 0; j < result[i]; ++ j ) {
				std::cout << (char) ('0' + i);
			}
		}
		std::cout << std::endl;
	}

	return EXIT_SUCCESS;
}
