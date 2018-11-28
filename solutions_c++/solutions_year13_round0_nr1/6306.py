#include <iostream>
#include <fstream>

using namespace std;

bool checkRows(char player, char board[][4])
{
	for(int i = 0; i < 4; i++)
	{
		
		for(int j = 0; j < 4; j++)
		{
			if(player != board[i][j] && 'T' != board[i][j])
				break;
			if(j == 3)
				return true;
		}
	}
	return false;
}

bool checkCols(char player, char board[][4])
{
	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			if(player != board[j][i] && 'T' != board[j][i])
				break;
			if(j == 3)
				return true;
		}
	}
	return false;
}

bool checkDiags(char player, char board[][4])
{
	for(int i = 0; i < 4; i++)
	{
		if(board[i][i] != player && board[i][i] != 'T')
			break;
		if(i == 3)
			return true;
	}
	for(int i = 0; i < 4; i++)
	{
		if(board[i][3-i] != player && board[i][3-i] != 'T')
			break;
		if(i == 3)
			return true;
	}
	return false;
}

bool isWinner(char player, char board[][4])
{
	if(checkRows(player, board) || checkCols(player, board) || checkDiags(player, board))
		return true;
	return false;
}

bool isFull(char board[][4])
{
	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
			if(board[i][j] == '.')
				return false;
	}
	return true;
}

int main()
{
	ifstream inFile;
	ofstream outFile;
	inFile.open("input.txt", ios::in);
	outFile.open("output.txt", ios::out);
	int numTests = 0;
	inFile >> numTests;
	for(int i = 0; i < numTests; i++)
	{
		char gameboard[4][4];
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				inFile >> gameboard[i][j];
			}
		}
	
		if(isWinner('X', gameboard))
			outFile << "Case #" << i+1 << ": " << "X won" << endl;
		else if(isWinner('O', gameboard))
			outFile << "Case #" << i+1 << ": " << "O won" << endl;
		else if(isFull(gameboard))
			outFile << "Case #" << i+1 << ": " << "Draw" << endl;
		else
			outFile << "Case #" << i+1 << ": " << "Game has not completed" << endl;
	}
	inFile.close();
	outFile.close();
	return 0;
}