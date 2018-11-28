#include<stdio.h>
#include<stdlib.h>
char table[7][7];
int solve(char t)
{
	int i,j;
	for(i=0;i<4;++i)
	{
		if(table[i][0]==table[i][1]&&table[i][1]==table[i][2]&&table[i][2]==table[i][3]&&table[i][0]==t)
		{
			return 1;
		}
		if(table[0][i]==table[1][i]&&table[1][i]==table[2][i]&&table[2][i]==table[3][i]&&table[0][i]==t)
		{
			return 1;
		}
	}
	if(table[0][0]==t&&table[0][0]==table[1][1]&&table[1][1]==table[2][2]&&table[2][2]==table[3][3])
	{
		return 1;
	}
	if(table[0][3]==t&&table[0][3]==table[1][2]&&table[1][2]==table[2][1]&&table[2][1]==table[3][0])
	{
		return 1;
	}
	return 0;
}

int main(void)
{
	int test,count=0;
	
	FILE *fr=fopen("A-large.in","r");
	FILE *fw=fopen("Tic-Tac-Toe-Tomek.txt","w");
	fscanf(fr,"%d",&test);
	while(test--)
	{
		count++;
		int i,j;
		int tmpx,tmpy,flag2=0;
		for(i=0;i<4;++i)
		{
			fscanf(fr,"%s",table[i]);
		}
		int flag=0;
		for(i=0;i<4;++i)
		{
			for(j=0;j<4;++j)
			{
				if(table[i][j]=='T')
				{
					flag2=1;
					tmpx=i;
					tmpy=j;
					table[i][j]='X';
				}
				if(flag==0&&table[i][j]=='.')
				{
					flag=1;
				}
			}
		}
		int result1=solve('X');
		if(flag2==1)
		{
			table[tmpx][tmpy]='O';
		}
		int result2=solve('O');
		if(result1==1)
		{
			fprintf(fw,"Case #%d: X won\n",count);
		}
		else
		{
			if(result2==1)
			{
				fprintf(fw,"Case #%d: O won\n",count);
			}
			else
			{
				if(flag==1)
				{
					fprintf(fw,"Case #%d: Game has not completed\n",count);
				}
				else
				{
					fprintf(fw,"Case #%d: Draw\n",count);
				}
			}
		}
	}
	fclose(fr);
	fclose(fw);
	return 0;
}



