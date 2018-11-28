#include <fstream>
#include <iostream>
#include <cstring>
using namespace std;

#define MAX_ROW			4
#define MAX_COLUMN		4
#define MAX_SQUARE		16
#define MAX_TRIALS		2
#define INVALID_CARD	17

int main()
{
	int			nCases, nVolunteerRow, nRow, nCol, nCard, nTrial, nSolution, nIdx, nCase = 1;
	int			SelectionsArr[MAX_SQUARE];
	bool		bCanBeSolved;
	ifstream	InFile("A-small-attempt0.in");
	ofstream	OutFile("A-small-attempt0.out", ios_base::ate || ios_base::out);

	InFile >> nCases;

	if (OutFile.is_open())
	{
		while (nCases--)
		{
			nSolution = INVALID_CARD;
			bCanBeSolved = false;
			memset(SelectionsArr, 0, MAX_SQUARE * sizeof(int));

			for (nTrial = 0; nTrial < MAX_TRIALS; ++nTrial)
			{
				InFile >> nVolunteerRow;

				for (nRow = 1; nRow < nVolunteerRow; ++nRow)
				{
					for (nCol = 1; nCol <= MAX_COLUMN; ++nCol)
					{
						InFile >> nCard;
					}
				}

				for (nCol = 1; nCol <= MAX_COLUMN; ++nCol)
				{
					InFile >> nCard;

					SelectionsArr[nCard - 1] = SelectionsArr[nCard - 1] + 1;
				}
				
				for (++nRow; nRow <= MAX_ROW; ++nRow)
				{
					for (nCol = 1; nCol <= MAX_COLUMN; ++nCol)
					{
						InFile >> nCard;
					}
				}
			}

			for (nIdx = 0; nIdx < MAX_SQUARE; ++nIdx)
			{
				if (SelectionsArr[nIdx] == 2)
				{
					if (bCanBeSolved == true)
						break;
				
					bCanBeSolved = true;
					nSolution = nIdx + 1;
				}
			}

			OutFile << "Case #" << nCase++ << ": ";
			
			if (nIdx == MAX_SQUARE)
			{
				if (bCanBeSolved)
					OutFile << nSolution << endl;
				else
					OutFile << "Volunteer cheated!" << endl;
			}
			else
				OutFile << "Bad magician!" << endl;
		}
	}

	return 0;
}