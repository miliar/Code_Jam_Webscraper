#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <string>

int main() {
	std::freopen( "A-large.in", "r", stdin );
	std::freopen( "A-large.out", "w", stdout );
	int numCases;
	std::cin >> numCases;
  for( int curCase = 1; curCase <= numCases; curCase++ ) {
		std::string shyPpl;
		int sMax;
		int standing = 0;
		int needed = 0;
		std::cout << "Case #" << curCase <<": ";
		std::cin >> sMax;
		std::cin >> shyPpl;
		for( int sChar = 0; sChar < (int)shyPpl.length(); ++sChar ) {
			if( standing < sChar ){
				needed += sChar - standing;
				standing += sChar - standing;
			}
			standing += ( shyPpl[ sChar ] - '0' );
		}
		if( curCase != numCases ){
			std::cout << needed << std::endl;
		}
		else {
			std::cout << needed;
		}
	}
	return 0;
}