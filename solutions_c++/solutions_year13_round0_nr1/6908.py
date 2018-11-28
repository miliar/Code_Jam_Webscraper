#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

bool IsAnyCrossWin(char** board, char& player)
{
	bool won = true;
	player = (board[0][0] == 'T') ? board[1][1] : board[0][0];
	if (player == '.')
		won = false;
		
	for (int i = 0; i < 4; ++i)
		if (board[i][i] != 'T' && board[i][i] != player)
			won = false;
	
	if (won) return true;
	
	won = true;
	player = (board[0][3] == 'T') ? board[1][2] : board[0][3];
	if (player == '.')
		won = false;
		
	for (int i = 0; i < 4; ++i)
		if (board[i][3-i] != 'T' && board[i][3-i] != player)
			won = false;
	
	return won;
}

bool IsAnyHorizontalWin(char** board, char& player)
{
	for (int r = 0; r < 4; ++r)
	{
		bool won = true;
		player = (board[r][0] == 'T') ? board[r][1] : board[r][0];
		if (player == '.')
			continue;
		for (int c = 0; c < 4; ++c)
			if (board[r][c] != 'T' && board[r][c] != player)
				won = false;
		if (won)
			return true;
	}
	return false;
}

bool IsAnyVerticalWin(char** board, char& player)
{
	for (int c = 0; c < 4; ++c)
	{
		bool won = true;
		player = (board[0][c] == 'T') ? board[1][c] : board[0][c];
		if (player == '.')
			continue;
		for (int r = 0; r < 4; ++r)
			if (board[r][c] != 'T' && board[r][c] != player)
				won = false;
		if (won)
			return true;
	}
	return false;
}

bool IsAnyBlank(char** board)
{
	for (int r = 0; r < 4; ++r)
		for (int c = 0; c < 4; ++c)
			if (board[r][c] == '.')
				return true;
	return false;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		char* board[4];
		for (int i = 0; i < 4; ++i)
			board[i] = new char[4];
		
		for (int r = 0; r < 4; ++r)
			for (int c = 0; c < 4; ++c)
				cin >> board[r][c];	
		char player;
		
		cout << "Case #" << (t+1) << ": ";
		
		if (IsAnyCrossWin(board,player) || IsAnyHorizontalWin(board,player) || IsAnyVerticalWin(board,player))
			cout << player << " won";
		else if (IsAnyBlank(board))
			cout << "Game has not completed";
		else
			cout << "Draw";
		
		for (int i = 0; i < 4; ++i)
			delete[] board[i];
		cout << endl;
	}
	return 0;
}
