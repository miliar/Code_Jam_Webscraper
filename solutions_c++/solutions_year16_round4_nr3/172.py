#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;
int T, n, m;
struct rec { 
	int x, y, z;
	rec() {}
	rec(int _x, int _y, int _z) { x = _x, y = _y, z = _z; }
}a[210];
vector<pair<int, int>> ver[250][250];
vector<rec> edge[250][250];
pair<int, int> st[500], ed[500];
int ans[110][110];

bool operator <(rec a, rec b)
{
	return a.z < b.z || a.z == b.z && a.x < b.x;
}

void add(int ax, int ay, int bx, int by, int i, int j, int k)
{
	ver[ax][ay].push_back(make_pair(bx, by));
	edge[ax][ay].push_back(rec(i, j, k));
	ver[bx][by].push_back(make_pair(ax, ay));
	edge[bx][by].push_back(rec(i, j, k));
}

bool able(int sx, int sy, int dx, int dy)
{
	for (int i = 0; i < ver[sx][sy].size(); i++)
	{
		int x = ver[sx][sy][i].first, y = ver[sx][sy][i].second;
		if (x == sx + dx && y == sy + dy)
		{
			int p = edge[sx][sy][i].x, q = edge[sx][sy][i].y;
			if (ans[p][q] == 0 || ans[p][q] == edge[sx][sy][i].z)
			{
				ans[p][q] = edge[sx][sy][i].z;
				return true;
			}
		}
	}
	return false;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	cin >> T;
	for (int C = 1; C <= T; C++)
	{
		cin >> n >> m;
		for (int i = 1; i <= n + m; i++)
		{
			int x, y;
			cin >> x >> y;
			if (x > y) swap(x, y);
			a[i].x = x, a[i].y = y, a[i].z = y - x;
		}
		sort(a + 1, a + n + m + 1);
		for (int i = 0; i <= 2 * n; i++)
			for (int j = 0; j <= 2 * m; j++)
			{
				ver[i][j].clear();
				edge[i][j].clear();
			}
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
			{
				int x = (i - 1) * 2, y = j * 2 - 1;
				add(x, y, x + 1, y + 1, i, j, 1);
				add(x, y, x + 1, y - 1, i, j, 2);
				x++, y--;
				add(x, y, x + 1, y + 1, i, j, 1);
				x++, y++;
				add(x, y, x - 1, y + 1, i, j, 2);
			}
		int tot = 0;
		for (int i = 1; i <= m; i++)
			st[++tot] = make_pair(0, 2 * i - 1), ed[tot] = make_pair(-1, 1);
		for (int i = 1; i <= n; i++)
			st[++tot] = make_pair(2 * i - 1, 2 * m), ed[tot] = make_pair(1, 1);
		for (int i = m; i; i--)
			st[++tot] = make_pair(2 * n, 2 * i - 1), ed[tot] = make_pair(1, -1);
		for (int i = n; i; i--)
			st[++tot] = make_pair(2 * i - 1, 0), ed[tot] = make_pair(-1, -1);
		memset(ans, 0, sizeof(ans));
		bool sol = true;
		for (int i = 1; i <= n + m; i++)
		{
			pair<int,int> now = st[a[i].x], dir = ed[a[i].x];
			while (now != st[a[i].y])
			{
				pair<int, int> nd = make_pair(dir.second, -dir.first);
				bool go = false;
				for (int j = 0; j < 3; j++)
				{
					if (able(now.first, now.second, nd.first, nd.second))
					{
						now.first += nd.first;
						now.second += nd.second;
						go = true;
						dir = make_pair(-nd.first, -nd.second);
						break;
					}
					nd = make_pair(nd.second, -nd.first);
				}
				if (!go) { sol = false; break; }
			}
		}
		printf("Case #%d:\n", C);
		if (!sol) puts("IMPOSSIBLE");
		else {
			for (int i = 1; i <= n; i++)
			{
				for (int j = 1; j <= m; j++)
					putchar(ans[i][j] == 1 ? '\\' : '/');
				puts("");
			}
		}
	}
}