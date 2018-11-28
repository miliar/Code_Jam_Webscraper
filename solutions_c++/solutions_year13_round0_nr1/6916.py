#include<stdio.h>
#include<string.h>
#include<stdlib.h>
char kal[10][10];

int bawah(int pos, char x)
{
	if(x=='T')x=kal[1][pos];
	if(x!='.' && (kal[1][pos]==x||kal[1][pos]=='T') && (kal[2][pos]==x||kal[2][pos]=='T') && (kal[3][pos]==x||kal[3][pos]=='T'))
	{
		printf("%c won\n",x);
		return 1;
	}
	else return 0;
}

int samping(int pos, char x)
{
	if(x=='T')x=kal[pos][1];
	if(x!='.' && (kal[pos][1]==x||kal[pos][1]=='T') && (kal[pos][2]==x||kal[pos][2]=='T') && (kal[pos][3]==x||kal[pos][3]=='T'))
	{
		printf("%c won\n",x);
		return 1;
	}
	else return 0;
}

int dia(char x)
{
	if(x=='T')x=kal[1][1];
	if(x!='.' && (kal[1][1]==x||kal[1][1]=='T') && (kal[2][2]==x||kal[2][2]=='T') && (kal[3][3]==x||kal[3][3]=='T'))
	{
		printf("%c won\n",x);
		return 1;
	}
	else return 0;
}

int diag(char x)
{
	if(x=='T')x=kal[1][2];
	if(x!='.' && (kal[1][2]==x||kal[1][2]=='T') && (kal[2][1]==x||kal[2][1]=='T') && (kal[3][0]==x||kal[3][0]=='T'))
	{
		printf("%c won\n",x);
		return 1;
	}
	else return 0;
}

int main()
{
	int t;
	scanf("%d\n",&t);
	for(int it=0;it<t;it++)
	{
		for(int i=0;i<4;i++)scanf("%s",kal[i]);
		getchar();
		getchar();
		int penuh = 0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)if(kal[i][j]!='.')penuh++;
		}
		int win = 0;
		printf("Case #%d: ",it+1);
		for(int i=0;i<4;i++)
		{
			if(kal[0][i]!='.')
			{
				int cekbawah = bawah(i,kal[0][i]);
				if(cekbawah==1)
				{
				//	puts("masuk 1");
						win = 1;
						break;
				}
			}
			if(kal[i][0]!='.')
			{
				int ceksamping = samping(i,kal[i][0]);
				if(ceksamping==1)
				{
				//	puts("masuk 2");
					win = 1;
					break;
				}
			}
		}
		
		
			if(win==0&&kal[0][0]!='.'&&dia(kal[0][0]))
			{
			//	puts("masuk 3");
				win = 1;
			}
			if(win==0&&kal[0][3]!='.'&&diag(kal[0][3]))
			{
			//	puts("masuk 4");
				win = 1;
			}
			if(win==0&&penuh!=16)printf("Game has not completed\n");
			else if(win==0)printf("Draw\n");
		
		
	}
	return 0;
}

