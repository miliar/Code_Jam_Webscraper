#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;
const int nmax = 100 + 18, times = 300;
const long double inf = 1e10, EPS = 1e-10;

long double R[nmax], C[nmax], V, X;
int n, p[nmax];

int sgn(long double x)
{
	return x < -EPS ? -1 : x > EPS;
}

bool check(long double t)
{
	long double bot, botv, top, topv;
	bot = botv = top = topv = 0;
	for (int i = 1; i <= n && sgn(botv - V) < 0; ++i) {
		long double maxv = min(V - botv, t * R[p[i]]);
		bot = (bot * botv + maxv * C[p[i]]) / (botv + maxv);
		botv += maxv;
	}
	for (int i = n; i >= 1 && sgn(topv - V) < 0; --i) {
		long double maxv = min(V - topv, t * R[p[i]]);
		top = (top * topv + maxv * C[p[i]]) / (topv + maxv);
		topv += maxv;
	}
//	printf("%.5f %.5f:%.5f %.5f:%.5f\n", (double)t, (double)bot, (double)botv, (double)top, (double)botv);
	return sgn(bot - X) <= 0 && sgn(top - X) >= 0 && sgn(botv - V) == 0 && sgn(topv - V) == 0;
}

bool cmper(int i, int j)
{
	return C[i] < C[j];
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++cases) {
		cin >> n >> V >> X;
		printf("Case #%d: ", cases);
		for (int i = 1; i <= n; ++i) {
			cin >> R[i] >> C[i];
			p[i] = i;
		}
		sort(p + 1, p + n + 1, cmper);
		int up = 0, down = 0, mi = 0;
		for (int i = 1; i <= n; ++i)
			if (sgn(C[i] - X) > 0)
				up = 1;
			else
				if (sgn(C[i] - X) < 0)
					down = 1;
				else
					mi = 1;
		if (!mi && ((up && !down) || (!up && down))) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		long double l = 0, r = inf, mid;
		for (int i = 1; i < times; ++i)
			if (check(mid = (l + r) / 2))
				r = mid;
			else
				l = mid;
		printf("%.10f\n", (double)mid);
	}
	return 0;
}
