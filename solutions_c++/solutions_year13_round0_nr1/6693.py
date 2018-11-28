#include <stdio.h>
char m[4][4]={0,};
int judge(char m[4][4])
{
	int i,j,k=16;
	for(i=0;i<4;i++)
	{
		if((m[i][0]=='X'||m[i][0]=='T')&&(m[i][1]=='X'||m[i][1]=='T')&&(m[i][2]=='X'||m[i][2]=='T')&&(m[i][3]=='X'||m[i][3]=='T'))
			return 1;
		else if((m[i][0]=='O'||m[i][0]=='T')&&(m[i][1]=='O'||m[i][1]=='T')&&(m[i][2]=='O'||m[i][2]=='T')&&(m[i][3]=='O'||m[i][3]=='T'))  
			return 2;                                                                                                                                                                                                                                                                                                                                                                                           
	}
	for(i=0;i<4;i++)
	{
		if((m[0][i]=='X'||m[0][i]=='T')&&(m[1][i]=='X'||m[1][i]=='T')&&(m[2][i]=='X'||m[2][i]=='T')&&(m[3][i]=='X'||m[3][i]=='T'))
			return 1;
		else if((m[0][i]=='O'||m[0][i]=='T')&&(m[1][i]=='O'||m[1][i]=='T')&&(m[2][i]=='O'||m[2][i]=='T')&&(m[3][i]=='O'||m[3][i]=='T'))  
			return 2;                                                                                                                                                                                                                                                                                                                                                                                           
	}
	if((m[0][0]=='X'||m[0][0]=='T')&&(m[1][1]=='X'||m[1][1]=='T')&&(m[2][2]=='X'||m[2][2]=='T')&&(m[3][3]=='X'||m[3][3]=='T'))
		return 1;
	else if((m[0][0]=='O'||m[0][0]=='T')&&(m[1][1]=='O'||m[1][1]=='T')&&(m[2][2]=='O'||m[2][2]=='T')&&(m[3][3]=='O'||m[3][3]=='T'))
		return 2;                                                                  
	else if((m[3][0]=='X'||m[3][0]=='T')&&(m[2][1]=='X'||m[2][1]=='T')&&(m[1][2]=='X'||m[1][2]=='T')&&(m[0][3]=='X'||m[0][3]=='T'))
		return 1;
	else if((m[3][0]=='O'||m[3][0]=='T')&&(m[2][1]=='O'||m[2][1]=='T')&&(m[1][2]=='O'||m[1][2]=='T')&&(m[0][3]=='O'||m[0][3]=='T'))
		return 2; 
	else
	{
		for (i = 0; i < 4; i++)
		{
			for ( j = 0; j < 4; j++)
			{
				if (m[i][j]=='.')
					return 3;
				else
					k-=1;
			}
		}
	}
	if (k==0)
		return 4;
}
int main()
{
	int cas,k=1;
	scanf("%d",&cas);
	while(cas--)
	{
		int i,j,c;
		for(i=0;i<4;i++) 
			scanf("%s",&m[i]); 
		printf("Case #%d: ",k);
		k+=1;
		switch(judge(m))
		{
		case 1:
			printf("X won\n");
			break;
		case 2:
			printf("O won\n");
			break;
		case 3:
			printf("Game has not completed\n");
			break;
		case 4:
			printf("Draw\n");
			break;
		}
	}
}