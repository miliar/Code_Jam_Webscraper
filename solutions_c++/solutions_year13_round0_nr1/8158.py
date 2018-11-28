#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
char tic_tac_to[4][4];
int main()
{   int test,counter=1;
char c;
	scanf("%d",&test);
	getchar();
	while(test--)
	{
	int flag=0;	
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		
		scanf("%c",&tic_tac_to[i][j]);
		getchar();
	}
	
	
	
	int rowX=0;int rowO=0;int diaX=0;int diaO=0;int colX=0;int colO=0;int rdiaX=0,rdiaO=0;int dot=0;
	for(int i=0;i<4;i++)
	{    rowX=0;rowO=0;colO=0;colX=0;
		for(int j=0;j<4;j++)
		{if(tic_tac_to[i][j]=='X'||tic_tac_to[i][j]=='T')
		rowX++;
		else if(tic_tac_to[i][j]=='O'||tic_tac_to[i][j]=='T')
		rowO++;
		if(tic_tac_to[j][i]=='X'||tic_tac_to[j][i]=='T')
		colX++;
		else if(tic_tac_to[j][i]=='O'||tic_tac_to[j][i]=='T')
		colO++;
		if(i==j&&(tic_tac_to[i][j]=='X'||tic_tac_to[i][j]=='T'))
		diaX++;
		if(i==j&&(tic_tac_to[i][j]=='O'||tic_tac_to[i][j]=='T'))
		diaO++;
		if(i+j==3&&(tic_tac_to[i][j]=='X'||tic_tac_to[i][j]=='T'))
		rdiaX++;
		if(i+j==3&&(tic_tac_to[i][j]=='O'||tic_tac_to[i][j]=='T'))
		rdiaO++;
		if(tic_tac_to[i][j]=='.')
		dot++;
	}
	if(rowX==4)
	{printf("Case #%d: X won\n",counter);
	flag=1;
	break;
}
	if(rowO==4)
	{printf("Case #%d: O won\n",counter);
	flag=1;
	break;
}	if(colX==4)
	{printf("Case #%d: X won\n",counter);
	flag=1;
	break;
}
	if(colO==4)
	{printf("Case #%d: O won\n",counter);
	flag=1;
	break;
}
	
	}	
		if(flag==0)
		{
		if(diaX==4)
		printf("Case #%d: X won\n",counter);
		else if(rdiaX==4)
		printf("Case #%d: X won\n",counter);
		else if(diaO==4)
			printf("Case #%d: O won\n",counter);
			else if(rdiaO==4)
				printf("Case #%d: O won\n",counter);
		else if(dot==0)
			printf("Case #%d: Draw\n",counter);
			else if(dot!=0)
			printf("Case #%d: Game has not completed\n",counter);
	}
	counter++;
	getchar();
		
	}
	
	return 0;
}
