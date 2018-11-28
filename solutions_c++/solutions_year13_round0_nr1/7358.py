#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

char board[10][10];

int GetWinner()
{
	for (int i = 0; i < 4; ++i)
	{
		int cntx = 0;
		int cnto = 0;
		int cntt = 0;
		for (int j = 0; j < 4; ++j)
			if (board[i][j] == 'X')
				++cntx;
			else if (board[i][j] == 'O')
				++cnto;
			else if (board[i][j] == 'T')
				++cntt;
		if (cntx + cntt == 4)
			return 1;
		else if (cnto + cntt == 4)
			return 2;
	}

	for (int i = 0; i < 4; ++i)
	{
		int cntx = 0;
		int cnto = 0;
		int cntt = 0;
		for (int j = 0; j < 4; ++j)
			if (board[j][i] == 'X')
				++cntx;
			else if (board[j][i] == 'O')
				++cnto;
			else if (board[j][i] == 'T')
				++cntt;
		if (cntx + cntt == 4)
			return 1;
		else if (cnto + cntt == 4)
			return 2;
	}

	int cntx = 0;
	int cnto = 0;
	int cntt = 0;
	for (int i = 0; i < 4; ++i)
	{
		if (board[i][i] == 'X')
			++cntx;
		else if (board[i][i] == 'O')
			++cnto;
		else if (board[i][i] == 'T')
			++cntt;
	}
	if (cntx + cntt == 4)
		return 1;
	else if (cnto + cntt == 4)
		return 2;
	
	cntx = 0;
	cnto = 0;
	cntt = 0;
	for (int i = 0; i < 4; ++i)
	{
		if (board[i][4 - i - 1] == 'X')
			++cntx;
		else if (board[i][4 - i - 1] == 'O')
			++cnto;
		else if (board[i][4 - i - 1] == 'T')
			++cntt;
	}
	if (cntx + cntt == 4)
		return 1;
	else if (cnto + cntt == 4)
		return 2;

	return 0;
}

bool isEnd()
{
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			if (board[i][j] == '.')
				return false;
	return true;
}

int main()
{
	int test;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &test);
	for (int t = 1; t <= test; ++t)
	{
		for (int i = 0; i < 4; ++i)
			scanf("%s", board[i]);
		
		printf("Case #%d: ", t);
		int winner = GetWinner();
		if (winner == 1)
		{
			printf("X won\n");
		}
		else if (winner == 2)
		{
			printf("O won\n");
		}
		else if (isEnd())
		{
			printf("Draw\n");
		}
		else 
		{
			printf("Game has not completed\n");
		}
	}
	return 0;
}