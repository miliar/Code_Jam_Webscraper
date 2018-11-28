#include<iostream>
using namespace std;

#define GN 1000

char board[GN][4][4];
int T = 0;


void input()
{
	scanf("%d",&T);
	getchar();
	for(int t = 0;t < T;t++)
	{
		for(int i = 0;i<4;i++)
		{
			for(int j = 0;j < 4;j++)
			{
				scanf("%c",&board[t][i][j]);
			}
			getchar();
		}
		getchar();
	}
}
int judge(int t)
{
	int i ,j;
	bool isSame = false;
	int player = 0;
	for(i = 0;i < 4;i++)//four row
	{
		for(j = 1;j<4; j++)
		{
			if(((board[t][i][j]==board[t][i][j-1])||(board[t][i][j])=='T'||(board[t][i][j-1])=='T')&&(board[t][i][j]!='.'&&board[t][i][j-1]!='.'))
			{
				isSame = true;
				if(board[t][i][j]=='X')
					player = 1;
				else if(board[t][i][j]=='O')
					player = 2;
			}
			else
			{
				isSame = false;
				break;
			}
		}
		if(isSame)
			return player;
	}
	for(i = 0;i < 4;i++)//four colomn
	{
		for(j = 1;j<4; j++)
		{
			if(((board[t][j][i]==board[t][j-1][i])||(board[t][j][i])=='T'||(board[t][j-1][i])=='T')&&(board[t][j][i]!='.'&&board[t][j-1][i]!='.'))
			{
				isSame = true;
				if(board[t][j][i]=='X')
					player = 1;
				else if(board[t][j][i]=='O')
					player = 2;
			}
			else
			{
				isSame = false;
				break;
			}
		}
		if(isSame)
			return player;
	}
	for(i = 1;i < 4;i++)
	{
		if(((board[t][i][i]==board[t][i-1][i-1])||(board[t][i][i]=='T')||(board[t][i-1][i-1])=='T')&&(board[t][i][i]!='.'&&board[t][i-1][i-1]!='.'))
		{
			isSame = true;
			if(board[t][i][i]=='X')
				player = 1;
			else if(board[t][i][i]=='O')
				player = 2;
		}
		else
		{
			isSame = false;
			break;
		}
	}
	if(isSame)
		return player;
	for(i = 1;i < 4;i++)
	{
		if(((board[t][i][3-i]==board[t][i-1][4-i])||(board[t][i][3-i]=='T')||(board[t][i-1][4-i])=='T')&&(board[t][i][3-i]!='.'&&board[t][i-1][4-i]!='.'))
		{
			isSame = true;
			if(board[t][i][3-i]=='X')
				player = 1;
			else if(board[t][i][3-i]=='O')
				player = 2;
		}
		else
		{
			isSame = false;
			break;
		}
	}
	if(isSame)
		return player;
	for(i = 0;i < 4;i++)//whether finished
	{
		for(j = 1;j<4; j++)
		{
			if(board[t][i][j]=='.')
				return 4;
		}
	}
	return 3;//Draw
}
int main()
{
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("slyar.out", "w", stdout);
	input();
	for(int t = 0;t < T;t++)
	{
		int result = judge(t);
		switch(result)
		{
		case 1: printf("Case #%d: X won",t+1); break;
		case 2: printf("Case #%d: O won",t+1); break;
		case 3: printf("Case #%d: Draw",t+1); break;
		case 4: printf("Case #%d: Game has not completed",t+1); break;
		}
		if(t<T-1)
            printf("\n");
	}
	fflush(stdout);
	fclose(stdin);
	fclose(stdout);
    return 0;
}
