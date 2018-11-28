#include <cstdio>
#include <cstring>
const int Maxk=5, Maxn=10, Maxl=15, Maxv=110;
int n, k, ans, cnt, u[Maxk], g[Maxv], a[Maxn], next[Maxv];
char s[Maxn][Maxl], ch[Maxv];

void dfs(int dep)
{
	if (dep==n)
	{
		for (int i=0; i<k; ++i)
			if (!u[i]) return;
		int tot=0;
		//memset(g, 0, sizeof g);
		for (int i=0; i<k; ++i) g[++tot]=0;
		for (int i=0; i<n; ++i)
		{
			int v=a[i]+1, p;
			for (int j=0; s[i][j]; ++j)
			{
				for (p=g[v]; p; p=next[p])
					if (ch[p]==s[i][j]) break;
				if (p) v=p; else
				{
					++tot;
					ch[tot]=s[i][j]; next[tot]=g[v]; g[v]=tot;
					v=tot;
					g[tot]=0;
				}
			}
		}
		if (tot>ans) ans=tot, cnt=1;
		else if (tot==ans) ++cnt;
		return;
	}
	for (int i=0; i<k; ++i)
	{
		a[dep]=i;
		++u[i];
		dfs(dep+1);
		--u[i];
	}
}

int main()
{
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int T, i;
	scanf("%d", &T);
	for (int tt=1; tt<=T; ++tt)
	{
		scanf("%d%d", &n, &k);
		for (i=0; i<n; ++i) scanf("%s", s[i]);
		ans=0;
		for (i=0; i<k; ++i) u[i]=0;
		dfs(0);
		printf("Case #%d: %d %d\n", tt, ans, cnt);
	}
	return 0;
}

