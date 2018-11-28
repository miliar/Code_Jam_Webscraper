#include <iostream>

/*
 * Google Code Jam 2013 - Problem A: Tic-Tac-Toe-Tomek
 *
 * Submitter: dorphion (Jonas Weber)
 *
 */

int cell(int row, int col)
{
	return row * 4 + col;
}

bool is_field_of_player_or_tomek(char player, int row, int col, char field[16])
{
	return (field[cell(row,col)] == player) || 
			(field[cell(row,col)] == 'T');
}

bool has_player_won(char field[16], char player)
{
	// rows
	for (int row = 0; row < 4; row++)
	{
		if (is_field_of_player_or_tomek(player, row, 0, field) &&
			is_field_of_player_or_tomek(player, row, 1, field) &&
			is_field_of_player_or_tomek(player, row, 2, field) &&
			is_field_of_player_or_tomek(player, row, 3, field))
		return true;
	}
	
	// columns
	for (int col = 0; col < 4; col++)
	{
		if (is_field_of_player_or_tomek(player, 0, col, field) &&
			is_field_of_player_or_tomek(player, 1, col, field) &&
			is_field_of_player_or_tomek(player, 2, col, field) &&
			is_field_of_player_or_tomek(player, 3, col, field))
		return true;
	}

	// diagonals
	if (is_field_of_player_or_tomek(player, 0, 0, field) &&
		is_field_of_player_or_tomek(player, 1, 1, field) &&
		is_field_of_player_or_tomek(player, 2, 2, field) &&
		is_field_of_player_or_tomek(player, 3, 3, field))
	return true;
	if (is_field_of_player_or_tomek(player, 0, 3, field) &&
		is_field_of_player_or_tomek(player, 1, 2, field) &&
		is_field_of_player_or_tomek(player, 2, 1, field) &&
		is_field_of_player_or_tomek(player, 3, 0, field))
	return true;


	return false;
	
}

bool field_is_full(char field[16])
{
	for (int i=0; i < 16; i++)
	{
		if (field[i] == '.')
			return false;
	}
	return true;
}

void announce_winner(int testcase, char player)
{
	std::cout << "Case #" << testcase+1 << ": " << player << " won" << std::endl;
}

void announce_not_completed(int testcase)
{
	std::cout << "Case #" << testcase+1 << ": Game has not completed" << std::endl;
}

void announce_draw(int testcase)
{
	std::cout << "Case #" << testcase+1 << ": Draw" << std::endl;
}

int main(int argc, char** argv)
{
	int testcasecount;
	std::cin >> testcasecount;

	for (int i=0; i < testcasecount; i++)
	{
		char field[16];
		for (int x=0; x < 16; x++)
			std::cin >> field[x];

		if (has_player_won(field, 'X'))
			announce_winner(i, 'X');
		else if (has_player_won(field, 'O'))
			announce_winner(i, 'O');
		else if (field_is_full(field))
			announce_draw(i);
		else
			announce_not_completed(i);


	}

}
