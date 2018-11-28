#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 505;

bool get;
bool Ch[MAXN][MAXN];
int Ref[MAXN][MAXN][4],Ord[MAXN * 2],Final[MAXN],To[MAXN],Next[MAXN],Fa[MAXN],R,C,cnt,tot;

int Get(int a) {return Fa[a] == a ? a : Fa[a] = Get(Fa[a]);}

void Link(int u,int v)
{
	Fa[Get(u)] = Get(v);
}

int Pd(int u)
{
	if (u <= C) return Ref[1][u][0];
	if (u <= C + R) return Ref[u - C][C][1];
	if (u <= C + R + C) return Ref[R][C - (u - C - R) + 1][2];
	return Ref[R - (u - C - R - C) + 1][1][3];
}

void Test()
{
	tot = 0;
	for(int i = 1;i <= cnt;i ++) Final[i] = 0;
	for(int i = 1;i <= cnt;i ++) Fa[i] = i;
	for(int i = 1;i <= R;i ++)
		for(int j = 1;j <= C;j ++)
		{
			if (!Ch[i][j])
			{
				for(int k = 0;k < 4;k += 2) Link(Ref[i][j][k],Ref[i][j][k + 1]);
			} else
			{
				Link(Ref[i][j][0],Ref[i][j][3]),Link(Ref[i][j][1],Ref[i][j][2]);
			}
			if (j + 1 <= C)
				Link(Ref[i][j][1],Ref[i][j + 1][3]);
			if (i + 1 <= R)
				Link(Ref[i][j][2],Ref[i + 1][j][0]);
		}
	for(int i = 1;i <= 2 * (R + C);i += 2)
	{
		int u = Ord[i];
		if (Get(Pd(u)) != Get(Pd(Ord[i + 1]))) return;
	}
	get = 1;
	for(int i = 1;i <= R;i ++)
	{
		for(int j = 1;j <= C;j ++)
			if (!Ch[i][j]) printf("\\"); else
				printf("/");
		printf("\n");
	}
}

void Dfs(int x,int y)
{
	if (get) return;
	if (x > R) {Test();return;}
	if (y > C) {Dfs(x + 1,1);return;}
	for(int i = 0;i < 2;i ++)
		Ch[x][y] = i,Dfs(x,y + 1); 
}

void Work(int Case)
{
	printf("Case #%d:\n", Case);
	memset(Ch,0,sizeof Ch);
	scanf("%d%d", &R, &C);
	cnt = 0;
	for(int i = 1;i <= R;i ++)
		for(int j = 1;j <= C;j ++)
			for(int k = 0;k < 4;k ++) Ref[i][j][k] = ++ cnt;
	for(int i = 1;i <= 2 * (R + C);i ++)
		scanf("%d", &Ord[i]);
	get = 0;
	Dfs(1,1);
	if (!get) printf("IMPOSSIBLE\n");
}

int main()
{
	freopen("data.in","r",stdin);
	int T;
	scanf("%d", &T);
	for(int i = 1;i <= T;i ++)
		Work(i);
	return 0;
}
