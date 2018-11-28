#include <stdio.h>
#include <iostream>
#include <string>
#include <string.h>
#include <vector>
#include <algorithm>
#include <stdlib.h>
using namespace std;

char check(char* line)
{
	int numX = 0, numO = 0, numT = 0, numE = 0;
	for (int i = 0; i < 4; ++i)
	{
		switch (line[i])
		{
			case 'X':
				numX++;
				break;
			case 'O':
				numO++;
				break;
			case 'T':
				numT++;
				break;
			case '.':
				numE++;
				break;
			default:
				;
		}
	}

	if (numX == 4)
		return 'X';
	else if (numO == 4)
		return 'O';
	else if (numX == 3 && numT == 1)
		return 'X';
	else if (numO == 3 && numT == 1)
		return 'O';
	else if (numE > 0)
		return '.';
	else
		return '*';
}

int main(int argc, char *argv[])
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	cin.get();

	char board[4][4];
	char arr[4];
	int numX, numO, numE;
	for (int t=1; t<=T; ++t)
	{
		numX = numO = numE = 0;
		for (int i = 0; i < 4; ++i)
		{
			string line;
			getline(cin, line);
			for (int j = 0; j < 4; ++j)
				board[i][j] = line[j];
		}
		cin.get();
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
				arr[j] = board[i][j];
			switch (check(arr))
			{
				case 'X':
					numX++;
					break;
				case 'O':
					numO++;
					break;
				case '.':
					numE++;
					break;
				default:
					;
			}
		}
		for (int j = 0; j < 4; ++j)
		{
			for (int i = 0; i < 4; ++i)
				arr[i] = board[i][j];
			switch (check(arr))
			{
				case 'X':
					numX++;
					break;
				case 'O':
					numO++;
					break;
				case '.':
					numE++;
					break;
				default:
					;
			}
		}
		for (int i = 0; i < 4; ++i)
			arr[i] = board[i][i];
		switch (check(arr))
		{
			case 'X':
				numX++;
				break;
			case 'O':
				numO++;
				break;
			case '.':
				numE++;
				break;
			default:
				;
		}
		for (int i = 0; i < 4; ++i)
			arr[i] = board[i][3-i];
		switch (check(arr))
		{
			case 'X':
				numX++;
				break;
			case 'O':
				numO++;
				break;
			case '.':
				numE++;
				break;
			default:
				;
		}
		cout << "Case #" << t << ": ";
		if (numX > 0)
			cout << "X won";
		else if (numO > 0)
			cout << "O won";
		else if (numE > 0)
			cout << "Game has not completed";
		else 
			cout << "Draw";
		cout << endl;
	}


	return 0;
}
