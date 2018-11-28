#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cstdio>
#include<numeric>
#include<cstring>
#include<ctime>
#include<cstdlib>
#include<set>
#include<map>
#include<unordered_map>
#include<unordered_set>
#include<list>
#include<cmath>
#include<bitset>
#include<cassert>
#include<queue>
#include<stack>
#include<deque>
#include<cassert>
using namespace std;
typedef long long ll;
typedef long double ld;
char tmp[7];
int a[7][7];
int cur[7][7];
int cnt[7];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		cerr << tt << endl;
		int n;
		scanf("%d\n", &n);
		for (int i = 1; i <= n; i++)
		{
			scanf("%s", tmp);
			for (int j = 1; j <= n; j++)
			{
				if (tmp[j - 1] == '1')
				{
					a[i][j] = 1;
				}
				else
				{
					a[i][j] = 0;
				}
			}
		}
		int res = n*n + 7;
		for (int mask = 0; mask < (1 << (n*n)); mask++)
		{
			bool ok = true;
			int cost = 0;
			int tmp = mask;
			for (int i = 1; i <= n; i++)
			{
				for (int j = 1; j <= n; j++)
				{
					cur[i][j] = tmp % 2;
					tmp /= 2;
					if (a[i][j] == 1 && cur[i][j] == 0) ok = false;
					if (a[i][j] == 0 && cur[i][j] == 1) cost++;
				}
			}
			for (int i = 1; i <= n; i++)
			{
				cnt[i] = 0;
			}
			for (int i = 1; i <= n; i++)
			{
				for (int j = 1; j <= n; j++)
				{
					cnt[i] += cur[i][j];
				}
			}
			for (int i = 1; i <= n; i++)
			{
				if (cnt[i] == 0)
				{
					ok = false;
				}
			}
			for (int i = 1; i <= n; i++)
			{
				if (cnt[i] == 1)
				{
					int x = 0;
					for (int j = 1; j <= n; j++)
					{
						if (cur[i][j])
						{
							x = j;
						}
					}
					for (int j = 1; j <= n; j++)
					{
						if (i != j && cur[j][x]) ok = false;
					}
				}
			}
			for (int i = 1; i <= n; i++)
			{
				if (cnt[i] == 2)
				{
					int x = 0, y = 0;
					for (int j = 1; j <= n; j++)
					{
						if (cur[i][j])
						{
							if (x == 0)
							{
								x = j;
							}
							else
							{
								y = j;
							}
						}
					}
					for (int a = 1; a <= n; a++)
					{
						if (a == i) continue;
						for (int b = 1; b <= n; b++)
						{
							if (b == a || b == i) continue;
							if (cur[a][x] && cur[b][y]) ok = false;
						}
					}
				}
			}
			for (int i = 1; i <= n; i++)
			{
				if (cnt[i] == 3)
				{
					int x = 0, y = 0, z = 0;
					for (int j = 1; j <= n; j++)
					{
						if (cur[i][j])
						{
							if (x == 0)
							{
								x = j;
							}
							else if (y == 0)
							{
								y = j;
							}
							else
							{
								z = j;
							}
						}
					}
					for (int a = 1; a <= n; a++)
					{
						if (a == i) continue;
						for (int b = 1; b <= n; b++)
						{
							if (b == i || b == a) continue;
							for (int c = 1; c <= n; c++)
							{
								if (a == c || b == c || i == c) continue;
								if (cur[a][x] && cur[b][y] && cur[c][z]) ok = false;
							}
						}
					}
				}
			}
			if (ok)
			{
				res = min(res, cost);
			}
		}
		printf("Case #%d: %d\n", tt, res);
	}
}
