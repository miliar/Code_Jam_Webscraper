//Tic-Tac-Toe-Tomek

#include <iostream>
#include <fstream>

int main()
{
	short numberOfCases;
	char board[16];
	int i, j;
	bool boardIsFull, isWin, hasT;
	char winSymbol;
	int tx, ty;
	std::ofstream fout("out.out") ;

	std::cin >> numberOfCases;

	for(j = 1; j <= numberOfCases; ++j)
	{
		boardIsFull = true;
		isWin = false;
		hasT = false;
		for(i = 0; i < 16; ++i)
		{
			std::cin >> board[i];
			if(board[i] == '.') boardIsFull = false;
			if(board[i] == 'T') tx = i%4, ty =i/4, hasT = true;
		}
		if(hasT) board[tx + ty*4] = 'X';
	
		for(i = 0; i < 4; ++i)
		{
			if(board[i] == 'X' && board[i] == board[i + 1*4] && board[i + 1*4] == board[i + 2*4] && board[i + 2*4] == board[i + 3*4])
			{
				winSymbol = 'X';
				isWin = true;
				break;
			} else if(board[i*4] == 'X' && board[i*4] == board[i*4 + 1] && board[i*4 + 1]  == board[i*4 + 2] && board[i*4 + 2] == board[i*4 + 3])
			{
				winSymbol = 'X';
				isWin = true;
				break;
			}
		}
		
		if(!isWin && board[0] == 'X' && board[0] == board[1 + 1*4] && board[1 + 1*4] == board[2 + 2*4] && board[2 + 2*4] == board[3 + 3*4])
		{
				winSymbol = 'X';
				isWin = true;
		} else if(!isWin && board[3] == 'X' && board[3] == board[2 + 1*4] && board[2 + 1*4] == board[1 + 2*4] && board[1 + 2*4] == board[3*4])
		{
				winSymbol = 'X';
				isWin = true;
		}

		if(hasT) board[tx + ty*4] = 'O';

		for(i = 0; !isWin && i < 4; ++i)
		{
			if(board[i] == 'O' && board[i] == board[i + 1*4] && board[i + 1*4] == board[i + 2*4] && board[i + 2*4] == board[i + 3*4])
			{
				winSymbol = 'O';
				isWin = true;
				break;
			} else if(board[i*4] == 'O' && board[i*4] == board[i*4 + 1] && board[i*4 + 1]  == board[i*4 + 2] && board[i*4 + 2] == board[i*4 + 3])
			{
				winSymbol = 'O';
				isWin = true;
				break;
			}
		}
		
		if(!isWin && board[0] == 'O' && board[0] == board[1 + 1*4] && board[1 + 1*4] == board[2 + 2*4] && board[2 + 2*4] == board[3 + 3*4])
		{
				winSymbol = 'O';
				isWin = true;
		} else if(!isWin && board[3] == 'O' && board[3] == board[2 + 1*4] && board[2 + 1*4] == board[1 + 2*4] && board[1 + 2*4] == board[3*4])
		{
				winSymbol = 'O';
				isWin = true;
		}

		fout << "Case #" << j << ": ";

		if(isWin)
		{
			fout << winSymbol << " won" << std::endl;
		} else if(boardIsFull)
		{
			fout << "Draw" << std::endl;
		} else
		{
			fout << "Game has not completed" << std::endl;
		}

	}
	return 0;
}