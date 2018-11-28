#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <map>
#include <vector>
using namespace std;
struct Node
{
	map<char, int> mp;
};
vector<Node> v;
int ans1, ans2;
int t, m, n, a[10], x[10];
char s[10][20];

int getTrie(int k)
{
	v.clear();
	Node tmp;
	tmp.mp.clear();
	v.push_back(tmp);
	for (int i = 1; i <= m; i++)
		if (a[i] == k)
		{
			int z = 0, len = strlen(s[i]);
			for (int j = 0; j < len; j++)
			{
				if (v[z].mp.find(s[i][j]) == v[z].mp.end())
				{
					v[z].mp[s[i][j]] = v.size();
					v.push_back(tmp);
				}
				z = v[z].mp[s[i][j]];
			}
		}
	return v.size();
}

void dfs(int k)
{
	if (k > m)
	{
		for (int i = 1; i <= n; i++)
			if (x[i] == 0) return;
		int ret = 0;
		for (int i = 1; i <= n; i++)
			ret += getTrie(i);
		if (ret > ans1)
		{
			ans1 = ret;
			ans2 = 1;
		}
		else if (ret == ans1)
			ans2++;
		return;
	}
	for (int i = 1; i <= n; i++)
	{
		a[k] = i;
		x[i]++;
		dfs(k + 1);
		x[i]--;
	}
}

int main()
{
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		memset(x, 0, sizeof(x));
		scanf("%d%d", &m, &n);
		for (int i = 1; i <= m; i++)
			scanf("%s", s[i]);
		ans1 = -1;
		ans2 = 0;
		dfs(1);
		printf("Case #%d: %d %d\n", tt, ans1, ans2);
	}
	return 0;
}
