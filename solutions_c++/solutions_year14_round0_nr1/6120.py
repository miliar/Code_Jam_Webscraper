#include <iostream>
#include <fstream>

using namespace std;

void main()
{
	ifstream in("c:\\doom\\A-small-attempt1.in");
	ofstream out("c:\\doom\\out.txt");

	int iRounds;
	in >> iRounds;
	for (int i = 0; i < iRounds; ++i)
	{
		int guess1, guess2;
		int grid1[4][4], grid2[4][4];
		in >> guess1;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				in >> grid1[j][k];
			}
		}
		in >> guess2;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				in >> grid2[j][k];
			}
		}
		
		int guess = 0;
		int nGuesses = 0;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				if (grid2[guess2 - 1][k] == grid1[guess1 - 1][j])
				{
					++nGuesses;
					guess = grid2[guess2 - 1][k];
					break;
				}
			}
		}

		out << "Case #" << (i + 1) << ": ";
		if (nGuesses == 0)
		{
			out << "Volunteer cheated!";
		}
		else if (nGuesses == 1)
		{
			out << guess;
		}
		else
		{
			out << "Bad magician!";
		}
		out << endl;
	}
}