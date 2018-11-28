#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
char board[4][5];
int getwinner()
{
	int cnt=0;
	if(board[0][0]=='X'&&board[0][1]=='X'&&board[0][2]=='X'&&board[0][3]=='X')
		return 1;
	if(board[1][0]=='X'&&board[1][1]=='X'&&board[1][2]=='X'&&board[1][3]=='X')
		return 1;
	if(board[2][0]=='X'&&board[2][1]=='X'&&board[2][2]=='X'&&board[2][3]=='X')
		return 1;
	if(board[3][0]=='X'&&board[3][1]=='X'&&board[3][2]=='X'&&board[3][3]=='X')
		return 1;
	if(board[0][0]=='T'&&board[0][1]=='X'&&board[0][2]=='X'&&board[0][3]=='X')
		return 1;
	if(board[0][0]=='X'&&board[0][1]=='T'&&board[0][2]=='X'&&board[0][3]=='X')
		return 1;
	if(board[0][0]=='X'&&board[0][1]=='X'&&board[0][2]=='T'&&board[0][3]=='X')
		return 1;
	if(board[0][0]=='X'&&board[0][1]=='X'&&board[0][2]=='X'&&board[0][3]=='T')
		return 1;
	if(board[1][0]=='T'&&board[1][1]=='X'&&board[1][2]=='X'&&board[1][3]=='X')
		return 1;
	if(board[1][0]=='X'&&board[1][1]=='T'&&board[1][2]=='X'&&board[1][3]=='X')
		return 1;
	if(board[1][0]=='X'&&board[1][1]=='X'&&board[1][2]=='T'&&board[1][3]=='X')
		return 1;
	if(board[1][0]=='X'&&board[1][1]=='X'&&board[1][2]=='X'&&board[1][3]=='T')
		return 1;
	if(board[2][0]=='T'&&board[2][1]=='X'&&board[2][2]=='X'&&board[2][3]=='X')
		return 1;
	if(board[2][0]=='X'&&board[2][1]=='T'&&board[2][2]=='X'&&board[2][3]=='X')
		return 1;
	if(board[2][0]=='X'&&board[2][1]=='X'&&board[2][2]=='T'&&board[2][3]=='X')
		return 1;
	if(board[2][0]=='X'&&board[2][1]=='X'&&board[2][2]=='X'&&board[2][3]=='T')
		return 1;
	if(board[3][0]=='T'&&board[3][1]=='X'&&board[3][2]=='X'&&board[3][3]=='X')
		return 1;
	if(board[3][0]=='X'&&board[3][1]=='T'&&board[3][2]=='X'&&board[3][3]=='X')
		return 1;
	if(board[3][0]=='X'&&board[3][1]=='X'&&board[3][2]=='T'&&board[3][3]=='X')
		return 1;
	if(board[3][0]=='X'&&board[3][1]=='X'&&board[3][2]=='X'&&board[3][3]=='T')
		return 1;
	if(board[0][0]=='X'&&board[1][0]=='X'&&board[2][0]=='X'&&board[3][0]=='X')
		return 1;
	if(board[0][1]=='X'&&board[1][1]=='X'&&board[2][1]=='X'&&board[3][1]=='X')
		return 1;
	if(board[0][2]=='X'&&board[1][2]=='X'&&board[2][2]=='X'&&board[3][2]=='X')
		return 1;
	if(board[0][3]=='X'&&board[1][3]=='X'&&board[2][3]=='X'&&board[3][3]=='X')
		return 1;
	if(board[0][0]=='T'&&board[1][0]=='X'&&board[2][0]=='X'&&board[3][0]=='X')
		return 1;
	if(board[0][0]=='X'&&board[1][0]=='T'&&board[2][0]=='X'&&board[3][0]=='X')
		return 1;
	if(board[0][0]=='X'&&board[1][0]=='X'&&board[2][0]=='T'&&board[3][0]=='X')
		return 1;
	if(board[0][0]=='X'&&board[1][0]=='X'&&board[2][0]=='X'&&board[3][0]=='T')
		return 1;
	if(board[0][1]=='T'&&board[1][1]=='X'&&board[2][1]=='X'&&board[3][1]=='X')
		return 1;
	if(board[0][1]=='X'&&board[1][1]=='T'&&board[2][1]=='X'&&board[3][1]=='X')
		return 1;
	if(board[0][1]=='X'&&board[1][1]=='X'&&board[2][1]=='T'&&board[3][1]=='X')
		return 1;
	if(board[0][1]=='X'&&board[1][1]=='X'&&board[2][1]=='X'&&board[3][1]=='T')
		return 1;
	if(board[0][2]=='T'&&board[1][2]=='X'&&board[2][2]=='X'&&board[3][2]=='X')
		return 1;
	if(board[0][2]=='X'&&board[1][2]=='T'&&board[2][2]=='X'&&board[3][2]=='X')
		return 1;
	if(board[0][2]=='X'&&board[1][2]=='X'&&board[2][2]=='T'&&board[3][2]=='X')
		return 1;
	if(board[0][2]=='X'&&board[1][2]=='X'&&board[2][2]=='X'&&board[3][2]=='T')
		return 1;
	if(board[0][3]=='T'&&board[1][3]=='X'&&board[2][3]=='X'&&board[3][3]=='X')
		return 1;
	if(board[0][3]=='X'&&board[1][3]=='T'&&board[2][3]=='X'&&board[3][3]=='X')
		return 1;
	if(board[0][3]=='X'&&board[1][3]=='X'&&board[2][3]=='T'&&board[3][3]=='X')
		return 1;
	if(board[0][3]=='X'&&board[1][3]=='X'&&board[2][3]=='X'&&board[3][3]=='T')
		return 1;
	if(board[0][0]=='O'&&board[0][1]=='O'&&board[0][2]=='O'&&board[0][3]=='O')
		return 2;
	if(board[1][0]=='O'&&board[1][1]=='O'&&board[1][2]=='O'&&board[1][3]=='O')
		return 2;
	if(board[2][0]=='O'&&board[2][1]=='O'&&board[2][2]=='O'&&board[2][3]=='O')
		return 2;
	if(board[3][0]=='O'&&board[3][1]=='O'&&board[3][2]=='O'&&board[3][3]=='O')
		return 2;
	if(board[0][0]=='T'&&board[0][1]=='O'&&board[0][2]=='O'&&board[0][3]=='O')
		return 2;
	if(board[0][0]=='O'&&board[0][1]=='T'&&board[0][2]=='O'&&board[0][3]=='O')
		return 2;
	if(board[0][0]=='O'&&board[0][1]=='O'&&board[0][2]=='T'&&board[0][3]=='O')
		return 2;
	if(board[0][0]=='O'&&board[0][1]=='O'&&board[0][2]=='O'&&board[0][3]=='T')
		return 2;
	if(board[1][0]=='T'&&board[1][1]=='O'&&board[1][2]=='O'&&board[1][3]=='O')
		return 2;
	if(board[1][0]=='O'&&board[1][1]=='T'&&board[1][2]=='O'&&board[1][3]=='O')
		return 2;
	if(board[1][0]=='O'&&board[1][1]=='O'&&board[1][2]=='T'&&board[1][3]=='O')
		return 2;
	if(board[1][0]=='O'&&board[1][1]=='O'&&board[1][2]=='O'&&board[1][3]=='T')
		return 2;
	if(board[2][0]=='T'&&board[2][1]=='O'&&board[2][2]=='O'&&board[2][3]=='O')
		return 2;
	if(board[2][0]=='O'&&board[2][1]=='T'&&board[2][2]=='O'&&board[2][3]=='O')
		return 2;
	if(board[2][0]=='O'&&board[2][1]=='O'&&board[2][2]=='T'&&board[2][3]=='O')
		return 2;
	if(board[2][0]=='O'&&board[2][1]=='O'&&board[2][2]=='O'&&board[2][3]=='T')
		return 2;
	if(board[3][0]=='T'&&board[3][1]=='O'&&board[3][2]=='O'&&board[3][3]=='O')
		return 2;
	if(board[3][0]=='O'&&board[3][1]=='T'&&board[3][2]=='O'&&board[3][3]=='O')
		return 2;
	if(board[3][0]=='O'&&board[3][1]=='O'&&board[3][2]=='T'&&board[3][3]=='O')
		return 2;
	if(board[3][0]=='O'&&board[3][1]=='O'&&board[3][2]=='O'&&board[3][3]=='T')
		return 2;
	if(board[0][0]=='O'&&board[1][0]=='O'&&board[2][0]=='O'&&board[3][0]=='O')
		return 2;
	if(board[0][1]=='O'&&board[1][1]=='O'&&board[2][1]=='O'&&board[3][1]=='O')
		return 2;
	if(board[0][2]=='O'&&board[1][2]=='O'&&board[2][2]=='O'&&board[3][2]=='O')
		return 2;
	if(board[0][3]=='O'&&board[1][3]=='O'&&board[2][3]=='O'&&board[3][3]=='O')
		return 2;
	if(board[0][0]=='T'&&board[1][0]=='O'&&board[2][0]=='O'&&board[3][0]=='O')
		return 2;
	if(board[0][0]=='O'&&board[1][0]=='T'&&board[2][0]=='O'&&board[3][0]=='O')
		return 2;
	if(board[0][0]=='O'&&board[1][0]=='O'&&board[2][0]=='T'&&board[3][0]=='O')
		return 2;
	if(board[0][0]=='O'&&board[1][0]=='O'&&board[2][0]=='O'&&board[3][0]=='T')
		return 2;
	if(board[0][1]=='T'&&board[1][1]=='O'&&board[2][1]=='O'&&board[3][1]=='O')
		return 2;
	if(board[0][1]=='O'&&board[1][1]=='T'&&board[2][1]=='O'&&board[3][1]=='O')
		return 2;
	if(board[0][1]=='O'&&board[1][1]=='O'&&board[2][1]=='T'&&board[3][1]=='O')
		return 2;
	if(board[0][1]=='O'&&board[1][1]=='O'&&board[2][1]=='O'&&board[3][1]=='T')
		return 2;
	if(board[0][2]=='T'&&board[1][2]=='O'&&board[2][2]=='O'&&board[3][2]=='O')
		return 2;
	if(board[0][2]=='O'&&board[1][2]=='T'&&board[2][2]=='O'&&board[3][2]=='O')
		return 2;
	if(board[0][2]=='O'&&board[1][2]=='O'&&board[2][2]=='T'&&board[3][2]=='O')
		return 2;
	if(board[0][2]=='O'&&board[1][2]=='O'&&board[2][2]=='O'&&board[3][2]=='T')
		return 2;
	if(board[0][3]=='T'&&board[1][3]=='O'&&board[2][3]=='O'&&board[3][3]=='O')
		return 2;
	if(board[0][3]=='O'&&board[1][3]=='T'&&board[2][3]=='O'&&board[3][3]=='O')
		return 2;
	if(board[0][3]=='O'&&board[1][3]=='O'&&board[2][3]=='T'&&board[3][3]=='O')
		return 2;
	if(board[0][3]=='O'&&board[1][3]=='O'&&board[2][3]=='O'&&board[3][3]=='T')
		return 2;
	if(board[0][0]=='X'&&board[1][1]=='X'&&board[2][2]=='X'&&board[3][3]=='X')
		return 1;
	if(board[0][0]=='T'&&board[1][1]=='X'&&board[2][2]=='X'&&board[3][3]=='X')
		return 1;
	if(board[0][0]=='X'&&board[1][1]=='T'&&board[2][2]=='X'&&board[3][3]=='X')
		return 1;
	if(board[0][0]=='X'&&board[1][1]=='X'&&board[2][2]=='T'&&board[3][3]=='X')
		return 1;
	if(board[0][0]=='X'&&board[1][1]=='X'&&board[2][2]=='X'&&board[3][3]=='T')
		return 1;
	if(board[0][3]=='X'&&board[1][2]=='X'&&board[2][1]=='X'&&board[3][0]=='X')
		return 1;
	if(board[0][3]=='T'&&board[1][2]=='X'&&board[2][1]=='X'&&board[3][0]=='X')
		return 1;
	if(board[0][3]=='X'&&board[1][2]=='T'&&board[2][1]=='X'&&board[3][0]=='X')
		return 1;
	if(board[0][3]=='X'&&board[1][2]=='X'&&board[2][1]=='T'&&board[3][0]=='X')
		return 1;
	if(board[0][3]=='X'&&board[1][2]=='X'&&board[2][1]=='X'&&board[3][0]=='T')
		return 1;
	if(board[0][0]=='O'&&board[1][1]=='O'&&board[2][2]=='O'&&board[3][3]=='O')
		return 2;
	if(board[0][0]=='T'&&board[1][1]=='O'&&board[2][2]=='O'&&board[3][3]=='O')
		return 2;
	if(board[0][0]=='O'&&board[1][1]=='T'&&board[2][2]=='O'&&board[3][3]=='O')
		return 2;
	if(board[0][0]=='O'&&board[1][1]=='O'&&board[2][2]=='T'&&board[3][3]=='O')
		return 2;
	if(board[0][0]=='O'&&board[1][1]=='O'&&board[2][2]=='O'&&board[3][3]=='T')
		return 2;
	if(board[0][3]=='O'&&board[1][2]=='O'&&board[2][1]=='O'&&board[3][0]=='O')
		return 2;
	if(board[0][3]=='T'&&board[1][2]=='O'&&board[2][1]=='O'&&board[3][0]=='O')
		return 2;
	if(board[0][3]=='O'&&board[1][2]=='T'&&board[2][1]=='O'&&board[3][0]=='O')
		return 2;
	if(board[0][3]=='O'&&board[1][2]=='O'&&board[2][1]=='T'&&board[3][0]=='O')
		return 2;
	if(board[0][3]=='O'&&board[1][2]=='O'&&board[2][1]=='O'&&board[3][0]=='T')
		return 2;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(board[i][j]=='.')
			{
				cnt++;
			}
		}
	}
	if(cnt==0)
		return 0;
	else
		return -1;
}
int main()
{
	int t,i,j;
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		for(i=0;i<4;i++)
			scanf("%s",board[i]);
		int win=getwinner();
		if(win==1)
		{
			printf("Case #%d: X won\n",j);
		}
		else if(win==2)
		{
			printf("Case #%d: O won\n",j);
		}
		else if(win==0)
		{
			printf("Case #%d: Draw\n",j);
		}
		else
		{
			printf("Case #%d: Game has not completed\n",j);
		}
	}
	return 0;
}