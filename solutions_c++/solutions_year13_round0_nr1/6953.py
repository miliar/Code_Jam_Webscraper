#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;


main()
{
	int T,CASE=0;
	int i,j,k,p;
	char board[5][5];
	char buf[1000];
	int x,o,t;


//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("A-small-attempt0.out","w",stdout);

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int winner, blank;

	gets(buf);
	sscanf(buf,"%d",&T);

	while(T--)
	{
		CASE++;

		for(i=0; i<4; i++)
		{
			gets(board[i]);
		}

		gets(buf);

		winner = -1;

		for(i=0; i<4 && winner == -1; i++)
		{
			x = o = t = 0;

			for(j=0; j<4; j++)
			{
				if(board[i][j] == 'X')
					x++;
				else if(board[i][j] == 'O')
					o++;
				else if(board[i][j] == 'T')
					t++;
			}

			if(x == 4 || (x == 3 && t == 1))
			{
				winner = 1;
			}
			else if(o == 4 || (o == 3 && t == 1))
			{
				winner = 0;
			}


			if(winner == -1)
			{
				x = o = t = 0;

				for(j=0; j<4; j++)
				{
					if(board[j][i] == 'X')
						x++;
					else if(board[j][i] == 'O')
						o++;
					else if(board[j][i] == 'T')
						t++;
				}

				if(x == 4 || (x == 3 && t == 1))
				{
					winner = 1;
				}
				else if(o == 4 || (o == 3 && t == 1))
				{
					winner = 0;
				}
			}


		}

		x = o = t = 0;
		for(i=0; i<4 && winner == -1; i++)
			for(j=0; j<4; j++)
				if(i == j)
				{
					if(board[i][j] == 'X')
						x++;
					else if(board[i][j] == 'O')
						o++;
					else if(board[i][j] == 'T')
						t++;
				}

		if(x == 4 || (x == 3 && t == 1))
		{
			winner = 1;
		}
		else if(o == 4 || (o == 3 && t == 1))
		{
			winner = 0;
		}


		x = o = t = 0;
		for(i=0; i<4 && winner == -1; i++)
			for(j=0; j<4; j++)
				if(i == j)
				{
					if(board[i][3-j] == 'X')
						x++;
					else if(board[i][3-j] == 'O')
						o++;
					else if(board[i][3-j] == 'T')
						t++;
				}

		if(x == 4 || (x == 3 && t == 1))
		{
			winner = 1;
		}
		else if(o == 4 || (o == 3 && t == 1))
		{
			winner = 0;
		}

		blank = 0;
		for(i=0; i<4 && winner == -1; i++)
			for(j=0; j<4; j++)
				if(board[i][j] == '.')
					blank++;


		if(winner == 1)
			printf("Case #%d: X won\n",CASE);
		else if(winner == 0)
			printf("Case #%d: O won\n",CASE);
		else if(winner == -1 && blank == 0)
			printf("Case #%d: Draw\n",CASE);
		else
			printf("Case #%d: Game has not completed\n",CASE);


	}




}