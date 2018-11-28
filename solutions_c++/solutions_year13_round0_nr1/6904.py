#include<stdio.h>
#include<string.h>

int main()
{
	freopen("in_a.txt","r",stdin);

	freopen("C:\\Users\\Rana\\Desktop\\codejam first round\\out_a_big.txt","w",stdout);



	long cc,cas;
	char board[5][5];
	char dm[5];
	long i,j,k;
	char win;
	long count;

	scanf("%ld",&cas);

	gets(dm);

	for(cc=1;cc<=cas;cc++)
	{
		//take input

		for(i=0;i<4;i++)
		{
			gets(board[i]);

		}
		gets(board[4]);

		win='d';

		//count blank field
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(board[i][j]=='.')
				{
					win='.';
				}
			}
		}

		//test for X win
		for(i=0;i<4;i++)
		{
			if((board[i][0]=='X' || board[i][0]=='T') && (board[i][1]=='X' || board[i][1]=='T') && (board[i][2]=='X' || board[i][2]=='T') && (board[i][3]=='X' || board[i][3]=='T'))
			{
				win='X';
			}

			if((board[0][i]=='X' || board[0][i]=='T') && (board[1][i]=='X' || board[1][i]=='T') && (board[2][i]=='X' || board[2][i]=='T') && (board[3][i]=='X' || board[3][i]=='T'))
			{
				win='X';
			}
		}
		if((board[0][0]=='X' || board[0][0]=='T') && (board[1][1]=='X' || board[1][1]=='T') && (board[2][2]=='X' || board[2][2]=='T') && (board[3][3]=='X' || board[3][3]=='T'))
		{
			win='X';
		}
		if((board[3][0]=='X' || board[3][0]=='T') && (board[2][1]=='X' || board[2][1]=='T') && (board[1][2]=='X' || board[1][2]=='T') && (board[0][3]=='X' || board[0][3]=='T'))
		{
			win='X';
		}

		//test for O win
		for(i=0;i<4;i++)
		{
			if((board[i][0]=='O' || board[i][0]=='T') && (board[i][1]=='O' || board[i][1]=='T') && (board[i][2]=='O' || board[i][2]=='T') && (board[i][3]=='O' || board[i][3]=='T'))
			{
				win='O';
			}

			if((board[0][i]=='O' || board[0][i]=='T') && (board[1][i]=='O' || board[1][i]=='T') && (board[2][i]=='O' || board[2][i]=='T') && (board[3][i]=='O' || board[3][i]=='T'))
			{
				win='O';
			}
		}
		if((board[0][0]=='O' || board[0][0]=='T') && (board[1][1]=='O' || board[1][1]=='T') && (board[2][2]=='O' || board[2][2]=='T') && (board[3][3]=='O' || board[3][3]=='T'))
		{
			win='O';
		}
		if((board[3][0]=='O' || board[3][0]=='T') && (board[2][1]=='O' || board[2][1]=='T') && (board[1][2]=='O' || board[1][2]=='T') && (board[0][3]=='O' || board[0][3]=='T'))
		{
			win='O';
		}


		if(win=='X' || win=='O')
		{
			printf("Case #%ld: %c won\n",cc,win);
		}
		else if(win=='.')
		{
			printf("Case #%ld: Game has not completed\n",cc);
		}
		else
		{
			printf("Case #%ld: Draw\n",cc);
		}


	}



	return 0;
}
