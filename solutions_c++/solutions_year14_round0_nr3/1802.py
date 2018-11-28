#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int T,R,C,N,ansx,ansy;
bool map[10][10],c[10][10],done;

bool check(int x,int y)
{
	return map[x-1][y] + map[x+1][y] + map[x][y-1] + map[x][y+1] + map[x-1][y-1] + map[x-1][y+1] + map[x+1][y-1] + map[x+1][y+1] == 0;
}

void floodfill(int x,int y)
{
	if (c[x][y]) return;
	c[x][y] = 1;
	if (!check(x,y)) return;
	if (x-1 > 0 && !map[x-1][y]) floodfill(x-1,y);
	if (x+1 <= R && !map[x+1][y]) floodfill(x+1,y);
	if (y-1 > 0 && !map[x][y-1]) floodfill(x,y-1);
	if (y+1 <= C && !map[x][y+1]) floodfill(x,y+1);
	if (x > 1 && y > 1 && !map[x-1][y-1]) floodfill(x-1,y-1);
	if (x > 1 && y < C && !map[x-1][y+1]) floodfill(x-1,y+1);
	if (x < R && y > 1 && !map[x+1][y-1]) floodfill(x+1,y-1);
	if (x < R && y < C && !map[x+1][y+1]) floodfill(x+1,y+1);
}

void dfs(int x,int y,int tot)
{
	if (tot == N)
	{
		for (int i = 1;i <= R;i ++)
			for (int j = 1;j <= C;j ++)
				if (!map[i][j])
				{
					memset(c,0,sizeof c);
					floodfill(i,j);
					bool bz = 1;
					for (int k = 1;k <= R;k ++)
					{
						for (int p = 1;p <= C;p ++)
							if (!map[k][p] && !c[k][p])
							{
								bz = 0;
								break;
							}
						if (!bz) break;
					}
					if (bz)
					{
						done = 1;
						ansx = i;
						ansy = j;
					}
					if (done) return;
				}
		return;
	}
	if (x > R) return;
	map[x][y] = 1;
	if (y == C) dfs(x+1,1,tot+1);
	else dfs(x,y+1,tot+1);
	if (done) return;
	map[x][y] = 0;
	if (y == C) dfs(x+1,1,tot);
	else dfs(x,y+1,tot);
	if (done) return;
}

int main()
{
	freopen("mine.in","r",stdin);
	freopen("mine.out","w",stdout);
	scanf("%d",&T);
	for (int cas = 1;cas <= T;cas ++)
	{
		scanf("%d%d%d",&R,&C,&N);
		memset(map,0,sizeof map);
		done = 0;
		dfs(1,1,0);
		printf("Case #%d:\n",cas);
		if (!done) puts("Impossible");
		else
		{
			for (int i = 1;i <= R;i ++)
			{
				for (int j = 1;j <= C;j ++)
				{
					if (i == ansx && j == ansy) printf("c");
					else printf("%c",map[i][j]?'*':'.');
				}
				printf("\n");
			}	
		}
	}
	return 0;
}
