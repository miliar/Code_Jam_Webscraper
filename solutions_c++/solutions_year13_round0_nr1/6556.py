#include <iostream>
#include <fstream>

using namespace std;

char board[4][4];

int init_board(ifstream &input_file)
{
	int not_draw = 0;

	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			input_file >> board[i][j];

			if (board[i][j] == '.')
			{
				not_draw = 1; 
			}
		}
	}

	return not_draw;
}

void main () 
{
	ifstream input_file ("input_file.txt");
	ofstream output_file ("output_file.txt");
	int kamut, not_draw, x_won, o_won;
	input_file >> kamut;

	for (int current = 1; current < kamut + 1; current++)
	{
		not_draw = init_board(input_file);		
	
		for (int i = 0; i < 4; i++)
		{
			x_won = 1;
			o_won = 1;

			for (int j = 0; j < 4; j++)
			{
				if (board[i][j] == 'X' || board[i][j] == '.')
				{
					o_won = 0;
				}

				if (board[i][j] == 'O' || board[i][j] == '.')
				{
					x_won = 0;
				}
			}

			if (x_won || o_won)
			{
				break;
			}
		}

		if (!x_won && !o_won)
		{
			for (int j = 0; j < 4; j++)
			{
				x_won = 1;
				o_won = 1;

				for (int i = 0; i < 4; i++)
				{
					if (board[i][j] == 'X' || board[i][j] == '.')
					{
						o_won = 0;
					}

					if (board[i][j] == 'O' || board[i][j] == '.')
					{
						x_won = 0;
					}
				}

				if (x_won || o_won)
				{
					break;
				}
			}
		}

		if (!x_won && !o_won)
		{
			x_won = 1;
			o_won = 1;

			for (int i = 0; i < 4; i++)
			{
				if (board[i][i] == 'X' || board[i][i] == '.')
				{
					o_won = 0;
				}

				if (board[i][i] == 'O' || board[i][i] == '.')
				{
					x_won = 0;
				}
			}
		}

		if (!x_won && !o_won)
		{
			x_won = 1;
			o_won = 1;

			for (int i = 0; i < 4; i++)
			{
				if (board[3-i][i] == 'X' || board[3-i][i] == '.')
				{
					o_won = 0;
				}

				if (board[3-i][i] == 'O' || board[3-i][i] == '.')
				{
					x_won = 0;
				}
			}
		}

		output_file << "Case #" << current;

		if (x_won)
		{
			output_file << ": X won" << endl;
		}
		else if (o_won)
		{
			output_file << ": O won" << endl;
		}
		else if (not_draw)
		{
			output_file << ": Game has not completed" << endl;				
		}
		else
		{
			output_file << ": Draw" << endl;
		}
	}

	input_file.close();
	output_file.close();
}