/**
* File:		Round00_ProbC.cpp
* Title:	Google Code Jam 2015 - Qualification Round - Problem C - Dijkstra
* Author:	R.Quatrefoil
* Date:		2015-04-11
* Purpose:	Tile Polyominoes
* Notes:	Created using Microsoft Visual Studio 2013
*
*			Limits
*				Small dataset
*					T = 64.
*					1 <= X, R, C <= 4.
*				Large dataset
*					1 <= T <= 100.
*					1 <= X, R, C <= 20.
*				X is X-omino, RxC is grid rows and cols
*				Richard picks a specific X-omino
*				Gabriel tries to win using the specific X-omino plus any other X-ominoes he wants
*					(all covered, no overlap, no extending outside)
*				Gabriel wins if grid is covered
*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream iFile("Round00_ProbD_Input.txt", ios::in);
	ofstream oFile;		//will only open if iFile opens correctly

	int testCasesTotal = 0;		//total number of test cases to evaluate (1 <= T <= 100)
	int polyominoSize = 0;		//number of squares in the polyomino shape
	int rowCount = 0;		//number of rows in grid
	int colCount = 0;		//number of columns in grid
	bool canForceLoss = false;		//if game can be forced into loss then Richard wins, if game can always be won then Gabriel wins
	string winner;		//who will win the game

	if (iFile)
	{
		oFile.open("Round00_ProbD_Output.txt", ios::out | ios::trunc);

		iFile >> testCasesTotal;
		for (int currCase = 0; currCase < testCasesTotal; currCase++)		//evaluate all test cases
		{
			iFile >> polyominoSize;
			iFile >> rowCount;
			iFile >> colCount;
			canForceLoss = false;

			if (((rowCount * colCount) % polyominoSize) != 0)
			{
				canForceLoss = true;
			}
			else if ((rowCount <= (polyominoSize - 2)) || (colCount <= (polyominoSize - 2)))		//this isn't quite all of it, but it is enough for the small case
			{
				canForceLoss = true;
			}
			else if (polyominoSize >= 7)		//can always pick a hollow polyomino as forced choice
			{
				canForceLoss = true;
			}

			//create message for output
			if (canForceLoss)
				winner = "RICHARD";
			else
				winner = "GABRIEL";

			//output case to file
			oFile << "Case #" << (currCase + 1) << ": " << winner << endl;
		}

		iFile.close();
		oFile.close();
		cout << "Output successful!!" << endl;
	}
	else
	{
		cout << "Error opening input file!!" << endl;
	}

	cout << endl << endl << "Press Enter key to continue..." << endl;
	cin.get();
	return 0;
}//endfcn main