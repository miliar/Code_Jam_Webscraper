#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
char in[30];
bool map[25][25];
int n;
bool v[25];
int perm[25];
bool chk(int next)
{
	if (next == n) return true;
	int i = perm[next];
	bool ans = false;
	for (int j = 0; j < n; j++)
	{
		if (map[i][j] && !v[j])
		{
			v[j] = true;
			ans = true;
			if (!chk(next + 1))return false;
			v[j] = false;
		}
	}
	return ans;
}

bool solve(int p, int x, int y)
{
	if (!p)
	{
		bool ans = true;
		for (int i = 0; i < n; i++) perm[i] = i;
		do
		{
			for (int i = 0; i < n; i++) v[i] = false;
			ans &= chk(0);
		} while (next_permutation(perm, perm + n));
		return ans;
	}
	bool ret = false;
	for (; y < n; y++)
	{
		for (; x < n; x++)
		{
			if (map[y][x]) continue;
			map[y][x] = true;
			ret |= solve(p - 1, x, y);
			map[y][x] = false;
		}
		x = 0;
	}
	return ret;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d", &n);
		int c = 0;
		for (int i = 0; i < n; i++)
		{
			scanf("%s", in);
			for (int j = 0; j < n; j++)
			{
				map[i][j] = in[j] == '1';
				if (map[i][j])c++;
			}
		}
		int r = n*n - c;
		int ans = r;
		for (int i = r - 1; i >= 0; i--)
		{
			if (solve(i, 0, 0))
			{
				ans = i;
			}
		}
		
		printf("Case #%d: %d\n",t, ans);
	}
}