#include <iostream>
#include <string>
#include <stdlib.h>

// https://code.google.com/codejam/contest/4304486/dashboard#s=p0

std::string solve_last_word( const std::string &input ) {
	std::string result;
	char firstchar = '\0';
	for( char c : input ) {
		if( c >= firstchar ) {
			result.insert( result.begin( ), c );
			firstchar = c;
		} else {
			result.push_back( c );
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
		std::string answer = solve_last_word( input );
		std::cout << "Case #" << (n + 1) << ": " << answer << std::endl;
	}

	return EXIT_SUCCESS;
}
