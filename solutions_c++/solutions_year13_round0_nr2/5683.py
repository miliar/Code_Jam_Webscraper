#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool checkColumn(int board[100][100], int i, int j, int r, int c)
{
	for(int t = 0; t < i; t++)
	{
		if(board[t][j] > board [i][j])
			return false;
	}

	for(int t = i + 1; t < r; t++)
	{
		if(board[t][j] > board [i][j])
			return false;
	}
	return true;
}

bool checkRow(int board[100][100], int i, int j, int r, int c)
{
	for(int t = 0; t < j; t++)
	{
		if(board[i][t] > board [i][j])
			return false;
	}

	for(int t = j + 1; t < c; t++)
	{
		if(board[i][t] > board [i][j])
			return false;
	}
	return true;
}

bool checkBoard(int board[100][100], int r, int c)
{
	if(r == 0 || c == 0)
		return true;
	for(int i = 0; i < r; i++)
	{
		for(int j = 0; j < c; j++)
		{
			if(!checkColumn(board, i, j, r, c) && !checkRow(board, i, j, r, c))
				return false;
		}
	}
	return true;
}

void testLawn(int board[100][100], int r, int c)
{
	if(!checkBoard(board, r, c))
	{
		cout << "NO";
		return;
	}
	cout << "YES";
}

int main(int argc, char *argv[])
{
	ifstream input;
	input.open(argv[1]);
	if(!input.is_open())
	{
		cout << "Error Opening" << endl;
		return 0;
	}
	
	char add;
	int total, r, c;
	input >> total;
	int board[100][100];
	for(int count = 0; count < total; count++)
	{
		input >> r;
		input >> c;
		for(int i = 0; i < r; i++)
		{
			for(int j = 0; j < c; j++)
			{
				input >> add;
				board[i][j] = add;
			}
		}
		cout << "Case #" << count + 1 << ": ";
		testLawn(board, r, c);
		cout << endl;
	}	
}