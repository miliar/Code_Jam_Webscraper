// Google Codejam
// Problem A - Tic-Tac-Toe-Tomek
// By Jake Randolph B Muncada
// On April 13, 2013

#include <iostream>
#include <stdio.h>
#include <fstream>

using namespace std;

int main(void) {
	ifstream input("A-large.in");
	ofstream output("output.txt");
	int testCases, test, i, j;
	bool unfinished;
	char arr[4][4];
	input >> testCases;
	for ( test = 1; test <= testCases; test++ ) {
		
		unfinished = false;
		
		for ( i = 0; i < 4; i++ )
			for ( j = 0; j < 4; j++ ) {
				input >> arr[i][j];
				if (arr[i][j] == '.')
					unfinished = true;
			}
			
		output << "Case #" << test << ": ";
		
		// First row
		if ( (arr[0][0] == 'X' || arr[0][0] == 'T') &&
			 (arr[0][1] == 'X' || arr[0][1] == 'T') &&
			 (arr[0][2] == 'X' || arr[0][2] == 'T') &&
			 (arr[0][3] == 'X' || arr[0][3] == 'T') )
			output << "X won" << endl;
		else if ( (arr[0][0] == 'O' || arr[0][0] == 'T') &&
			 	  (arr[0][1] == 'O' || arr[0][1] == 'T') &&
			 	  (arr[0][2] == 'O' || arr[0][2] == 'T') &&
			 	  (arr[0][3] == 'O' || arr[0][3] == 'T') )
			output << "O won" << endl;
		//Second row
		else if ( (arr[1][0] == 'O' || arr[1][0] == 'T') &&
			 	  (arr[1][1] == 'O' || arr[1][1] == 'T') &&
			 	  (arr[1][2] == 'O' || arr[1][2] == 'T') &&
			 	  (arr[1][3] == 'O' || arr[1][3] == 'T') )
			output << "O won" << endl;
		else if ( (arr[1][0] == 'X' || arr[1][0] == 'T') &&
			 	  (arr[1][1] == 'X' || arr[1][1] == 'T') &&
			 	  (arr[1][2] == 'X' || arr[1][2] == 'T') &&
			 	  (arr[1][3] == 'X' || arr[1][3] == 'T') )
			output << "X won" << endl;
		// Third row
		else if ( (arr[2][0] == 'O' || arr[2][0] == 'T') &&
			 	  (arr[2][1] == 'O' || arr[2][1] == 'T') &&
			 	  (arr[2][2] == 'O' || arr[2][2] == 'T') &&
			 	  (arr[2][3] == 'O' || arr[2][3] == 'T') )
			output << "O won" << endl;
		else if ( (arr[2][0] == 'X' || arr[2][0] == 'T') &&
			 	  (arr[2][1] == 'X' || arr[2][1] == 'T') &&
			 	  (arr[2][2] == 'X' || arr[2][2] == 'T') &&
			 	  (arr[2][3] == 'X' || arr[2][3] == 'T') )
			output << "X won" << endl;
		// Fourth row
		else if ( (arr[3][0] == 'X' || arr[3][0] == 'T') &&
			 	  (arr[3][1] == 'X' || arr[3][1] == 'T') &&
			 	  (arr[3][2] == 'X' || arr[3][2] == 'T') &&
			 	  (arr[3][3] == 'X' || arr[3][3] == 'T') )
			output << "X won" << endl;
		else if ( (arr[3][0] == 'O' || arr[3][0] == 'T') &&
			 	  (arr[3][1] == 'O' || arr[3][1] == 'T') &&
			 	  (arr[3][2] == 'O' || arr[3][2] == 'T') &&
			 	  (arr[3][3] == 'O' || arr[3][3] == 'T') )
			output << "O won" << endl;
		// First column
		else if ( (arr[0][0] == 'X' || arr[0][0] == 'T') &&
			 	  (arr[1][0] == 'X' || arr[1][0] == 'T') &&
			 	  (arr[2][0] == 'X' || arr[2][0] == 'T') &&
			 	  (arr[3][0] == 'X' || arr[3][0] == 'T') )
			output << "X won" << endl;
		else if ( (arr[0][0] == 'O' || arr[0][0] == 'T') &&
			 	  (arr[1][0] == 'O' || arr[1][0] == 'T') &&
			 	  (arr[2][0] == 'O' || arr[2][0] == 'T') &&
			 	  (arr[3][0] == 'O' || arr[3][0] == 'T') )
			output << "O won" << endl;
		// Second column
		else if ( (arr[0][1] == 'X' || arr[0][1] == 'T') &&
			 	  (arr[1][1] == 'X' || arr[1][1] == 'T') &&
			 	  (arr[2][1] == 'X' || arr[2][1] == 'T') &&
			 	  (arr[3][1] == 'X' || arr[3][1] == 'T') )
			output << "X won" << endl;
		else if ( (arr[0][1] == 'O' || arr[0][1] == 'T') &&
			 	  (arr[1][1] == 'O' || arr[1][1] == 'T') &&
			 	  (arr[2][1] == 'O' || arr[2][1] == 'T') &&
			 	  (arr[3][1] == 'O' || arr[3][1] == 'T') )
			output << "O won" << endl;
		// Third column
		else if ( (arr[0][2] == 'X' || arr[0][2] == 'T') &&
			 	  (arr[1][2] == 'X' || arr[1][2] == 'T') &&
			 	  (arr[2][2] == 'X' || arr[2][2] == 'T') &&
			 	  (arr[3][2] == 'X' || arr[3][2] == 'T') )
			output << "X won" << endl;
		else if ( (arr[0][2] == 'O' || arr[0][2] == 'T') &&
			 	  (arr[1][2] == 'O' || arr[1][2] == 'T') &&
			 	  (arr[2][2] == 'O' || arr[2][2] == 'T') &&
			 	  (arr[3][2] == 'O' || arr[3][2] == 'T') )
			output << "O won" << endl;
		// Fourth column
		else if ( (arr[0][3] == 'X' || arr[0][3] == 'T') &&
			 	  (arr[1][3] == 'X' || arr[1][3] == 'T') &&
			 	  (arr[2][3] == 'X' || arr[2][3] == 'T') &&
			 	  (arr[3][3] == 'X' || arr[3][3] == 'T') )
			output << "X won" << endl;
		else if ( (arr[0][3] == 'O' || arr[0][3] == 'T') &&
			 	  (arr[1][3] == 'O' || arr[1][3] == 'T') &&
			 	  (arr[2][3] == 'O' || arr[2][3] == 'T') &&
			 	  (arr[3][3] == 'O' || arr[3][3] == 'T') )
			output << "O won" << endl;
		// Slash
		else if ( (arr[0][0] == 'X' || arr[0][0] == 'T') &&
			 	  (arr[1][1] == 'X' || arr[1][1] == 'T') &&
			 	  (arr[2][2] == 'X' || arr[2][2] == 'T') &&
			 	  (arr[3][3] == 'X' || arr[3][3] == 'T') )
			output << "X won" << endl;
		else if ( (arr[0][0] == 'O' || arr[0][0] == 'T') &&
			 	  (arr[1][1] == 'O' || arr[1][1] == 'T') &&
			 	  (arr[2][2] == 'O' || arr[2][2] == 'T') &&
			 	  (arr[3][3] == 'O' || arr[3][3] == 'T') )
			output << "O won" << endl;
		// Backslash
		else if ( (arr[0][3] == 'X' || arr[0][3] == 'T') &&
			 	  (arr[1][2] == 'X' || arr[1][2] == 'T') &&
			 	  (arr[2][1] == 'X' || arr[2][1] == 'T') &&
			 	  (arr[3][0] == 'X' || arr[3][0] == 'T') )
			output << "X won" << endl;
		else if ( (arr[0][3] == 'O' || arr[0][3] == 'T') &&
			 	  (arr[1][2] == 'O' || arr[1][2] == 'T') &&
			 	  (arr[2][1] == 'O' || arr[2][1] == 'T') &&
			 	  (arr[3][0] == 'O' || arr[3][0] == 'T') )
			output << "O won" << endl;
		else if ( unfinished )
			output << "Game has not completed" << endl;
		else
			output << "Draw" << endl;
			
			
	}
	return 0;
}

