#include <iostream>

using namespace std;

char board[4][4];
int testCases;
int victor[1000];

bool IsTaken(char letter, int x, int y)
{
	return (board[x][y] == letter || board[x][y] == 'T');
}

bool FindCols(char letter)
{
	for (int y = 0; y < 4; y++)
	{
		if (IsTaken(letter, 0, y) && IsTaken(letter, 1, y) && IsTaken(letter, 2, y) && IsTaken(letter, 3, y))
		{
			return true;
		}
	}

	return false;
}

bool FindRows(char letter)
{
	for (int x = 0; x < 4; x++)
	{
		if (IsTaken(letter, x, 0) && IsTaken(letter, x, 1) && IsTaken(letter, x, 2) && IsTaken(letter, x, 3))
		{
			return true;
		}
	}

	return false;
}

bool FindDiagonals(char letter)
{
	return	(IsTaken(letter, 0, 0) && IsTaken(letter, 1, 1) && IsTaken(letter, 2, 2) && IsTaken(letter, 3, 3) 
			 || IsTaken(letter, 3, 0) && IsTaken(letter, 2, 1) && IsTaken(letter, 1, 2) && IsTaken(letter, 0, 3));
}

bool Won(char letter)
{
	return (FindCols(letter) || FindRows(letter) || FindDiagonals(letter));
}


bool EmptyBoard()
{
	for (int x = 0; x < 4; x++)
	{
		for (int y = 0; y < 4; y++)
		{
			if (board[x][y] == '.')
			{
				return true;
			}
		}
	}

	return false;
}

int main()
{
	cin >> testCases;

	for (int i = 0; i < testCases; i++)
	{
		for (int y = 0; y < 4; y++)
		{
			for (int x = 0; x < 4; x++)
			{
				char letter;

				cin >> letter;

				board[x][y] = letter;
			}
		}

		if (Won('X'))
		{
			victor[i] = 0;
		}
		else if (Won('O'))
		{
			victor[i] = 1;
		}
		else if (EmptyBoard())
		{
			victor[i] = 2;
		}
		else
		{
			victor[i] = 3;
		}
	}

	for (int i = 0; i < testCases; i++)
	{
		cout << "Case #" << (i+1) << ": ";

		switch(victor[i])
		{
		case 0:
			cout << "X won";
			break;

		case 1:
			cout << "O won";
			break;

		case 2:
			cout << "Game has not completed";
			break;

		case 3:
			cout << "Draw";
		}

		cout << endl;
	}

	return 0;
}