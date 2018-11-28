#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <utility>
#include <algorithm>
#include <memory.h>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>

using namespace std;

#pragma comment (linker, "/STACK:64000000")

#define pb push_back
#define pii pair<int, int>
#define pdi pair<double, int>
#define pdii pair<pdi, int>
#define pll pair<ll, ll>
#define pib pair<int, bool>
#define pli pair<ll, int>
#define pil pair<int, ll>
#define vi vector<int>
#define inf 2000000000
#define mod 1000000007
#define mod2 536870911
#define y1 uhgeg
#define eps 1e-9
#define prime 3001
#define N 200005
#define clean(mas) memset(mas, 0, sizeof(mas))

typedef long long ll;
typedef unsigned long long ull;

int n, m, j, i, h, k, t, q1, q2, q, ans, s1[105][105], s2[105][105];
char buf[105][105];
string s[105];
bool imp;

void solve()
{
	scanf ("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		if (tt > 1)
		{
			clean(s1);
			clean(s2);
		}
		scanf ("%d %d\n", &n, &m);
		for (j = 1; j <= n; j++)
		{
			scanf ("%s\n", &buf[j]);
			s[j] = " ";
			s[j] += buf[j];
		}
		for (j = 1; j <= n; j++)
		{
			for (i = 1; i <= m; i++)
			{
				s1[j][i] = s1[j][i - 1];
				s2[i][j] = s2[i][j - 1];
				if (s[j][i] != '.')
				{
					s1[j][i]++;
					s2[i][j]++;
				}
			}
		}
		imp = 0;
		for (j = 1; j <= n && !imp; j++)
		{
			for (i = 1; i <= m && !imp; i++)
			{
				if (s[j][i] != '.')
				{
					if (!s1[j][i - 1] && !(s1[j][m] - s1[j][i]) && !s2[i][j - 1] && !(s2[i][n] - s2[i][j]))
					{
						imp = 1;
					}
				}
			}
		}
		if (imp)
		{
			printf ("Case #%d: IMPOSSIBLE\n", tt);
			continue;
		}
		ans = 0;
		for (j = 1; j <= n; j++)
		{
			for (i = 1; i <= m; i++)
			{
				if (s[j][i] == '^' && !s2[i][j - 1])
				{
					ans++;
				}
				if (s[j][i] == 'v' && !(s2[i][n] - s2[i][j]))
				{
					ans++;
				}
				if (s[j][i] == '<' && !s1[j][i - 1])
				{
					ans++;
				}
				if (s[j][i] == '>' && !(s1[j][m] - s1[j][i]))
				{
					ans++;
				}
			}
		}
		printf ("Case #%d: %d\n", tt, ans);
	}
}

int main()
{
	ios_base::sync_with_stdio(false);cin.tie(0);
	freopen("A-large.in", "rt", stdin); freopen("output.txt", "wt", stdout);
	srand(3333);
	solve();
	return 0;
}