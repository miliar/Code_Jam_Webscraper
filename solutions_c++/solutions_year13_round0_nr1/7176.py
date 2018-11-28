// A.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"

#include<iostream>
#include<cstdio>
using namespace std;

char board[4][4];

int check()
{
	int i,j,cc,rc,r=0,pd=0,sd=0;
	for(i=0;i<4;i++)
	{
		rc = cc = 0;
		for(j=0;j<4;j++)
		{
			if(board[i][j]=='X' || board[i][j]=='T')
				rc++;

			if(board[j][i]=='X' || board[j][i]=='T')
				cc++;

			if(board[i][j]=='.')r = 3;
		}
		if(rc==4 || cc==4)return 1;
		if(board[i][i]=='X'||board[i][i]=='T')pd++;
		if(board[i][3-i]=='X'||board[i][3-i]=='T')sd++;

		if(pd==4||sd==4)return 1;
	}

	//Check for O
	cc = rc = pd = sd = 0;
	for(i=0;i<4;i++)
	{
		rc = cc = 0;
		for(j=0;j<4;j++)
		{
			if(board[i][j]=='O' || board[i][j]=='T')
				rc++;

			if(board[j][i]=='O' || board[j][i]=='T')
				cc++;
		}

		if(rc==4 || cc==4)return 2;
		if(board[i][i]=='O'||board[i][i]=='T')pd++;
		if(board[i][3-i]=='O'||board[i][3-i]=='T')sd++;

		if(pd==4||sd==4)return 2;
	}

	if(!r)return 3;
		return 4;

}


int main()
{
	int t,i,j,k;
	freopen("A-large.in","r",stdin);
	freopen("out12.txt","w",stdout);
	scanf("%d\n",&t);

	for(k=1;k<=t;k++)
	{
		for(i=0;i<4;i++)
			gets(board[i]);
		switch(check())
		{
			case 1:	printf("Case #%d: X won\n",k); break;
			case 2: printf("Case #%d: O won\n",k); break;
			case 3: printf("Case #%d: Draw\n",k); break;
			case 4: printf("Case #%d: Game has not completed\n",k); break;
		}
		gets(board[0]);
	}
	return 0;
}

