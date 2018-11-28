#include <iostream>

using namespace std;

int resp1;
int grid1[4][4];
int resp2;
int grid2[4][4];

int main () {

	int numcases = 0;
	cin >> numcases;
	for (int cc = 1; cc <= numcases; ++cc) {
		
		cin >> resp1;
		for ( int l = 0; l < 4; ++l )
			for ( int c = 0; c < 4; ++c )
				cin >> grid1[l][c];
				
		cin >> resp2;
		for ( int l = 0; l < 4; ++l )
			for ( int c = 0; c < 4; ++c )
				cin >> grid2[l][c];
				
		// get matches
		int matches = 0;
		int matchitem = 0;
		for ( int l = 0; l < 4; ++l )
			for ( int c = 0; c < 4; ++c ) {
				if ( grid1[resp1-1][l] == grid2[resp2-1][c] ) {
					++matches;
					matchitem = grid1[resp1-1][l];
				}
			}
		
		if ( matches == 1 ) {
			cout << "Case #" << cc << ": " << matchitem << "\n";
		}
		else if ( matches > 1 ) {
			cout << "Case #" << cc << ": Bad magician!\n";
		}
		else {
			cout << "Case #" << cc << ": Volunteer cheated!\n";
		}
	}
	return 0;
}
			
			
	
