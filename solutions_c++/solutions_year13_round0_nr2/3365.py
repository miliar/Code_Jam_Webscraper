#include <iostream>
#include <cstdio>
#include <utility>
#include <algorithm>
using namespace std;
const int maxn = 110, maxs = 10010;

int n, m;
int dat[maxn][maxn];
pair<int, int> sorted[maxs];
int row[maxn], col[maxn];

void init()
{
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			scanf("%d", &dat[i][j]);
}

bool work()
{
	for (int i = 0; i < n; i++) row[i] = m;
	for (int i = 0; i < m; i++) col[i] = n;
	int scnt = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			sorted[scnt++] = make_pair(dat[i][j], i * m + j);
	sort(sorted, sorted + scnt);
	
	static pair<int, int> now[maxs];
	int cnt = 0;
	for (int i = 0; i < scnt; i++)
	{
		now[cnt++] = make_pair(sorted[i].second / m, sorted[i].second % m);
		row[now[cnt - 1].first]--; col[now[cnt - 1].second]--;
		if (i + 1 >= scnt || sorted[i].first != sorted[i + 1].first)
		{
			for (int j = 0; j < cnt; j++) if (row[now[j].first] && col[now[j].second]) return false;
			cnt = 0;
		}
	}
	
	return true;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		init();
		printf("Case #%d: ", i);
		if (work()) printf("YES\n"); else printf("NO\n");
	}
	return 0;
}
