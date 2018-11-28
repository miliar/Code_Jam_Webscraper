#include <algorithm>
#include <cstring>
#include <iostream>
#include <stdio.h>

using namespace std;

char T ='T';
bool hasDots = false;
char **loadGame()
{
	char **game;
	game = (char **)malloc(sizeof (char *) * 4);

	for (int i = 0; i < 4; i++)
		game[i] = (char *)malloc(sizeof (char));


	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			cin >> game[i][j];
		}
	}

	return game;
}

bool hasColumnWinner(char **tictac, int line, char *out){
	*out = tictac[line][0] == T ? tictac[line][1] : tictac[line][0];

	if (*out =='.')
		return false;

	for (int i = 0; i < 4; i++)
	{
		if (tictac[line][i] =='.')
		{
			hasDots = true;
			return false;
		}
		if (tictac[line][i] != *out && tictac[line][i] != T)
		{
			return false;
		}
	}

	return true;
}

bool hasLineWinner(char **tictac, int column, char *out){
	*out = tictac[0][column] == T ? tictac[1][column] : tictac[0][column];

	if (*out =='.')
		return false;

	for (int i = 0; i < 4; i++)
	{
		if (tictac[i][column] =='.')
		{
			hasDots = true;
			return false;
		}
		if (tictac[i][column] != *out && tictac[i][column] != T)
		{
			return false;
		}
	}
	return true;
}

bool hasReverseDiagonalWinner(char **tictac, char *out){
	*out = tictac[0][3] == T ? tictac[1][2] : tictac[0][3];

	if (*out =='.')
		return false;

	for (int i = 0; i < 4; i++)
	{
		if (tictac[i][3-i] =='.')
		{
			hasDots = true;
			return false;
		}
		if (tictac[i][3-i] != *out && tictac[i][3-i] != T)
		{
			return false;
		}
	}
	return true;
}

bool hasDiagonalWinner(char **tictac, char *out){
	*out = tictac[0][0] == T ? tictac[1][1] : tictac[0][0];

	for (int i = 0; i < 4; i++)
	{
		if (tictac[i][i] =='.')
		{
			hasDots = true;
			return false;
		}

		if (tictac[i][i] != *out && tictac[i][i] != T)
		{
			return false;
		}
	}
	return true;
}

bool hasWinner(char **tictac)
{
	char current;

	for (int i = 0; i < 4; i++)
	{
		if (hasColumnWinner(tictac,i,&current) || hasLineWinner(tictac,i,&current))
		{
			cout << current << " won\n";
			return true;
		}
	}

	if (hasDiagonalWinner(tictac,&current) || hasReverseDiagonalWinner(tictac,&current))
	{
		cout << current << " won\n";
		return true;
	}
	return false;
}

int main (int argc, char *argv[])
{
	int T = 0;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		cin;
		hasDots = false;

		cout << "Case #" << i+1 << ": ";

		if (hasWinner(loadGame()))
		{
			continue;
		}

		if (hasDots)
			cout << "Game has not completed\n";
		else
			cout << "Draw\n";
	}
}
