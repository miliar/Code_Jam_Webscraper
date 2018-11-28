#include <iostream>

#include <fstream>
#include <sstream>
#include <cstdlib>
#include <stdlib.h>
#include <string.h>
#include <string>

using namespace std;

const bool TRUE = 1, FALSE = 0;
const int NumOfRows = 4, NumOfCols = 4;

int main (int argc, char *argv[]) {
	ifstream ins(argv[1]);

	if ( !ins ) {
	cerr << "Cannot open: infile\n";

		exit(1);

	}


	ofstream outs(argv[2]);

	if ( !outs ) {
	cerr << "Cannot open: outfile\n";

		exit(1);

	}




	int T = 0;	// T Number of cases.

	string str;
	getline( ins, str );
	T = atoi( str.c_str() );
	str.clear();

	for ( int i = 0; i < T; i++ ) {		// For each case
		str.clear();
		getline( ins, str );
		int selection1;
		selection1 = atoi( str.c_str() );	// The first selection of the volunteer
		int FirstArrangement[NumOfRows][NumOfCols];
		for (  int j = 0; j < NumOfRows && getline( ins, str ); j++ ) {		// Get the rows of first arrangement
			istringstream ss( str );
			for ( int k = 0; k < NumOfCols && !ss.eof(); k++ ) {
				string x;
				getline( ss, x, ' ' );
				FirstArrangement[j][k] = atoi( x.c_str() );
				
			}
		}
		str.clear();
		getline( ins, str );
		int selection2;
		selection2 = atoi( str.c_str() );	// The second selection of the volunteer
		int SecondArrangement[NumOfRows][NumOfCols];
		for (  int j = 0; j < NumOfRows && getline( ins, str ); j++ ) {		// Get the rows of first arrangement
			istringstream ss( str );
			for ( int k = 0; k < NumOfCols && !ss.eof(); k++ ) {
				string x;
				getline( ss, x, ' ' );
				SecondArrangement[j][k] = atoi( x.c_str() );
				
			}
		}
		
		int matches = 0;
		int selectedCard = 0;
		for ( int j = 0; j < NumOfCols; j++ ) {		// Look for the selection
			for ( int k = 0; k < NumOfCols; k++ ) {
				if ( SecondArrangement[selection2-1][j] == FirstArrangement[selection1-1][k] ) {
					matches++;
					selectedCard = SecondArrangement[selection2-1][j];
				}
			}
		}

		if ( matches == 1 ) {	// Selected card found
			outs << "Case #" << i+1 << ": " << selectedCard << "\n";
		} else if ( matches == 0 ) {	// No match. Volunteer cheated.
			outs << "Case #" << i+1 << ": Volunteer cheated!\n";
		} else if ( matches > 1 ) {	// Multiple matches. Bad magician.
			outs << "Case #" << i+1 << ": Bad magician!\n";
		}

	}		
		
	outs.close();
	ins.close();


}