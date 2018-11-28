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

int n, m, j, i, h, k, t, q1, q2, q, ans;
double v0, x0, v[101], x[101];

void solve()
{
	scanf ("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		scanf ("%d%lf%lf\n", &n, &v0, &x0);
		for (j = 1; j <= n; j++)
		{
			scanf ("%lf%lf", &v[j], &x[j]);
		}
		if (n == 1)
		{
			if (abs(x[1] - x0) > 1e-8)
			{
				printf ("Case #%d: IMPOSSIBLE\n", tt);
			}
			else
			{
				printf ("Case #%d: %.10lf\n", tt, v0 / v[1]);
			}
		}
		else
		{
			if (max(x[1], x[2]) + 1e-8 < x0 || min(x[1], x[2]) - 1e-8 > x0)
			{
				printf ("Case #%d: IMPOSSIBLE\n", tt);
				continue;
			}
			if (abs(x0 - x[1]) < 1e-8 || abs(x0 - x[2]) < 1e-8)
			{
				if (abs(x0 - x[1]) > 1e-8)
				{
					swap(x[1], x[2]);
					swap(v[1], v[2]);
				}
				if (abs(x[1] - x[2]) < 1e-8)
				{
					v[1] += v[2];
				}
				printf ("Case #%d: %.10lf\n", tt, v0 / v[1]);
			}
			else
			{
				if (x[1] > x[2])
				{
					swap(x[1], x[2]);
					swap(v[1], v[2]);
				}
				double b = v0 / ((x[2] - x0) / (x0 - x[1]) + 1.0);
				double a = v0 - b;
				printf ("Case #%d: %.10lf\n", tt, max(a / v[1], b / v[2]));
			}
		}
	}
}

int main()
{
	ios_base::sync_with_stdio(false);cin.tie(0);
	freopen("B-small-attempt1.in", "rt", stdin); freopen("output.txt", "wt", stdout);
	srand(3333);
	solve();
	return 0;
}