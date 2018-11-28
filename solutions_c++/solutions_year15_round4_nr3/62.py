#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<map>
#include<string>
#include<vector>
using namespace std;
const int inf = 0x3fffffff, u = 5010, w = 200010, c = 100;
int head[u], ver[w], edge[w], Next[w], q[u], d[u];
int NUM, T, n, m, s, t, tot, maxflow, Eng, Fre;
char str[1010][12];
map<string, int> h;
bool eng[u], fre[u];
vector<pair<int, int>> same;

void add(int x, int y, int z)
{
	ver[++tot] = y; edge[tot] = z; Next[tot] = head[x]; head[x] = tot;
	ver[++tot] = x; edge[tot] = 0; Next[tot] = head[y]; head[y] = tot;
}

bool bfs()
{
	memset(d, 0, sizeof(d));
	int l, r, i;
	l = r = 1; q[1] = s; d[s] = 1;
	while (l <= r)
	{
		for (i = head[q[l]];i;i = Next[i])
			if (edge[i] && !d[ver[i]])
			{
				q[++r] = ver[i];
				d[ver[i]] = d[q[l]] + 1;
				if (ver[i] == t) return 1;
			}
		l++;
	}
	return 0;
}

int dinic(int x, int f)
{
	if (x == t) return f;
	int temp = f, k, i;
	for (i = head[x];i;i = Next[i])
		if (edge[i] && temp&&d[ver[i]] == d[x] + 1)
		{
			k = dinic(ver[i], min(temp, edge[i]));
			if (!k) d[ver[i]] = 0;
			edge[i] -= k;
			edge[i ^ 1] += k;
			temp -= k;
		}
	return f - temp;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	cin >> NUM;
	for (int T = 1;T <= NUM;T++)
	{
		cin >> n;
		same.clear(); h.clear(); m = 0;
		memset(eng, 0, sizeof(eng));
		memset(fre, 0, sizeof(fre));
		for (int i = 1;i <= n;i++)
		{
			int cnt = 0;
			do {
				scanf("%s", str[++cnt]);
				if (!h[str[cnt]]) h[str[cnt]] = ++m;
				if (i == 1) eng[h[str[cnt]]] = 1;
				if (i == 2) fre[h[str[cnt]]] = 1;
			} while (getchar() == ' ');
			if (i > 2)
			{
				for (int i = 1;i < cnt;i++)
					for (int j = i + 1;j <= cnt;j++)
						same.push_back(make_pair(h[str[i]], h[str[j]]));
			}
		}
		s = 0; t = 2 * m + 1; tot = 1;
		memset(head, 0, sizeof(head));
		for (int i = 1;i <= m;i++)
		{
			add(s, i, fre[i] ? inf : c);
			add(i, m + i, c + 1);
			add(m + i, t, eng[i] ? inf : c);
		}
		for (int i = 0;i < same.size();i++)
		{
			int x = same[i].first, y = same[i].second;
			add(m + x, y, inf), add(m + y, x, inf);
		}
		int i;
		maxflow = 0;
		while (bfs())
			while (i = dinic(s, inf)) maxflow += i;
		printf("Case #%d: ", T);
		cout << maxflow - c*m << endl;
	}
	return 0;
}