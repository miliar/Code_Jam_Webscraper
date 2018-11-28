#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <fstream>

using namespace std;

int main ()
{
	int T;
	ifstream infile;
	ofstream outfile;
	infile.open("A-small-attempt1.in");
	outfile.open("Result.txt");
	infile >> T;
	for (int count = 0; count < T; count++)
	{
		int hasCompleted = 1, Winner = 0;
		outfile << "Case #" << count + 1 << ": ";
		char board[4][4];
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				infile >> board[i][j];
				if (board[i][j] == '.')
				{
					hasCompleted = 0;
				}
			}
		}
		for (int j = 0; j < 4 ; j++)
		{
		if ((board[0][j] == 'X' || board[0][j] == 'T') && (board[1][j] == 'X' || board[1][j] == 'T') && (board[2][j] == 'X' || board[2][j] == 'T') && (board[3][j] == 'X' || board[3][j] == 'T'))
		{
			Winner = 1;
			outfile << "X won";
			goto Verdict;
		}
		if ((board[0][j] == 'O' || board[0][j] == 'T') && (board[1][j] == 'O' || board[1][j] == 'T') && (board[2][j] == 'O' || board[2][j] == 'T') && (board[3][j] == 'O' || board[3][j] == 'T'))
		{
			Winner = 1;
			outfile << "O won";
			goto Verdict;
		}
		}
		for (int i = 0; i < 4; i++)
		{
		if ((board[i][0] == 'X' || board[i][0] == 'T') && (board[i][1] == 'X' || board[i][1] == 'T') && (board[i][2] == 'X' || board[i][2] == 'T') && (board[i][3] == 'X' || board[i][3] == 'T'))
		{
			Winner = 1;
			outfile << "X won";
			goto Verdict;
		}
		if ((board[i][0] == 'O' || board[i][0] == 'T') && (board[i][1] == 'O' || board[i][1] == 'T') && (board[i][2] == 'O' || board[i][2] == 'T') && (board[i][3] == 'O' || board[i][3] == 'T'))
		{
			Winner = 1;
			outfile << "O won";
			goto Verdict;
		}
		}
		if ((board[0][0] == 'X' || board[0][0] == 'T') && (board[1][1] == 'X' || board[1][1] == 'T') && (board[2][2] == 'X' || board[2][2] == 'T') && (board[3][3] == 'X' || board[3][3] == 'T'))
		{
			Winner = 1;
			outfile << "X won";
			goto Verdict;
		}
		if ((board[0][0] == 'O' || board[0][0] == 'T') && (board[1][1] == 'O' || board[1][1] == 'T') && (board[2][2] == 'O' || board[2][2] == 'T') && (board[3][3] == 'O' || board[3][3] == 'T'))
		{
			Winner = 1;
			outfile << "O won";
			goto Verdict;
		}
Verdict:
		if (Winner == 0)
		{
			if (hasCompleted == 1)
			{
				outfile << "Draw";
			}
			else if (hasCompleted == 0)
			{
				outfile << "Game has not completed";
			}
		}
		outfile << '\n';
}
	infile.close();
	outfile.close();
}
