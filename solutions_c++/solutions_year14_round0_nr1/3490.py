#include <iostream>
#include <vector>
#include <algorithm>

int main(int argc, char* argv[]) {

	unsigned int T, a, v, w, c;
	std::vector<int> row(4);

	std::cin >> T;

	for( unsigned int t = 1; t <= T; t++ ) {

		c = 0;
		
		std::cin >> a;
		for( unsigned int i = 1; i <= 4; i++ ) {
			if( i == a ) {
				std::cin >> row[0] >> row[1] >> row[2] >> row[3];
			} else {
				std::cin >> v >> v >> v >> v;
			}
		}
		
		std::cin >> a;
		for( unsigned int i = 1; i <= 4; i++ ) {
			if( i == a ) {
				for( unsigned int j = 1; j <= 4; j++ ) {
					std::cin >> v;
					if( std::find(row.begin(), row.end(), v) != row.end() ) {
						c++; w = v;
					}
				}
			} else {
				std::cin >> v >> v >> v >> v;
			}
		}

		std::cout << "Case #" << t << ": ";
		switch( c ) {
			case 0: std::cout << "Volunteer cheated!"; break;
			case 1: std::cout << w;  break;
			default: std::cout << "Bad magician!"; break;
		}

		std::cout << std::endl;

	}

	return 0;
}