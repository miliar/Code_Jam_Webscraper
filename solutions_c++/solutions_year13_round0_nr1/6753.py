#include <stdio.h>
#include <string.h>

char board[4][10];

bool IsWin(char p)
{
    int i,j;
	//row
	for(i=0; i<4; ++i)
	{
		for(j=0; j<4; ++j)
		{
			if(board[i][j] != p && board[i][j] != 'T')
			{
				break;
			}
		}
		if(j == 4)
		{
			return true;
		}
	}
	
	//column
	for(i=0; i<4; ++i)
	{
		for(j=0; j<4; ++j)
		{
			if(board[j][i] != p && board[j][i] != 'T')
			{
				break;
			}
		}
		if(j == 4)
		{
			return true;
		}
	}
	
	for(i=0; i<4; ++i)
	{
		if(board[i][i] != p && board[i][i] != 'T')
		{
			break;
		}
	}
	if(i == 4)
	{
		return true;
	}
	
	for(i=0; i<4; ++i)
	{
		if(board[i][3-i] != p && board[i][3-i] != 'T')
		{
			break;
		}
	}
	if(i == 4)
	{
		return true;
	}
	
	return false;
}

bool Finish()
{
	int i,j;
	for(i=0; i<4; ++i)
	{
		for(j=0; j<4; ++j)
		{
			if(board[i][j] == '.')
			return false;
		}
	}
	return true;
}

int main(void)
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
	int x,t;
	scanf("%d", &t);
	for(x=1; x<=t; ++x)
	{
		int i,j;
		for(i=0; i<4; ++i)
		{
			scanf("%s", board[i]);
		}
		
		printf("Case #%d: ", x);
		if(IsWin('X'))
		{
			printf("X won\n");
		}
		else if(IsWin('O'))
		{
			printf("O won\n");
		}
		else if(!Finish())
		{
			printf("Game has not completed\n");
		}
		else
		{
			printf("Draw\n");
		}
	}
	
	return 0;
}
