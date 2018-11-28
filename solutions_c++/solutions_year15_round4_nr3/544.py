#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>

#define pb push_back
#define mp make_pair
#define LL long long
#define LD long double
#define maxlongint 2147483647

using namespace std;

const int inf = 999999999;
const int mod = 1000000007;
const double eps = 1e-7;

inline int Getint()
{
	char ch = getchar();
	while (ch < '0' || ch > '9') ch = getchar();
	int ret = 0;
	while (ch >= '0' && ch <= '9') ret = ret * 10 + ch - '0', ch = getchar();
	return ret;
}

int T, n;
double VOL, TEMP, v0, t0, v1, t1;

int main()
{
	freopen("123.in", "r", stdin);
	freopen("124.out", "w", stdout);
	T = Getint();
	for (int _ = 1; _ <= T; _++)
	{
		n = Getint(), scanf("%lf%lf", &VOL, &TEMP);
		printf("Case #%d: ", _);
		if (n == 1)
		{
			scanf("%lf%lf", &v0, &t0);
			if (abs(TEMP - t0) < eps) printf("%.10f\n", VOL / v0); else puts("IMPOSSIBLE");
		}
		else if (n == 2)
		{
			scanf("%lf%lf%lf%lf", &v0, &t0, &v1, &t1);
			double ans0 = VOL * (TEMP - t1) / (t0 - t1), ans1 = VOL - ans0;
			//printf("ans0, ans1 = %.10f %.10f\n", ans0, ans1);
			if (ans0 + eps > 0 && ans1 + eps > 0)
			{
				printf("%.10f\n", max(ans0 / v0, ans1 / v1));
			}
			else puts("IMPOSSIBLE");
		}
	}
	return 0;
}
