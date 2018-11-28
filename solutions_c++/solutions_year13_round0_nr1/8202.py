#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;
int main(int argc, char const *argv[])
{
	int num;
	cin >> num;

	for (int i = 0; i < num; ++i)
	{
		// For each test case
		char ** board = (char**)malloc(4*sizeof(char*));
		for (int j = 0; j < 4; ++j)
		{
			board[j] = (char*)malloc(4);
			cin >> board[j];
		}
		int win = 0;
		int has_dot = 0;
		// For horizontal and vertical
		for (int j = 0; j < 4; ++j)
		{
			int has_other_piece_h = 0;
			char first_char_h = board[j][0];

			int has_other_piece_v = 0;
			char first_char_v = board[0][j];

			if (first_char_h == '.')
			{
				has_dot = 1;
				has_other_piece_h = 1;
			}

			if (first_char_v == '.')
			{
				has_dot = 1;
				has_other_piece_v = 1;
			}

			for (int k = 0; k < 4; ++k)
			{
				// For each char
				if ((board[j][k] != 'T')&&(!(first_char_h == board[j][k])))
				{
					// If has other piece, break
					has_other_piece_h = 1;
				}
				if (board[j][k] == '.')
				{
					has_dot = 1;
				}
			}
			for (int k = 0; k < 4; ++k)
			{
				// For each char
				if ((board[k][j] != 'T')&&(!(first_char_v == board[k][j]))){
					has_other_piece_v = 1;
				}
				if (board[j][k] == '.')
				{
					has_dot = 1;
				}
			}



			if (!has_other_piece_v)
			{
				win = 1;
				printf("Case #%d: %c won\n", i+1, first_char_v);
				break;
			}
			if (!has_other_piece_h)
			{
				win = 1;
				printf("Case #%d: %c won\n", i+1, first_char_h);
				break;
			}
		}
		// For diagonals


		char first_char_d_1 = board[0][0];
		int has_other_piece_d_1 = 0;
		for (int k = 0; k < 4; ++k)
		{
			if ((board[k][k] != 'T')&&(!(first_char_d_1 == board[k][k]))){
				has_other_piece_d_1 = 1;
			}
		}

		char first_char_d_2 = board[0][3];
		int has_other_piece_d_2 = 0;
		for (int k = 0; k < 4; ++k)
		{
			if ((board[k][3-k] != 'T')&&(!(first_char_d_2 == board[k][3-k]))){
				has_other_piece_d_2 = 1;
			}
		}
		if (first_char_d_1 == '.')
		{
			has_other_piece_d_1 = 1;
		}

		if (first_char_d_2 == '.')
		{
			has_other_piece_d_2 = 1;
		}
		if (!has_other_piece_d_2)
		{
			win = 1;
			printf("Case #%d: %c won\n", i+1, first_char_d_2);
		}
		if (!has_other_piece_d_1)
		{
			win = 1;
			printf("Case #%d: %c won\n", i+1, first_char_d_1);
		}
		if (has_dot && !win) {
			printf("Case #%d: Game has not completed\n", i+1);
		}else if (!win)
			printf("Case #%d: Draw\n", i+1);

	}
	/* code */
	return 0;
}