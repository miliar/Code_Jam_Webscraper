#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;

int T, R, C;
char a[101][101];
bool vis[101][101];
int ans;

char gox[129];
char goy[129];

int lx, ly,ld;

inline void ComplexSolve()
{
    for (int i=lx-1;i>0;i--)
        if (a[i][ly]!='.')
            return ;
    for (int i=lx+1;i<=R;i++)
        if (a[i][ly]!='.')
            return ;
    for (int j=ly-1;j>0;j--)
        if (a[lx][j]!='.' )
            return ;
    for (int j=ly+1;j<=C;j++)
        if (a[lx][j]!='.')
            return ;
    ans=-1;
}

void DFS(int x, int y, int d)
{
    if (vis[x][y]) return;
	if (a[x][y]!='.') vis[x][y] = true;

	if (a[x][y] != '.')
	{
		ld = d;
		lx = x;
		ly = y;
		d = a[x][y];
	}
	x += gox[d]; y += goy[d];

	if (x<=0 || x>R || y<=0 || y>C)
    {
        ans++;
        if (ld!=0)
            a[lx][ly] = ld;
        else ComplexSolve();
    }
	else DFS(x,y,d);
}

int main()
{
	freopen("A-large_lyz.in", "r", stdin);
	freopen("A-large_lyzlyz.out","w",stdout);

	gox['^'] = -1; goy['^'] = 0;
	gox['v'] =  1; goy['v'] = 0;
	gox['<'] = 0; goy['<'] = -1;
	gox['>'] = 0; goy['>'] = 1;

	scanf("%d\n", &T);
	for (int nowT = 1; nowT <= T; nowT++)
	{
		ans = 0;
		scanf("%d %d\n", &R, &C);
		memset(vis, 0, sizeof vis);
		for (int i = 1; i <= R; i++)
		{
			for (int j = 1; j <= C; j++)
				scanf("%c", &a[i][j]);
			scanf("\n");
		}
		for (int i = 1; i <= R; i++)
			for (int j = 1; j <= C; j++)
				if (ans>=0 && a[i][j]!='.' && !vis[i][j])
					DFS(i,j,0);

		if (ans>=0) printf("Case #%d: %d\n", nowT, ans);
		else printf("Case #%d: IMPOSSIBLE\n", nowT);

	}
	return 0;
}
