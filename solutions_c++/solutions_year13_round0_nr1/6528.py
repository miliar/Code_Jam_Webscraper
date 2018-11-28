#include<iostream>
#include<cstdio>
using namespace std;


int checkforY(int board[][4])
{
int cnt=0;
	int i,j;
	//either all are x or 3 are x and one T
	for(i=0;i<4;i++)
	{
		cnt=0;
		for(j=0;j<4;j++)
			{
			if(board[i][j]=='O' || board[i][j]=='T' )
				{
				cnt++;
				}
			}
		if(cnt==4)
		return 1;
	}


	for(i=0;i<4;i++)
	{
		cnt=0;
		for(j=0;j<4;j++)
			{
			if(board[j][i]=='O' || board[j][i]=='T' )
				{
				cnt++;
				}
			}
		if(cnt==4)
		return 1;
	}


	if( (board[0][0]=='O' || board[0][0]=='T') && (board[1][1]=='O' || board[1][1]=='T') && (board[2][2]=='O' || board[2][2]=='T') && (board[3][3]=='O' || board[3][3]=='T') )
		return 1;

		if( (board[0][3]=='O' || board[0][3]=='T') && (board[1][2]=='O' || board[1][2]=='T') && (board[2][1]=='O' || board[2][1]=='T') && (board[3][0]=='O' || board[3][0]=='T') )
		return 1;

	return 0;












}

int checkforX(int board[][4])
{
int cnt=0;
	int i,j;
	//either all are x or 3 are x and one T
	for(i=0;i<4;i++)
	{
		cnt=0;
		for(j=0;j<4;j++)
			{
			if(board[i][j]=='X' || board[i][j]=='T' )
				{
				cnt++;
				}
			}
		if(cnt==4)
		return 1;
	}


	for(i=0;i<4;i++)
	{
		cnt=0;
		for(j=0;j<4;j++)
			{
			if(board[j][i]=='X' || board[j][i]=='T' )
				{
				cnt++;
				}
			}
		if(cnt==4)
		return 1;
	}


	if( (board[0][0]=='X' || board[0][0]=='T') && (board[1][1]=='X' || board[1][1]=='T') && (board[2][2]=='X' || board[2][2]=='T') && (board[3][3]=='X' || board[3][3]=='T') )
		return 1;

		if( (board[0][3]=='X' || board[0][3]=='T') && (board[1][2]=='X' || board[1][2]=='T') && (board[2][1]=='X' || board[2][1]=='T') && (board[3][0]=='X' || board[3][0]=='T') )
		return 1;

	return 0;


}






int checkboard(int board[][4],int dots)
{
int flag=0;

flag=checkforX(board);

if(flag==1)
{
printf("X won\n");
return 0;
}

	
	flag=checkforY(board);	

	
	if(flag==1)
	{
	printf("O won\n");
	return 0;
	}


		if(dots!=0)
		{
		printf("Game has not completed\n");
		return 0;
		}
		else
		{
		printf("Draw\n");
		return 0;
		}


	





}






int main()
{
	int t,i,j;
	scanf("%d",&t);
	char a,b,c,d;
        int board[4][4];
	int dots=0;
	for(i=0;i<t;i++)
		{

			dots=0;
			for(j=0;j<4;j++)
			{
			//scanf("%c%c%c%c",&a,&b,&c,&d);
			cin>>a>>b>>c>>d;
			if(a=='.' || b=='.' || c=='.' || d=='.' )
			dots++;
			board[j][0]=a;
			board[j][1]=b;
			board[j][2]=c;
			board[j][3]=d;
			}
			
			printf("Case #%d: ",i+1);
			checkboard(board,dots);
			//printf("Case #%d",i+1);
			


		}












return 0;
}
