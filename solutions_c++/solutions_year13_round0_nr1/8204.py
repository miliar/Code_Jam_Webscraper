#include <iostream>
#include <fstream>
#include <math.h>
#include <string.h>
#include <time.h>

using namespace std;

typedef enum
{
	Unknown, X_won, Draw, Game_has_not_completed, O_won
} STATUS;

int main()
{
	int num;
	ifstream in;
	ofstream out;

	clock_t t = clock();

	in.open("in.txt", ifstream::in);
	if (!in.good())
	{
		cout << "In file bad" << endl;
		return -1;
	}

	out.open("out.txt", ofstream::out);
	if (!out.good())
	{
		cout << "Out file bad" << endl;
		return -1;
	}



	in >> num;

	for (int i = 0; i < num; i++)
	{
		char board[4][4];
		bool still_space = false;
		int tx = -1;
		int ty = -1;
		STATUS status = Unknown;

		//cout << "Case #" << i + 1 << ":" << endl;

		for (int y = 0; y < 4; y++)
		{
			string line;
			in >> line;
			for (int x = 0; x < 4; x++)
			{
				board[x][y] = line.c_str()[x];
				if (board[x][y] == '.')
				{
					still_space = true;
				}
				if (board[x][y] == 'T')
				{
					tx = x;
					ty = y;
				}
			}
		}

		/*for (int x = 0; x < 4; x++)
		{
			for (int y = 0; y < 4; y++)
			{
				cout << board[x][y];
			}
			cout << endl;
		}*/

		//horizontal
		if (tx >= 0)
		{
			board[tx][ty] = 'X';
		}
		for (int x = 0; x < 4; x++)
		{
			if (0 == memcmp(board[x], "XXXX", 4))
			{
				status = X_won;
			}
		}
		if (tx >= 0)
		{
			board[tx][ty] = 'O';
		}
		for (int x = 0; x < 4; x++)
		{
			if (0 == memcmp(board[x], "OOOO", 4))
			{
				status = O_won;
			}
		}

		//vertical
		if (tx >= 0)
		{
			board[tx][ty] = 'X';
		}
		for (int y = 0; y < 4; y++)
		{
			if (board[0][y] == 'X' && board[1][y] == 'X' && board[2][y] == 'X'
					&& board[3][y] == 'X')
			{
				status = X_won;
			}
		}
		if (tx >= 0)
		{
			board[tx][ty] = 'O';
		}
		for (int y = 0; y < 4; y++)
		{
			if (board[0][y] == 'O' && board[1][y] == 'O' && board[2][y] == 'O'
					&& board[3][y] == 'O')
			{
				status = O_won;
			}
		}

		//diagional
		if (board[0][0] == 'O' && board[1][1] == 'O' && board[2][2] == 'O'
				&& board[3][3] == 'O')
		{
			status = O_won;
		}
		if (board[0][0] == 'X' && board[1][1] == 'X' && board[2][2] == 'X'
				&& board[3][3] == 'X')
		{
			status = X_won;
		}

		if (board[3][0] == 'O' && board[2][1] == 'O' && board[1][2] == 'O'
				&& board[0][3] == 'O')
		{
			status = O_won;
		}
		if (board[3][0] == 'X' && board[2][1] == 'X' && board[1][2] == 'X'
				&& board[0][3] == 'X')
		{
			status = X_won;
		}

		if (status == X_won)
		{
			//cout << "Case #" << i + 1 << ": X won";
			out << "Case #" << i + 1 << ": X won";
		}
		else if (status == O_won)
		{
			//cout << "Case #" << i + 1 << ": O won";
			out << "Case #" << i + 1 << ": O won";
		}
		else if (status == Unknown)
		{
			if(still_space)
			{
				//cout << "Case #" << i + 1 << ": Game has not completed";
				out << "Case #" << i + 1 << ": Game has not completed";
			}
			else
			{
				//cout << "Case #" << i + 1 << ": Draw";
				out << "Case #" << i + 1 << ": Draw";
			}
		}

		//cout << endl;
		out << endl;
	}

	in.close();
	out.close();

	cout << "Took " << (clock() - t) << endl;
	return 0;
}
