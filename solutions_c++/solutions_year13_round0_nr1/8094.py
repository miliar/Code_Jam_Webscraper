#include <iostream>
#include <cstdio>

const int BOARD_SIZE = 4;

using namespace std;

int main()
{
	char board[BOARD_SIZE][BOARD_SIZE];
	int no_games;

	cin >> no_games;
	// Cleans the follow up newline.
	getchar();

	for(int current_game = 0; current_game < no_games; current_game++)
	{
		bool found_winner = false;
		char piece;
		char winner;
		bool has_empty_cells = false;

		// Read the input.
		for (int i = 0; i < BOARD_SIZE; i++)
		{
			for (int j = 0; j < BOARD_SIZE; j++)
			{
				piece = getchar();
				board[i][j] = piece;

				if (piece == '.')
					has_empty_cells = true;
			}

			// Reads the newline.
			piece = getchar();
		}

		// Cleans up the last new line.
		piece = getchar();

		// DEBUG
		// for (int i = 0; i < BOARD_SIZE; i++)
		// {
		// 	for (int j = 0; j < BOARD_SIZE; j++)
		// 		cout << board[i][j];
		// 	cout << "\n";
		// }
			
		// cout << "\n";

		/* There are only 10 winning rows. 4 from the top/bottom,
		 *  4 sideways and 2 in the diagonals.
		 */

		// Top/bottom
		for (int i = 0; i < BOARD_SIZE and !found_winner; i ++)
		{
			char initial = board[0][i];
			
			if (initial == '.')
				continue;

			int j = 1;

			for (; j < BOARD_SIZE; j++)
			{
				if (board[j][i] != initial and board[j][i] != 'T')
					break;
			}

			if (j == BOARD_SIZE)
			{
				found_winner = true;
				winner = initial;
			}
		}

		// Sideways
		for (int i = 0; i < BOARD_SIZE and !found_winner; i ++)
		{
		 	char initial = board[i][0];
			
			if (initial == '.')
				continue;

			int j = 1;

			for (; j < BOARD_SIZE; j++)
			{
				if (board[i][j] != initial and board[i][j] != 'T')
					break;
			}

			if (j == BOARD_SIZE)
			{
				found_winner = true;
				winner = initial;
			}
		}

		// Left/right diagonal.
		if (!found_winner and board[0][0] != '.')
		{
			char initial = board[0][0];

			int j = 1;

			for (; j < BOARD_SIZE; j++)
			{
				if (board[j][j] != initial and board[j][j] != 'T')
					break;
			}

			if (j == BOARD_SIZE)
			{
				found_winner = true;
				winner = initial;
			}
		}

		// Right/left diagonal.
		if (!found_winner and board[0][BOARD_SIZE-1] != '.')
		{
			char initial = board[0][BOARD_SIZE-1];

			int j = BOARD_SIZE-2;

			for (; j >= 0; j--)
			{
				if (board[BOARD_SIZE-j-1][j] != initial and board[BOARD_SIZE-j-1][j] != 'T')
					break;
			}

			if (j == -1)
			{
				found_winner = true;
				winner = initial;
			}
		}

		if (found_winner)
			cout << "Case #" << (current_game + 1) << ": " << winner << " won\n";
		else
		{
			if (has_empty_cells)
				cout << "Case #" << (current_game + 1) << ": Game has not completed\n";
			else
				cout << "Case #" << (current_game + 1) << ": Draw\n";
		}
	}
}