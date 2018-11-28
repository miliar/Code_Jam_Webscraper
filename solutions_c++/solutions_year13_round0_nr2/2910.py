#include <stdio.h>
#include <stdlib.h>

const char *checkBoard(int board[4][4])
{
	for(int i = 0; i < 4; ++i)
	{
		int count = 0;
		for(int j = 0; j < 4; ++j)
			count += board[i][j];
		if(count == -4 || count == -3)
			return "O won";
		if(count == 4 || count == 3)
			return "X won";
	}
	for(int i = 0; i < 4; ++i)
	{
		int count = 0;
		for(int j = 0; j < 4; ++j)
			count += board[j][i];
		if(count == -4 || count == -3)
			return "O won";
		if(count == 4 || count == 3)
			return "X won";
	}
	int count = 0;
	for(int i = 0; i < 4; ++i)
	{
		count += board[i][i];
	}
	if(count == -4 || count == -3)
		return "O won";
	if(count == 4 || count == 3)
		return "X won";
	count = 0;
	for(int i = 3; i >=0; --i)
	{
		count += board[i][3-i];
	}
	if(count == -4 || count == -3)
		return "O won";
	if(count == 4 || count == 3)
		return "X won";
	count = 0;
	for(int i = 0; i < 4; ++i)
	{
		for(int j = 0; j < 4; ++j)
			count += board[i][j];
	}
	if(count > 50)
		return "Game has not completed";
	return "Draw";
}

int main()
{
	char str[128];
	fgets(str, 128, stdin);
	int ninputs = atoi(str);
	for(int i = 0; i < ninputs; ++i)
	{
		int board[4][4];
		for(int k = 0; k < 4; ++k)
		{
			fgets(str, 128, stdin);
			for(int j = 0; j < 4; ++j)
			{
				if(str[j] == 'X')
					board[k][j] = 1;
				else if(str[j] == '.')
					board[k][j] = 100;
				else if(str[j] == 'O')
					board[k][j] = -1;
				else if(str[j] == 'T')
					board[k][j] = 0;
			}
		}
		fgets(str, 128, stdin);
		printf("Case #%d: %s\n", i+1, checkBoard(board));
	}
}

