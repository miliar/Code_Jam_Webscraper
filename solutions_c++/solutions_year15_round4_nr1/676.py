#include <cstdio>
#include <cstring>

const int Maxn=105;

bool left[Maxn][Maxn], right[Maxn][Maxn], up[Maxn][Maxn], down[Maxn][Maxn];
char str[Maxn][Maxn];

int main()
{
	int T, n, m;
	scanf("%d", &T);
	for (int tt=1; tt<=T; ++tt)
	{
		memset(left, 0, sizeof left);
		memset(right, 0, sizeof right);
		memset(up, 0, sizeof up);
		memset(down, 0, sizeof down);
		scanf("%d%d", &n, &m);
		for (int i=1; i<=n; ++i) scanf("%s", &str[i][1]);
		for (int i=1; i<=n; ++i)
			for (int j=1; j<=m; ++j)
			{
				left[i][j]=left[i][j-1]|(str[i][j]!='.');
				up[i][j]=up[i-1][j]|(str[i][j]!='.');
			}
		for (int i=n; i; --i)
			for (int j=m; j; --j)
			{
				right[i][j]=right[i][j+1]|(str[i][j]!='.');
				down[i][j]=down[i+1][j]|(str[i][j]!='.');
			}
		int cnt=0;
		for (int i=1; i<=n; ++i)
		{
			for (int j=1; j<=m; ++j)
			{
				if (str[i][j]=='.') continue;
				if (!left[i][j-1] && !right[i][j+1] && !up[i-1][j] && !down[i+1][j])
				{
					cnt=-1;
					break;
				}
				switch (str[i][j])
				{
					case '^':
						if (!up[i-1][j]) ++cnt; break;
					case 'v':
						if (!down[i+1][j]) ++cnt; break;
					case '<':
						if (!left[i][j-1]) ++cnt; break;
					case '>':
						if (!right[i][j+1]) ++cnt; break;
				}
			}
			if (cnt<0) break;
		}
		printf("Case #%d: ", tt);
		if (cnt<0) puts("IMPOSSIBLE");
		else printf("%d\n", cnt);
	}
	return 0;
}

