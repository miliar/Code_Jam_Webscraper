// Syed Ghulam Akbar
// CodeJam 2014

#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

void main() {
	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	int testCount;
	scanf("%d",&testCount);

	// Setup the initial game state flags
	int Grid1[4][4];
	int Grid2[4][4];

	for (int test=1;test<=testCount;test++) {
		int row1, row2, number=-1, matches=0;

		// Get the first number grid row and layout
		cin >> row1;
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++)
				cin >> Grid1[i][j];

		// Get the second number grid row and layout
		cin >> row2;
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++)
				cin >> Grid2[i][j];

		// Process the two grid, and try to find the answer based on these grid layout
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++)
				if (Grid1[row1-1][i] == Grid2[row2-1][j])
				{
					matches++;
					number = Grid1[row1-1][i];
				}

		cout << "Case #" << test << ": ";
		
		// Check the matches count and print the results accordingly. If no matches
		// are found, then definitely volunteer is cheating
		if (matches == 0)
			cout << "Volunteer cheated!";
		// If more than one numbers matches, then bagician has mixed up the numbers incorrectly
		// when re-arranging, so it's bad magician
		else if (matches > 1)
			cout << "Bad magician!";
		// If only one match is found, it's our number
		else 
			cout << number;

		cout << endl;
	}
}
