#include <fstream>
#include <algorithm>
#include <climits>

using namespace std;

#define MAX_SWATH	100

unsigned int LawnRectPattern[MAX_SWATH][MAX_SWATH];

int main()
{
	ifstream		InFile("B-large.in");
	ofstream		OutFile("B-large.out", ios_base::ate || ios_base::out);
	unsigned int	RowMaxHeights[MAX_SWATH], ColMaxHeights[MAX_SWATH], nRow, nCol, nIndex = 0, nCases, nMaxRowHeight, nCaseRows, nCaseCols;
	bool			bFinished;

	if (OutFile.is_open())
	{
		InFile >> nCases;
		
		while (nCases--)
		{
			fill(ColMaxHeights, ColMaxHeights + MAX_SWATH, 0);
			
			InFile >> nCaseRows >> nCaseCols;
			
			for (nRow = 0; nRow < nCaseRows; ++nRow)
			{
				nMaxRowHeight = 0;
				
				for (nCol = 0; nCol < nCaseCols; ++nCol)
				{
					InFile >> LawnRectPattern[nRow][nCol];
					
					if (LawnRectPattern[nRow][nCol] > nMaxRowHeight)
						nMaxRowHeight = LawnRectPattern[nRow][nCol];

					if (LawnRectPattern[nRow][nCol] > ColMaxHeights[nCol])
						ColMaxHeights[nCol] = LawnRectPattern[nRow][nCol];
				}
				
				RowMaxHeights[nRow] = nMaxRowHeight;
			}

			bFinished = false;
			
			for (nRow = 0; ((!bFinished) && (nRow < nCaseRows)); ++nRow)
			{
				for (nCol = 0; nCol < nCaseCols; ++nCol)
				{	
					if ((LawnRectPattern[nRow][nCol] < RowMaxHeights[nRow]) && (LawnRectPattern[nRow][nCol] < ColMaxHeights[nCol]))
					{
						OutFile << "Case #" << ++nIndex << ": " << "NO" << endl;
						bFinished = true;
						break;
					}
				}
			}

			if (!bFinished)
			{
				OutFile << "Case #" << ++nIndex << ": " << "YES" << endl;
			}
		}

	}

	return 0;
}