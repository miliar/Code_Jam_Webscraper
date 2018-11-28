#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	int testCases =0;
	const int FOUR = 4;
	char letter =' ';
	bool xWin = false;
	bool oWin = false;
	bool nComplete = false;

	//read from File
	string localFileName = "";
	string localOutputFile = "output.out";

	cin >> localFileName;

	ifstream readFile(localFileName);
	ofstream writeFile(localOutputFile);

	//cin >> testCases;
	readFile >> testCases;

	for (int test = 0; test < testCases; test++)
	{
		//-- Reset --//
		char board [FOUR][FOUR] =
		{
			letter,letter,letter,letter,
			letter,letter,letter,letter,
			letter,letter,letter,letter,
			letter,letter,letter,letter
		};
		xWin = false;
		oWin = false;
		nComplete = false;
		int oCountRow = 0;
		int xCountRow = 0;
		int tCountRow = 0;
		int empty =0;

		int xCountColumn[FOUR] = {0,0,0,0};
		int oCountColumn[FOUR] = {0,0,0,0};
		int tCountColumn[FOUR] = {0,0,0,0};
		//-- Reset --//


		//Read In Board;
		for (int i = 0; i < FOUR; i++)		//column
		{
			for (int j = 0; j < FOUR; j++)	//row
			{
				//cin >> letter;
				readFile >> letter;
				board [i][j] = letter;
				switch (letter)
				{
				case 'X':
					xCountRow++;
					xCountColumn[j]++;
					break;
				case 'O':
					oCountRow++;
					oCountColumn[j]++;
					break;
				case 'T':
					tCountRow++;
					tCountColumn[j]++;
					break;
				default:
					empty++;
					break;
				}
			}
			//-- STAGE 1 --//
			if(xCountRow + tCountRow == FOUR)
				xWin = true;
			if(oCountRow + tCountRow == FOUR)
				oWin = true;
			oCountRow = 0;
			xCountRow = 0;
			tCountRow = 0;
		}

		//-- STAGE 2 --//
		for(int i=0; i< FOUR; i++)
		{
			if(xCountColumn[i] + tCountColumn[i] == FOUR)	// FOUR x's in a column
				xWin = true;
			if(oCountColumn[i] + tCountColumn[i] == FOUR)	// FOUR o's in a column
				oWin = true;
		}

		//-- STAGE 3 --//
		if(!xWin && !oWin)	//If all False no one has won yet
		{
			xCountRow = 0;
			oCountRow = 0;
			tCountRow = 0;

			int r = 0;
			int c = 0;
			//Diagonal Left to Right
			for (int i = 0; i < FOUR; i++)
			{
				switch (board[r][c])
				{
				case 'X':
					xCountRow++;
					break;
				case 'O':
					oCountRow++;
					break;
				case 'T':
					tCountRow++;
					break;
				default:
					break;
				}
				r++;
				c++;
			}
			//-- STAGE 3.1 --//
			if(xCountRow + tCountRow == FOUR)
				xWin = true;
			if(oCountRow + tCountRow == FOUR)
				oWin = true;


			xCountRow = 0;
			oCountRow = 0;
			tCountRow = 0;
			r = 0;
			c = FOUR-1;
			//Diagonal Right to Left
			for (int i = 0; i < FOUR; i++)
			{
				switch (board[r][c])
				{
				case 'X':
					xCountRow++;
					break;
				case 'O':
					oCountRow++;
					break;
				case 'T':
					tCountRow++;
					break;
				default:
					break;
				}
				r++;
				c--;
			}
			//-- STAGE 3.1 --//
			if(xCountRow + tCountRow == FOUR)
				xWin = true;
			if(oCountRow + tCountRow == FOUR)
				oWin = true;
		}

		if(!oWin && !xWin && empty > 0)
			nComplete = true;

		writeFile << "Case #" << test+1 << ": ";

		if(xWin)
			writeFile << "X won";
		else if(oWin)
			writeFile << "O won";
		else if(nComplete)
			writeFile << "Game has not completed";
		else
			writeFile << "Draw";

		if(test != testCases-1)
			writeFile <<endl;
	}
}