#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

#define maxn 1010100
#define maxe 202020

int n, r, p, s;

int a[maxn];

string dfs(int idx, int val, int d)
{
	if (d == n)
	{
		a[idx] = val;
		if (val == 0) return "R";
		if (val == 1) return "P";
		if (val == 2) return "S";
	}

	string s1 = dfs(idx * 2, val, d + 1);
	string s2 = dfs(idx * 2 + 1, (val + 1) % 3, d + 1);
	if (s1<s2) return s1 + s2;
	return s2 + s1;
}

int check(string ans)
{
	int rr = 0, pp = 0, ss = 0;
	for (int i = 0; i<ans.size(); i++)
	{
		if (ans[i] == 'R')
			rr++;
		else if (ans[i] == 'P')
			pp++;
		else
			ss++;
	}
	if (rr == r && pp == p && ss == s)
		return 1;
	return 0;
}

int main()
{
	int i, j, tt = 0, ncase;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &ncase);
	while (ncase--)
	{
		scanf("%d %d %d %d", &n, &r, &p, &s);

		memset(a, 0, sizeof(a));

		printf("Case #%d: ", ++tt);
		for (j = 0; j<3; j++)
		{
			string ans = dfs(0, j, 0);
			if (check(ans))
			{
				printf("%s\n", ans.c_str());
				break;
			}
		}
		if (j == 3)
			puts("IMPOSSIBLE");
	}
	return 0;
}
