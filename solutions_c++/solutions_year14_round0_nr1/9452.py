#include <iostream>
#include <fstream>
#include <vector>

int main () {

	std::ifstream input ( "input.txt" );
	std::ofstream output ( "output.txt" );
	int T,a1,a2,r;
	int c1[4][4],c2[4][4];
	bool v;
	bool d;
	input >> T;
	for ( int i = 0 ; i < T ; ++i ) {

		v = false;
		d = false;
		input >> a1;
		a1 -= 1;
		for ( int j = 0 ; j < 4 ; ++j ) {

			for ( int k = 0 ; k < 4 ; ++k ) {

				input >> c1[j][k];
			}
		}
		input >> a2;
		a2 -= 1;
		for ( int j = 0 ; j < 4 ; ++j ) {

			for ( int k = 0 ; k < 4 ; ++k ) {

				input >> c2[j][k];
			}
		}
		for ( int j = 0 ; j < 4 ; ++j ) {

			for ( int k = 0 ; k < 4 ; ++k ) {
				if ( c1[a1][j] == c2[a2][k] ) {

					r = c1[a1][j];
					if ( !v )
						v = true;
					else {
						if ( !d )
							d = true;
					}
				}
			}
		}
		if ( v && d )
			output << "Case #" << i+1 << ": Bad magician!" << std::endl;
		if ( !v )
			output << "Case #" << i+1 << ": Volunteer cheated!" << std::endl;
		if ( v && !d )
			output << "Case #" << i+1 << ": " << r << std::endl;
	}
	return 0;
}
