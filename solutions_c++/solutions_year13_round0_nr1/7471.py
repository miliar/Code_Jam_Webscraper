#include<cstdio>
#include<cstring>

char board[4][4],tmp;
int  x,o,numdot,tcase,Case=0;
bool tie;
  
int main()
{
	scanf("%d",&tcase);
	while(tcase--)
	{
		tie=true;
		for(int i=0;i<4;i++)
			scanf("%s",board[i]);
		printf("Case #%d: ",++Case);
		for(int i=0;i<4;i++)
		{
			x=o=0;
			for(int j=0;j<4;j++)
			{
				if(board[i][j]=='X'||board[i][j]=='T')
				  x++;
				if(board[i][j]=='O'||board[i][j]=='T')
				  o++;
			}
			if(x==4)
			{
			  printf("X won\n");
			  tie=false;
			  break;
			}
			if(o==4)
			{
			  printf("O won\n");
			  tie=false;
			  break;
			}
			x=o=0;
			for(int j=0;j<4;j++)
			{
				if(board[j][i]=='X'||board[j][i]=='T')
				  x++;
				if(board[j][i]=='O'||board[j][i]=='T')
				  o++;
			}
			if(x==4)
			{
			  printf("X won\n");
			  tie=false;
			  break;
			}
			if(o==4)
			{
			  printf("O won\n");
			  tie=false;
			  break;
			}
		}
		if(tie)
		{
		x=o=0;
		for(int j=0;j<4;j++)
		{
			if(board[j][j]=='X'||board[j][j]=='T')
			  x++;
			if(board[j][j]=='O'||board[j][j]=='T')
			  o++;
		}
		if(x==4)
		{
		  printf("X won\n");
		  tie=false;
		}
		if(o==4)
		{
		  printf("O won\n");
		  tie=false;
		}
		if(tie)
		{
		x=o=0;
		for(int j=0;j<4;j++)
		{
			if(board[j][3-j]=='X'||board[j][3-j]=='T')
			  x++;
			if(board[j][3-j]=='O'||board[j][3-j]=='T')
			  o++;
		}
		if(x==4)
		{
		  printf("X won\n");
		  tie=false;
		}
		if(o==4)
		{
		  printf("O won\n");
		  tie=false;
		}
		}
		if(tie)
		{
			numdot=0;
			for(int i=0;i<4;i++)
			  for(int j=0;j<4;j++)
			   if(board[i][j]=='.')
			  {
				numdot++;
				break;
			  }
			if(numdot>0)
			  printf("Game has not completed\n");
			else
			  printf("Draw\n");
		}
		}
	}
	return 0;
}

