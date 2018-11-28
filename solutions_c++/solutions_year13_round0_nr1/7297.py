#include <iostream>
#include <cstdio>

#define ROW 1
#define COL 2
#define DIAG 3
#define SUCCESS 1
#define FAILURE 0
#define writeResult(i,x) printf("Case #%d: %s\n", i, x)

using namespace std;

char board[5][5];

int check(int i, char p, int choice) // row or col number, character to be checked, choose between row and column
{
	int c;
	if (choice == ROW)
	{
		c = 0;
		for ( int j = 0; j < 4; ++j )
		{
			if ( board[i][j] == 'T' || board[i][j] == p )
			{
				++c;
			}
		}
		if ( c == 4 )
			return SUCCESS;
		return FAILURE;
	}
	if (choice == COL)
	{
		c = 0;
		for ( int j = 0; j < 4; ++j )
		{
			if ( board[j][i] == 'T' || board[j][i] == p )
			{
				++c;
			}
		}
		if ( c == 4 )
			return SUCCESS;
		return FAILURE;
	}
	if (choice == DIAG)
	{
		c = 0;
		for ( int j = 0; j < 4; ++j )
		{
			if ( board[j][j] == 'T' || board[j][j] == p )
			{
				++c;
			}
		}
		if ( c == 4 )
			return SUCCESS;

		c = 0;
		for ( int j = 0; j < 4; ++j )
		{
			if ( board[j][4 - j -1] == 'T' || board[j][4 - j - 1] == p )
			{
				++c;
			}
		}
		if ( c == 4 )
			return SUCCESS;
		return FAILURE;
	}
}

void readBoard()
{
	int i;
	for ( i = 0; i < 4; ++i )
	{
		cin.getline(board[i], 5);
	}
	cin.getline(board[i], 5);
}

int isIncomplete()
{
	for ( int i = 0; i < 4; ++i )
	{
		for ( int j = 0; j < 4; ++j )
		{
			if ( board[i][j] == '.' )
				return SUCCESS;
		}
	}
	return FAILURE;
}

int main()
{
	int t, i, j;
	cin >> t;
	cin.getline(board[0],5);

	for ( i = 1; i <= t; ++i )
	{
		readBoard();

		if (check ( 0 , 'X', DIAG ) )
		{
			writeResult(i,"X won");
			continue;
		}
		
		if (check ( 0 , 'O', DIAG ) )
		{
			writeResult(i,"O won");
			continue;
		}

		for ( j = 0; j < 4; ++j )
		{
			if ( check ( j, 'X', ROW ) )
			{
				writeResult(i,"X won");
				break;
			}
			if ( check ( j, 'X', COL ) )
			{
				writeResult(i,"X won");
				break;
			}
			if ( check ( j, 'O', ROW ) )
			{
				writeResult(i,"O won");
				break;
			}
			if ( check ( j, 'O', COL ) )
			{
				writeResult(i,"O won");
				break;
			}
		}

		if ( j == 4 )
		{
			if ( isIncomplete() )
			{
				writeResult(i, "Game has not completed");
			}
			else
			{
				writeResult(i, "Draw");
			}
		}
	}
	return 0;
}
