#include<stdio.h>
char map[4][4];
int main()
{
	freopen("C:/Users/zyren/Downloads/A-large.in", "r", stdin);
	freopen("C:/Users/zyren/Downloads/A-large.in.out", "w", stdout);
	int T,i=0,tag=0;
	scanf("%d", &T);
	while (++i<=T)
	{
		tag = 0;
		for (int j=0; j<4; j++)
		{
			getchar();
			for (int k=0; k<4; k++)
				scanf("%c", &map[j][k]);
		}
		getchar();
		printf("Case #%d: ", i);
		for (int j=0; j<4; j++)
		{
			if((map[j][0]=='O'||map[j][0]=='T')
				&&(map[j][1]=='O'||map[j][1]=='T')
				&&(map[j][2]=='O'||map[j][2]=='T')
				&&(map[j][3]=='O'||map[j][3]=='T'))
			{
				printf("O won\n");
				tag = 1;
				break;
			}
			if((map[0][j]=='O'||map[0][j]=='T')
				&&(map[1][j]=='O'||map[1][j]=='T')
				&&(map[2][j]=='O'||map[2][j]=='T')
				&&(map[3][j]=='O'||map[3][j]=='T'))
			{
				printf("O won\n");
				tag = 1;
				break;
			}
		}
		if(tag)
			continue;

		if((map[0][0]=='O'||map[0][0]=='T')
			&&(map[1][1]=='O'||map[1][1]=='T')
			&&(map[2][2]=='O'||map[2][2]=='T')
			&&(map[3][3]=='O'||map[3][3]=='T'))
		{
			printf("O won\n");
			tag = 1;
			continue;
		}
		if((map[0][3]=='O'||map[0][3]=='T')
			&&(map[1][2]=='O'||map[1][2]=='T')
			&&(map[2][1]=='O'||map[2][1]=='T')
			&&(map[3][0]=='O'||map[3][0]=='T'))
		{
			printf("O won\n");
			tag = 1;
			continue;
		}


		for (int j=0; j<4; j++)
		{
			if((map[j][0]=='X'||map[j][0]=='T')
				&&(map[j][1]=='X'||map[j][1]=='T')
				&&(map[j][2]=='X'||map[j][2]=='T')
				&&(map[j][3]=='X'||map[j][3]=='T'))
			{
				printf("X won\n");
				tag = 1;
				break;
			}
			if((map[0][j]=='X'||map[0][j]=='T')
				&&(map[1][j]=='X'||map[1][j]=='T')
				&&(map[2][j]=='X'||map[2][j]=='T')
				&&(map[3][j]=='X'||map[3][j]=='T'))
			{
				printf("X won\n");
				tag = 1;
				break;
			}
		}
		if(tag)
			continue;
		if((map[0][0]=='X'||map[0][0]=='T')
			&&(map[1][1]=='X'||map[1][1]=='T')
			&&(map[2][2]=='X'||map[2][2]=='T')
			&&(map[3][3]=='X'||map[3][3]=='T'))
		{
			printf("X won\n");
			tag = 1;
			continue;
		}
		if((map[0][3]=='X'||map[0][3]=='T')
			&&(map[1][2]=='X'||map[1][2]=='T')
			&&(map[2][1]=='X'||map[2][1]=='T')
			&&(map[3][0]=='X'||map[3][0]=='T'))
		{
			printf("X won\n");
			tag = 1;
			continue;
		}

		for (int j=0; j<4; j++)
			for (int k=0; k<4; k++)
				if(map[j][k]=='.')
					tag = 1;
		if(tag==1)
			printf("Game has not completed\n");
		else
			printf("Draw\n");
	}
	return 0;
}