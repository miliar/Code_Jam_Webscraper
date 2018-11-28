#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

#define FOR(i, n) for( int i = 0; i < (int)(n); i++)

char IsLineWinner(char board[4][4]);
char IsColWinner(char board[4][4]);
char IsDiagForwardWinner(char board[4][4]);
char IsDiagBackWinner(char board[4][4]);


void tictac()
{
	int testCaseNum = 0;

	FILE* input = fopen("..\\Input\\A-large.in", "rt");
	FILE* output = fopen("..\\Output\\A-large.out", "wt");

	

	fscanf(input, "%d\r\n", &testCaseNum);

	for (int i = 1; i <= testCaseNum; i++)
	{
		char board[4][4] = { '.' };
		char winner = 'N';
		int isBoardComplete = 1;
		
		FOR(j, 4)
		{
			FOR(k, 4)
			{
				fscanf(input, "%c ", &board[j][k]);

				if (board[j][k] == '.')
				{
					isBoardComplete = 0;
				}
			}
		}

		do
		{
			winner = IsLineWinner(board);
			if (winner != 'N') break;

			winner = IsColWinner(board);
			if (winner != 'N') break;

			winner = IsDiagForwardWinner(board);
			if (winner != 'N') break;

			winner = IsDiagBackWinner(board);
			if (winner != 'N') break;

		} while(false);

		if(winner == 'N')
		{
			if(isBoardComplete == 1)
			{
				fprintf(output, "Case #%d: Draw\r\n", i);
			}
			else
			{
				fprintf(output, "Case #%d: Game has not completed\r\n", i);
			}
		}
		else
		{
			fprintf(output, "Case #%d: %c %s\r\n", i, winner, "won");
		}
	}
}

char IsLineWinner(char board[4][4])
{
	char winner = 'N';

	FOR(j, 4)
	{
		FOR(i, 4)
		{
			if(board[j][i] == '.')
			{
				winner = 'N';
				break;
			}
			else if(board[j][i] == 'T')
			{
				continue;
			}
			else if(winner == 'N')
			{
				winner = board[j][i];
			}
			else if(board[j][i] != winner)
			{
				winner = 'N';
				break;
			}
		}
		if (winner != 'N')
		{
			return winner;
		}
	}

	return winner;
}

char IsColWinner(char board[4][4])
{
	char winner = 'N';

	FOR(j, 4)
	{
		FOR(i, 4)
		{
			if(board[i][j] == '.')
			{
				winner = 'N';
				break;
			}
			else if(board[i][j] == 'T')
			{
				continue;
			}
			else if(winner == 'N')
			{
				winner = board[i][j];
			}
			else if(board[i][j] != winner)
			{
				winner = 'N';
				break;
			}
		}
		if (winner != 'N')
		{
			return winner;
		}
	}

	return winner;
}

char IsDiagForwardWinner(char board[4][4])
{
	char winner = 'N';

	FOR(i, 4)
	{			
		if(board[i][i] == '.')
		{
			winner = 'N';
			break;
		}
		else if(board[i][i] == 'T')
		{

		}
		else if(winner == 'N')
		{
			winner = board[i][i];
		}
		else if(board[i][i] != winner)
		{
			return 'N';
		}
	}

	return winner;
}

char IsDiagBackWinner(char board[4][4])
{
	char winner = 'N';

	FOR(i, 4)
	{
		if(board[i][3-i] == '.')
		{
			winner = 'N';
			break;
		}
		else if(board[i][3-i] == 'T')
		{

		}
		else if(winner == 'N')
		{
			winner = board[i][3-i];
		}
		else if(board[i][3-i] != winner)
		{
			return 'N';
		}
	}

	return winner;
}