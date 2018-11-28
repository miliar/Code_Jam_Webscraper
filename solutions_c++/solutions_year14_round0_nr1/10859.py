#include <iostream>
#include <fstream>
#include <vector>
#include <assert.h>

using namespace std;

int main( int argc, char* argv[] )
{
	assert(argc>1);

	ifstream inputFile(argv[1]);
	ofstream outputFile("output.out");

	int T;
	inputFile >> T;

	int cards[4][4];
	int row1[4];
	int row2[4];
	for( int t = 1; t <= T; t++ )
	{
		int first, second;
		inputFile >> first;
		first = first-1;

		outputFile << "Case #" << t << ": ";

		// get first arrangement
		for( int i = 0; i < 4; i++ )
		{
			for( int j = 0; j < 4; j++ )
			{
				inputFile >> cards[i][j];
			}
		}
		for( int i = 0; i < 4; i++ )
		{
			row1[i] = cards[first][i];
		}

		inputFile >> second;
		second = second-1;

		// get second arrangement
		for( int i = 0; i < 4; i++ )
		{
			for( int j = 0; j < 4; j++ )
			{
				inputFile >> cards[i][j];
			}
		}
		for( int i = 0; i < 4; i++ )
		{
			row2[i] = cards[second][i];
		}
		
		// compare
		int match, count = 0;
		for( int i = 0; i < 4; i++ )
		{
			for( int j = 0; j < 4; j++ )
			{
				if( row1[i] == row2[j] )
				{
					match = row1[i];
					count++;
				}
			}
		}

		if( count == 1 ) // magic trick worked
			outputFile << match << endl;
		else if( count > 1 ) // bad magician
			outputFile << "Bad magician!" << endl;
		else // volunteer cheated
			outputFile << "Volunteer cheated!" << endl;
	}

	return 0;
}
