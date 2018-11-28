#include <winsock2.h>
#include <stdio.h>

int cas, f, mark;
char g[5][5] ;
void check(char a, char b, char c, char d)
{
	int cnto, cntg;
	cnto = cntg = 0;
	char tmp[5] ;
	tmp[1] = a, tmp[2] = b, tmp[3] = c, tmp[4] = d;
	int t = 0;
	for(int i=1; i<=4; i++)
	{
		if(tmp[i] == 'O')
			cnto ++;
		else if(tmp[i] == 'X')
			cntg++;
		else if(tmp[i] == 'T')
			t = 1;
		else
			mark = 1;
	}
	if(cnto == 4|| cnto+t == 4)
	{
		printf("O won\n");
		f = 1;
		return ;
	}
	if(cntg == 4|| cntg+t == 4)
	{
		printf("X won\n");
		f = 1;
		return ;
	}
	
}
int main()
{
	int i, j, c = 1;
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &cas);

	while(cas--)
	{
		f = 0, mark = 0;
		for(i=1; i<=4; i++)
			scanf("%s", g[i]+1);
		printf("Case #%d: ", c++);
		for(j=1; j<=4 && !f; j++)
		{
			check(g[j][1], g[j][2], g[j][3], g[j][4]);
		}
		for(j=1; j<=4 && !f; j++)
		{
			check(g[1][j], g[2][j], g[3][j], g[4][j]);
		}
		if(!f)
			check(g[1][1], g[2][2], g[3][3], g[4][4]);
		if(!f)
			check(g[1][4], g[2][3], g[3][2], g[4][1]);
		if(!f)
		{
			if(mark == 1)
				printf("Game has not completed\n");
			else
				printf("Draw\n");
		}
	}
 	return 0;
}