#include <cstdio>
int xf[4]={-1,1,0,0},yf[4]={0,0,-1,1},T,cas,imp,o,ans,i,j,t,n,m,ch,map[111][111];

bool ok(int x, int y, int t)
{
	x += xf[t];
	y += yf[t];
	while (map[x][y] == '.') x+=xf[t], y+=yf[t];
	return !(map[x][y]=='#');
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &T);
	for (cas=1; cas<=T; ++cas)
	{
		imp = 0;
		scanf("%d%d", &n, &m);
		for (i=1; i<=n; ++i)
		for (j=1; j<=m; ++j)
		{
			for (ch=getchar(); ch<=32; ch=getchar());
			map[i][j] = ch;
		}
		for (i=0; i<=n+1; ++i) map[i][0]=map[i][m+1] = '#';
		for (j=0; j<=m+1; ++j) map[0][j]=map[n+1][j] = '#';
		ans = 0;
		for (i=1; i<=n; ++i)
		for (j=1; j<=m; ++j)
		if (map[i][j] != '.')
		{
			if (map[i][j] == '^') t = 0; else
			if (map[i][j] == 'v') t = 1; else
			if (map[i][j] == '<') t = 2; else t = 3;
			if (ok(i,j,t)) continue;
			++ans;
			o = 0;
			for (t=0; t<4; ++t) o |= ok(i,j,t);
			if (!o)
			{
				imp = 1;
				break;
			}
		}
		printf("Case #%d: ", cas);
		if (imp) printf("IMPOSSIBLE\n"); else printf("%d\n", ans);
	}
	return 0;
}
