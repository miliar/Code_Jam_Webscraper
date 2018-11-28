#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int l, x, n;
char s[10101];

int mat[4][4] =
{
	{0, 1, 2, 3},
	{1, 0, 3, 2},
	{2, 3, 0, 1},
	{3, 2, 1, 0}
};

int sg[4][4] =
{
	{0, 0, 0, 0},
	{0, 1, 0, 1},
	{0, 1, 1, 0},
	{0, 0, 1, 1}
};

int dp[10101][4][2][3];

inline int test(int i, int cur, int sign, int k)
{
	if (k > 2) return 0;
	if (i == n) return (cur == k + 1 && k == 2 && sign == 0);
	int &ret = dp[i][cur][sign][k];
	if (ret != -1) return ret;
	ret = 0;
	if (cur == k + 1 && sign == 0)
		ret |= test(i, 0, 0, k + 1);
	ret |= test(i + 1, mat[cur][s[i] - 'h'], sign ^ sg[cur][s[i] - 'h'], k);
	return ret;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc)
	{
		scanf("%d %d", &l, &x);
		scanf("%s", s);
		n = l * x;
		for (int i = 1; i < x; i++)
		{
			int p = i * l;
			for (int j = 0; j < l; ++j)
				s[p + j] = s[j];
		}
		memset(dp, -1, sizeof dp);
		printf("Case #%d: %s\n", tc, test(0, 0, 0, 0) ? "YES" : "NO");
	}
	return 0;
}