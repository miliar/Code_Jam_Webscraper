#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

char won(char board[4][4])
{
	for (int i = 0; i < 4; i++)
	{
		if ( (board[0][0] == board[1][1] || board[0][0] == 'T') && (board[1][1] == board[2][2] || board[1][1] == 'T')
			&& ( (board[2][2] == board[3][3] || board[2][2] == 'T') || (board[3][3] == board[2][2] || board[3][3] == 'T') ) && board[0][0] != '.' && board[1][1] != '.' )
		{
			if (board[0][0] != 'T')
				return board[0][0];
			else return board[1][1];
		}
		if ( (board[0][3] == board[1][2] || board[0][3] == 'T') && (board[1][2] == board[2][1] || board[1][2] == 'T')
			&& ( (board[2][1] == board[3][0] || board[2][1] == 'T') || (board[3][0] == board[2][1] || board[3][0] == 'T') ) && board[0][3] != '.' && board[1][2] != '.' )
		{
			if (board[0][3] != 'T')
				return board[0][3];
			else return board[1][2];
		}
		if ( (board[i][0] == board[i][1] || board[i][0] == 'T') && (board[i][1] == board[i][2] || board[i][1] == 'T')
			&& ( (board[i][2] == board[i][3] || board[i][2] == 'T') || (board[i][3] == board[i][2] || board[i][3] == 'T') ) && board[i][0] != '.' && board[i][1] != '.' )
			
		{
			if (board[i][0] != 'T')
				return board[i][0];
			else return board[i][1];
		}
		if ( (board[0][i] == board[1][i] || board[0][i] == 'T') && (board[1][i] == board[2][i] || board[1][i] == 'T')
			&& ( (board[2][i] == board[3][i] || board[2][i] == 'T') || (board[3][i] == board[2][i] || board[3][i] == 'T') ) && board[0][i] != '.' && board[1][i] != '.' )
		{
			if (board[0][i] != 'T')
				return board[0][i];
			else return board[1][i];
		}
	}
	
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (board[i][j] == '.')
				return -1;
		}
	}
	
	return 0;
}

int main(int argc, char **argv)
{	
	ifstream infile("A-small-attempt0.in");
	ofstream outfile("small.out");
	
	string in;
	int T;
	char board[4][4];
	
	if (infile.is_open())
	{
		infile >> in;
		T = atoi( in.c_str() );
		
		for (int k = 1; k <= T; k++)
		{
			for (int j = 0; j < 4; j++)
			{
				infile >> in;
				board[j][0] = in[0];
				board[j][1] = in[1];
				board[j][2] = in[2];
				board[j][3] = in[3];
			}
			
			
			char ch = won(board);
			outfile << "Case #" << k << ": ";
			if (ch == 0)
				outfile << "Draw" << endl;
			else if (ch == -1)
				outfile << "Game has not completed" << endl;
			else outfile << ch << " won" << endl;
		}
		
		infile.close();
		outfile.close();
	}
	else cout << "Unable to open file" << endl;
	
	return 0;
}
