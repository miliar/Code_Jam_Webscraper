#include <stdio.h>
char Grid[105][105];
int R,C;
int moveOut(int y,int x)
{
	int dy=0,dx=0;
	switch(Grid[y][x])
	{
		case '<':dx=-1;break;
		case '>':dx=1;break;
		case '^':dy=-1;break;
		case 'v':dy=1;break;
	}
	y+=dy;
	x+=dx;
	while (y>=0 && y<R && x>=0 && x<C)
	{
		if (Grid[y][x] !='.') return 0;
		y+=dy;
		x+=dx;
	}
	return 1;
}
int main()
{
	int T; scanf("%d",&T);
	for (int kase=1;kase<=T;++kase)
	{
		scanf("%d %d",&R,&C);
		for (int q=0;q<R;q++)
			scanf("%s",Grid[q]);
		bool impo = false;
		int cnt = 0;
		for (int q=0;q<R;q++) for (int w=0;w<C;w++)
		{
			if (Grid[q][w]!='.')
			{
				if (moveOut(q,w))
				{
					cnt++;
					int meet = -2;
					for (int e=0;e<C;e++)
						if (Grid[q][e]!='.')meet++;
					for (int e=0;e<R;e++)
						if (Grid[e][w]!='.')meet++;
					if (meet <= 0)
						impo = true;
				}
			}
		}
		printf("Case #%d: ",kase);
		if (impo) printf("IMPOSSIBLE\n");
		else printf("%d\n",cnt);
	}
	return 0;
}