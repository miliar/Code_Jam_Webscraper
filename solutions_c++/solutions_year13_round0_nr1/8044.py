// tictactoe.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <fstream>
#include <iostream>

char hasWon(char board[][4])
{
	int r = 0, c = 0;

	//Check rows
	for(r = 0; r < 4; r++)
	{
		if(board[r][0] != '.')
		{
			if(board[r][0] != 'T')
			{
				for(c = 1; c < 4; c++)
				{
					if(board[r][c] != 'T')
					{
						if(board[r][c] != board[r][0])
						{
							break;
						}
					}
				}
				if(c == 4)
				{
					return board[r][0];
				}
			}
			else
			{
				for(c = 2; c < 4; c++)
				{
					if(board[r][c] != board[r][c-1] || board[r][c] == '.' || board[r][c-1] == '.')
					{
						break;
					}
				}
				if(c == 4)
				{
					return board[r][1];
				}
			}
		}
	}

	//Check columns
	for(c = 0; c < 4; c++)
	{
		if(board[0][c] != '.')
		{
			if(board[0][c] != 'T')
			{
				for(r = 1; r < 4; r++)
				{
					if(board[r][c] != 'T')
					{
						if(board[r][c] != board[0][c])
							break;
					}
				}
				if(r == 4)
					return board[0][c];
			}
			else
			{
				for(r = 2; r < 4; r++)
				{
					if(board[r][c] != board[r-1][c] || board[r][c] == '.' || board[r-1][c] == '.')
						break;
				}
				if(r == 4)
					return board[1][c];
			}
		}
	}

	//Check diagonal
	if(board[0][0] != '.')
	{
		if(board[0][0] != 'T')
		{
			for(r = 1; r < 4; r++)
			{
				if(board[r][r] != 'T')
				{
					if(board[r][r] != board[0][0])
						break;
				}
			}
			if(r == 4)
				return board[0][0];
		}
		else
		{
			for(r = 2; r < 4; r++)
			{
				if(board[r][r] != board[r-1][r-1] || board[r][r] == '.' || board[r-1][r-1] == '.')
					break;
			}
			if(r == 4)
				return board[1][1];
		}
	}

	//Check Reverse Diagonal
	if(board[3][0] != '.')
	{
		if(board[3][0] != 'T')
		{
			for(r = 1; r < 4; r++)
			{
				if(board[4-r-1][r] != 'T')
				{
					if(board[4-r-1][r] != board[3][0])
						break;
				}
			}
			if(r == 4)
				return board[3][0];
		}
		else
		{
			for(r = 2; r < 4; r++)
			{
				if(board[4-r-1][r] != board[4-r][r-1] || board[4-r-1][r] == '.' || board[4-r][r-1] == '.')
					break;
			}
			if(r == 4)
				return board[2][1];
		}
	}

	int draw_flag = 1;
	//Check if Game is draw or if game is not completed
	for(r = 0; r < 4; r++)
	{
		for(c = 0; c < 4; c++)
		{
			if(board[r][c] == '.')
			{
				draw_flag = 0;
				break;
			}
		}
		if(draw_flag == 0)
		{
			break;
		}
	}

	if(draw_flag == 0)
	{
		return 'N';
	}
	else if(draw_flag == 1)
	{
		return 'D';
	}
}


int main()
{
	int no_of_test_cases = 0, row = 0;
	FILE* file_input;
	FILE* file_output;
	file_input = fopen("A-small-attempt6.in", "r");
	char line[6] = "";
	char board[4][4];
	char result;
	fgets(line,	6, file_input);
	sscanf(line, "%d", &no_of_test_cases);
	for(int count = 1; count <= no_of_test_cases; count++)
	{
		while(fgets(line, 6, file_input) != NULL)
		{
			board[row][0] = line[0];
			board[row][1] = line[1];
			board[row][2] = line[2];
			board[row][3] = line[3];
			row++;
			if(row == 4)
			{
				break;
			}
		}
		result = hasWon(board);
		file_output = fopen("A-small-attempt6.out", "a");
		if(result == 'X')
		{
			fprintf(file_output, "Case #%d: %c won", count, result);
		} else if(result == 'O')
		{
			fprintf(file_output, "Case #%d: %c won", count, result);
		} else if(result == 'D')
		{
			fprintf(file_output, "Case #%d: Draw", count);
		} else if(result == 'N')
		{
			fprintf(file_output, "Case #%d: Game has not completed", count);
		}
		row = 0;
		if(count == no_of_test_cases)
		{
			break;
		}
		else
		{
			fprintf(file_output, "\n");
			fgets(line, 6, file_input);
		}
	}
	return 0;
}

