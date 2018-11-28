#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <functional>
using namespace std;

#pragma comment(linker,"/STACK:100000000")

vector <pair <int, int> > v;
int a[105][105];
int bad[205];

bool cmp(pair <int, int> p1, pair <int, int> p2)
{
	return a[p1.first][p1.second] > a[p2.first][p2.second];
}

void solve(int t)
{
	int n, m;
	int i, j;
	scanf("%d%d", &n, &m);
	v.clear();
	for (i = 0; i < n; ++i)
		for (j = 0; j < m; ++j)
		{
			scanf("%d", &a[i][j]);
			v.push_back(make_pair(i, j));
		}
	memset(bad, 0xff, sizeof(bad));
	sort(v.begin(), v.end(), cmp);
	printf("Case #%d: ", t);
	for (i = 0; i < v.size(); ++i)
	{
		if (i > 0 && bad[v[i].first] > a[v[i].first][v[i].second] && bad[n + v[i].second] > a[v[i].first][v[i].second])
		{
			printf("NO\n");
			return;
		}
//		printf("%d %d\n", v[i].first, v[i].second);
		bad[v[i].first] = max(bad[v[i].first], a[v[i].first][v[i].second]);
		bad[n + v[i].second] = max(bad[n + v[i].second], a[v[i].first][v[i].second]);
	}
	printf("YES\n");
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int i, T;
	scanf("%d", &T);
	for (i = 0; i < T; ++i)
		solve(i + 1);
	return 0;
}