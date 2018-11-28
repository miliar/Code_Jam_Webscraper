#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

struct node
{
	char x;
	int a[27];
};
struct trie
{
	node a[105];
	int size;
	void clear()
	{
		memset(a[0].a, 0, sizeof a[0].a);
		size = 1;
	}
	void add (char* s)
	{
		int l = strlen(s);
		int now = 0;
		for (int i = 0; i < l; i++)
		{
			int x = s[i] - 'A';
			if (a[now].a[x] == 0)
			{
				a[now].a[x] = size;
				memset(a[size].a, 0, sizeof a[size].a);
				size++;
			}
			now = a[now].a[x];
		}
	}
} tr[5];

char s[10][12];
int n, m, f[110];
int ans, way;

int doit()
{
	int x[5] = {0};
	for (int i = 0; i < m; i++)
	{
		x[f[i]]++;
	}
	for (int i = 0; i < n; i++)
	{
		if (x[i] == 0) return -100;
	}
	for (int i = 0; i < n; i++)
	{
		tr[i].clear();
	}
	for (int i = 0; i < m; i++)
	{
		tr[f[i]].add(s[i]);
	}
	int size = 0;
	for (int i = 0; i < n; i++)
	{
		size += tr[i].size;
	}
	return size;
}

void dfs (int now)
{
	if (now == m)
	{
		int tt = doit();
		if (tt > ans) ans = tt, way = 1;
		else if (tt == ans) ++way;
	}
	else
	{
		for (int i = 0; i < n; i++)
		{
			f[now] = i;
			dfs(now + 1);
		}
	}
}

int main()
{
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	
	int T; scanf("%d", &T);
	for (int kase = 1; kase <= T; kase++)
	{
		scanf("%d %d", &m, &n);
		for (int i = 0; i < m; i++)
		{
			scanf("%s", s[i]);
		}
		ans = 0; way = 0;
		dfs(0);
		printf("Case #%d: %d %d\n", kase, ans, way);
	}
}
