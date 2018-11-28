#include<iostream>
#include<stdio.h>

using namespace std;

char board[4][4];

int check(char ch,int n)
{
	int p,q,flag,i,j;
	for(p=0;p<4;p++)
	{
		flag = 0;
		for(q=0;q<4;q++)
		{
			if((board[p][q]=='T')||(board[p][q]==ch))
			{
				continue;
			}
			else
			{				
				flag = 1;
				break;
			}
		}
		if(!flag)
		{
			printf("Case #%d: %c won\n",n,ch);
			return 1;
		}
	}
	for(p=0;p<4;p++)
	{
		flag = 0;
		for(q=0;q<4;q++)
		{
			if((board[q][p]=='T')||(board[q][p]==ch))
			{
				continue;
			}
			else
			{
				flag = 1;
				break;
			}
		}
		if(!flag)
		{
			printf("Case #%d: %c won\n",n,ch);
			return 1;
		}
	}
	if(((board[0][0]=='T')||(board[0][0]==ch))&&((board[1][1]=='T')||(board[1][1]==ch))&&((board[2][2]=='T')||(board[2][2]==ch))&&((board[3][3]=='T')||(board[3][3]==ch)))
	{
		printf("Case #%d: %c won\n",n,ch);
		return 1;
	}
	if(((board[0][3]=='T')||(board[0][3]==ch))&&((board[1][2]=='T')||(board[1][2]==ch))&&((board[2][1]=='T')||(board[2][1]==ch))&&((board[3][0]=='T')||(board[3][0]==ch)))
	{
		printf("Case #%d: %c won\n",n,ch);
		return 1;
	}	
	return 0;
}

int main()
{
	int t,n,dot;
	cin>>t;
	n=1;
	while(t--)
	{
		dot = 0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>board[i][j];
				if(board[i][j]=='.')
				{
					dot++;
				}
			}
		}	
		if(!check('X',n))			
		{
			if(!check('O',n))
			{
				if(!dot)
				{
					printf("Case #%d: Draw\n",n);
				}
				else
				{
					printf("Case #%d: Game has not completed\n",n);
				}
			}
		}		
		n++;
	}		
	return 0;	
}


