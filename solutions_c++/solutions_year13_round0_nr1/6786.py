#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

const char X = 'X';
const char O = 'O';
const char T = 'T';
const char EMPTY = '.';

const string X_WIN = "X won";
const string O_WIN = "O won";
const string DRAW = "Draw";
const string UNFINISHED = "Game has not completed";

int main()
{
	int numTests;

	cin >> numTests;

	int testNum;

	for(testNum = 0; testNum < numTests; ++testNum)
	{
		char board[16] = "000000000000000";

		// 0  1  2  3
		// 4  5  6  7
		// 8  9  10 11
		// 12 13 14 15
	
		int y;
		for(y = 0; y < 16; ++y)
		{
			cin >> board[y];
		}

		int gameStatus = 0; 		// X won = 1, O won = 2; Draw = 3; Unfinished = 4

		int i; 		// 0, 4, 8 ,12
		// Rows
		for(i = 0; i < 13; i += 4)
		{
			int rowCount_X = count (board + i, board + i + 4, X);
			int rowCount_T = 5;
			if(rowCount_X >= 3)
			{
				if(rowCount_X == 4)
				{	
					gameStatus = 1;
					break;
				}
				rowCount_T = count (board + i, board + i + 4, T);
				if(rowCount_T == 1)
				{
					gameStatus = 1;
					break;
				}
			}

			int rowCount_O = count (board + i, board + i + 4, O);		
			if(rowCount_O >= 3)
			{
				if(rowCount_O == 4)
				{
					gameStatus = 2;
					break;
				}
				if(rowCount_T < 5 && rowCount_T == 1)
				{
					gameStatus = 2;
					break;
				}else{
					rowCount_T = count (board + i, board + i + 4, T);
					if (rowCount_T == 1){
						gameStatus = 2;
						break;
					}
				}
			}
		}

		if (gameStatus == 1 || gameStatus == 2)
		{
			// Don't do anything, we already have a result
		}else{
			// Columns
			for(i = 0; i < 4; ++i)
			{
				char tempColumn[4] = { board[i], board[i+4], board[i+8], board[i+12] };

				int columnCount_X = count (tempColumn, tempColumn + 4, X);
				int columnCount_T = 5;
				if(columnCount_X >= 3)
				{
					if(columnCount_X == 4)
					{	
						gameStatus = 1;
						break;
					}
					columnCount_T = count (tempColumn, tempColumn + 4, T);
					if(columnCount_T == 1)
					{
						gameStatus = 1;
						break;
					}
				}

				int columnCount_O = count (tempColumn, tempColumn + 4, O);		
				if(columnCount_O >= 3)
				{
					if(columnCount_O == 4)
					{
						gameStatus = 2;
						break;
					}
					if(columnCount_T < 5 && columnCount_T == 1)
					{
						gameStatus = 2;
						break;
					}else{
						columnCount_T = count (tempColumn, tempColumn + 4, T);
						if (columnCount_T == 1){
							gameStatus = 2;
							break;
						}
					}
				}
			}
		}
		if (gameStatus == 1 || gameStatus == 2)
		{
			//Don't do anything, we already have a winner
		}else{
			// Check diagonals
			char tempDiagLeft[4] = { board[0], board[5], board[10], board[15] };

			int diagLeft_X = count (tempDiagLeft, tempDiagLeft + 4, X);
			int diagLeft_T = 5; 
			if (diagLeft_X >= 3)
			{
				if(diagLeft_X == 4)
					gameStatus = 1;
				diagLeft_T = count (tempDiagLeft, tempDiagLeft + 4, T);
				if( diagLeft_T == 1)
					gameStatus = 1;
			}

			int diagLeft_O = count (tempDiagLeft, tempDiagLeft + 4, O);
		
			if (diagLeft_O >= 3)
			{
				if (diagLeft_O == 4)
					gameStatus = 2;
				if (diagLeft_T < 5 && diagLeft_T == 1){
					gameStatus = 2; 
				}else{
					diagLeft_T = count (tempDiagLeft, tempDiagLeft + 4, T);
					if (diagLeft_T == 1)
						gameStatus = 2;
				}
			}
		}

		if (gameStatus == 1 || gameStatus == 2)
		{
			//Don't do anything, we already have a winner
		}else{
			// Do diag right if winner not already found
			char tempDiagRight[4] = { board[3], board[6], board[9], board[12] };

			int diagRight_X = count (tempDiagRight, tempDiagRight + 4, X);
			int diagRight_T = 5; 
			if (diagRight_X >= 3)
			{
				if(diagRight_X == 4)
					gameStatus = 1;
				diagRight_T = count (tempDiagRight, tempDiagRight + 4, T);
				if( diagRight_T == 1)
					gameStatus = 1;
			}

			int diagRight_O = count (tempDiagRight, tempDiagRight + 4, O);
		
			if (diagRight_O >= 3)
			{
				if (diagRight_O == 4)
					gameStatus = 2;
				if (diagRight_T < 5 && diagRight_T == 1){
					gameStatus = 2; 
				}else{
					diagRight_T = count (tempDiagRight, tempDiagRight + 4, T);
					if (diagRight_T == 1)
						gameStatus = 2;
				}
			}
		}
		if(gameStatus == 0)
		{		
			int countEmpty = count (board, board+16, EMPTY);
			gameStatus = (countEmpty > 0) ? 4 : 3; 
		}

		cout << "Case #" << testNum + 1 << ": ";
		switch(gameStatus)
		{
			case 1:
				cout << X_WIN;
				break;
			case 2:
				cout << O_WIN;
				break;
			case 3:
				cout << DRAW;
				break;
			case 4:
				cout << UNFINISHED;
				break;
		}

		cout << endl;
	}

	return 0;
}
