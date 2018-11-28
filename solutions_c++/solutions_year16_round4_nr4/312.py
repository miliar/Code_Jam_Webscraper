#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;
const int N = 35;
char s[N][N];
int a[N], n;
bool v[N];
bool dfs(int x)
{
	if (x == n)
	{
		return 1;
	}
	bool flag = 1;
	int cnt = 0;
	for (int i = 0; i < n; ++ i)
	{
		if (!v[i] && s[a[x]][i] == '1')
		{
			v[i] = 1;
			cnt ++;
			if (!dfs(x + 1))
			{
				flag = 0;
				v[i] = 0;
				break;
			}
			v[i] = 0;
		}
	}
	if (cnt == 0) flag = 0;
	return flag;
}
int main()
{
	int T, zzz = 0;
	scanf("%d", &T);
	while (T --)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; ++ i) scanf("%s", s[i]);
		int ans = n * n;
		for (int m = 0; m < (1 << (n * n)); ++ m)
		{
			int cnt = __builtin_popcount(m);
			bool flag = 0;
			for (int i = 0; i < n; ++ i)
			{
				for (int j = 0; j < n; ++ j)
				{
					if ((m >> (i * n + j) & 1) && s[i][j] == '1')
					{
						flag = 1;
					}
				}
			}
			if (flag) continue;
			for (int i = 0; i < n; ++ i)
			{
				for (int j = 0; j < n; ++ j)
				{
					if (m >> (i * n + j) & 1)
					{
						s[i][j] = '1';
					}
				}
			}
			for (int i = 0; i < n; ++ i) a[i] = i;
			bool check = 1;
			do
			{
				if (!dfs(0))
				{
					check = 0;
					break;
				}
			}
			while (next_permutation(a, a + n));
			if (check) ans = min(ans, cnt);
			for (int i = 0; i < n; ++ i)
			{
				for (int j = 0; j < n; ++ j)
				{
					if (m >> (i * n + j) & 1)
					{
						s[i][j] = '0';
					}
				}
			}
		}
		printf("Case #%d: %d\n", ++ zzz, ans);
	}
}

