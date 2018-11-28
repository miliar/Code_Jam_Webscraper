// code_jam_1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

char file_input[] = "input_large.in";
char file_output[] = "output.ou";

FILE *fin, *fout;

int testcase_number;

char board[4][4];

bool end_state;
bool not_end;	
char winner;

int print_result(int case_num);

bool equal3(char a, char b, char c)
{
	if ( (a == b) && (b == c) )
	{
		return true;
	}
	else
	{

		return false;
	}
}
bool equal4(char a, char b, char c, char d )
{
	if ( (a == b) && (b == c) && (b == d) )
	{
		return true;
	}
	else
	{

		return false;
	}
}
int get_input()
{
	int i = 0, j = 0, ii = 0;

	int temp;

	fin = fopen(file_input, "r");
	fout = fopen(file_output, "w");
	
	if ( (fin == NULL) || (fout == NULL) )
	{
		printf("ERROR in open file!");
		return 0;
	}

	fscanf(fin, "%d \n", &testcase_number);
	
	for (ii = 0; ii < testcase_number; ii++)
	{
		end_state = false;
		not_end = false;	// xem con cho trong nao khong
		winner = 'D';
		
		for (i = 0; i < 4; i++)
		{
			
			for (j = 0; j < 4; j++)
			{
				fscanf(fin, "%c", &board[i][j]);
				
				if (end_state)
				{
					continue;
				}

				if ( (i == 3) && (j == 3) )
				{
					if ( (board[i-1][j-1] == '.') || (board[i][j] == '.') || (board[i-2][j-2] == '.') || (board[i-3][j-3] == '.') )
					{

					}
					else
					{
						if (equal4(board[i][j], board[i-1][j-1], board[i-2][j-2], board[i-3][j-3]))
						{
							end_state = true;

							if (board[i][j] == 'X')
							{
								winner = 'X';
							}
							else 
							{
								winner = 'O';
							}
						}
						else if ( (board[i][j] == 'T') && equal3(board[i-1][j-1], board[i-2][j-2], board[i-3][j-3]) ) 
						{
							end_state = true;
							if (board[i-1][j-1] == 'X')
							{
								winner = 'X';
							}
							else 
							{
								winner = 'O';
							}
						}
						else if ( (board[i-1][j-1] == 'T') && equal3(board[i][j], board[i-2][j-2], board[i-3][j-3]) )
						{
							end_state = true;
							if (board[i][j] == 'X')
							{
								winner = 'X';
							}
							else 
							{
								winner = 'O';
							}
						}
						else if ((board[i-2][j-2] == 'T') && equal3(board[i-1][j-1], board[i][j], board[i-3][j-3]) )
						{
							end_state = true;
							if (board[i][j] == 'X')
							{
								winner = 'X';
							}
							else 
							{
								winner = 'O';
							}
						}
						else if ( (board[i-3][j-3] == 'T') && equal3(board[i-1][j-1], board[i-2][j-2], board[i][j]) ) 
						{
							end_state = true;
							if (board[i][j] == 'X')
							{
								winner = 'X';
							}
							else 
							{
								winner = 'O';
							}
						}
					}
				}

				if ((i == 3) && (j == 0))
				{
					if ( (board[i-1][j+1] == '.') || (board[i][j] == '.') || (board[i-2][j+2] == '.') || (board[i-3][j+3] == '.') )
					{

					}
					else
					{
						if (equal4(board[i][j], board[i-1][j+1], board[i-2][j+2], board[i-3][j+3]))
						{
							end_state = true;

							if (board[i][j] == 'X')
							{
								winner = 'X';
							}
							else 
							{
								winner = 'O';
							}
						}
						else if ( (board[i][j] == 'T') && equal3(board[i-1][j+1], board[i-2][j+2], board[i-3][j+3]) ) 
						{
							end_state = true;
							if (board[i-1][j+1] == 'X')
							{
								winner = 'X';
							}
							else 
							{
								winner = 'O';
							}
						}
						else if ( (board[i-1][j+1] == 'T') && equal3(board[i][j], board[i-2][j+2], board[i-3][j+3]) )
						{
							end_state = true;
							if (board[i][j] == 'X')
							{
								winner = 'X';
							}
							else 
							{
								winner = 'O';
							}
						}
						else if ((board[i-2][j+2] == 'T') && equal3(board[i-1][j+1], board[i][j], board[i-3][j+3]) )
						{
							end_state = true;
							if (board[i][j] == 'X')
							{
								winner = 'X';
							}
							else 
							{
								winner = 'O';
							}
						}
						else if ( (board[i-3][j+3] == 'T') && equal3(board[i-1][j+1], board[i-2][j+2], board[i][j]) ) 
						{
							end_state = true;
							if (board[i][j] == 'X')
							{
								winner = 'X';
							}
							else 
							{
								winner = 'O';
							}
						}
					}
				}
				

				if (j == 3)
				{
					if (board[i][j] == 'T')
					{
						if ( (board[i][j-1] != '.') && (board[i][j-1] == board[i][j-2]) && (board[i][j-2] == board[i][j-3]))
						{
							end_state = true;

							if (board[i][j-1] == 'X')
							{
								winner = 'X';
							}
							else 
							{
								winner = 'O';
							}
						}
					}
					else if (board[i][j-1] == 'T')
					{
						if ( (board[i][j] != '.') && (board[i][j-2] == board[i][j-3]) && (board[i][j] == board[i][j-3]))
						{
							end_state = true;

							if (board[i][j] == 'X')
							{
								winner = 'X';
							}
							else 
							{
								winner = 'O';
							}
						}

					}
					else if (board[i][j-2] == 'T')
					{
						if ( (board[i][j] != '.') && (board[i][j] == board[i][j-1]) && (board[i][j-1] == board[i][j-3]))
						{
							end_state = true;

							if (board[i][j] == 'X')
							{
								winner = 'X';
							}
							else 
							{
								winner = 'O';
							}
						}
					}
					else if (board[i][j-3] == 'T')
					{
						if ( (board[i][j] != '.') && (board[i][j-1] == board[i][j-2]) && (board[i][j-2] == board[i][j]))
						{
							end_state = true;

							if (board[i][j] == 'X')
							{
								winner = 'X';
							}
							else 
							{
								winner = 'O';
							}
						}
					}
					else
					{
						if ( (board[i][j] != '.') && (board[i][j-1] == board[i][j-2]) && (board[i][j-2] == board[i][j]) && (board[i][j-3] == board[i][j-2]))
						{
							end_state = true;

							if (board[i][j] == 'X')
							{
								winner = 'X';
							}
							else 
							{
								winner = 'O';
							}
						}
					}
				}

				if (i == 3)
				{
					if (board[i][j] == 'T')
					{
						if ( (board[i-1][j] != '.') && (board[i-1][j] == board[i-2][j]) && (board[i-2][j] == board[i-3][j]))
						{
							end_state = true;

							if (board[i-1][j] == 'X')
							{
								winner = 'X';
							}
							else 
							{
								winner = 'O';
							}
						}
					}
					else if (board[i-1][j] == 'T')
					{
						if ( (board[i][j] != '.') && (board[i-2][j] == board[i-3][j]) && (board[i][j] == board[i-3][j]))
						{
							end_state = true;

							if (board[i][j] == 'X')
							{
								winner = 'X';
							}
							else 
							{
								winner = 'O';
							}
						}

					}
					else if (board[i-2][j] == 'T')
					{
						if ( (board[i][j] != '.') && (board[i][j] == board[i-1][j]) && (board[i-1][j] == board[i-3][j]))
						{
							end_state = true;

							if (board[i][j] == 'X')
							{
								winner = 'X';
							}
							else 
							{
								winner = 'O';
							}
						}
					}
					else if (board[i-3][j] == 'T')
					{
						if ( (board[i][j] != '.') && (board[i-1][j] == board[i-2][j]) && (board[i-2][j] == board[i][j]))
						{
							end_state = true;

							if (board[i][j] == 'X')
							{
								winner = 'X';
							}
							else 
							{
								winner = 'O';
							}
						}
					}
					else
					{
						if ( (board[i][j] != '.') && (board[i-1][j] == board[i-2][j]) && (board[i-2][j] == board[i][j]) && (board[i-3][j] == board[i-2][j]))
						{
							end_state = true;

							if (board[i][j] == 'X')
							{
								winner = 'X';
							}
							else 
							{
								winner = 'O';
							}
						}
					}
				}
				

				if ( (board[i][j] == '.') && (!not_end) )
				{
					not_end = true;
				}
			}

			fscanf(fin, "\n");
		}
		
	print_result(ii);
	
	fscanf(fin, "\n");
	}	// for testcase

	return 1;
}

int print_result(int case_num)
{
	int i = 0, j = 0;

	if ( (winner == 'D') && (not_end) )
	{
		fprintf(fout, "Case #%d: Game has not completed \n", case_num + 1);

	}
	else if ( (winner == 'D') && (!not_end) )
	{
		fprintf(fout, "Case #%d: Draw \n", case_num + 1);

	}
	else
	{
		fprintf(fout, "Case #%d: %c won \n", case_num + 1, winner);
	}

	return 1;
}

int _tmain(int argc, _TCHAR* argv[])
{

	int i = 0, j = 0;

	get_input();

	fclose(fin);
	fclose(fout);

	return 0;
}

