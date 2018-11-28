#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
#include <numeric>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long long int int64;


struct S
{
	double r, c;
	S() : r(), c() {}
	S(double _r, double _c) : r(_r), c(_c) {}

	S operator + (const S &A) const
	{
		return S(r + A.r, (r * c + A.r * A.c) / (r + A.r) );
	}

	void read()
	{
		scanf("%lf%lf", &r, &c);
	}

	bool operator < (const S &A) const
	{
		return c < A.c;
	}
};


const double eps = 1e-12;
const double inf = 1e18;

bool Eq(double a, double b)
{
	return fabs(a - b) < eps;
}
bool Ls(double a, double b)
{
	return a < b && !Eq(a, b);
}
bool Gr(double a, double b)
{
	return a > b && !Eq(a, b);
}

double getAns(S A, S m, double v, double t)
{
	if (Eq(A.c, t) )
	{
		if (Eq(m.c, t) )
		{
			return v / (A.r + m.r);
		}
		else
			return inf;
	}
	double ra = m.r * (t - m.c) / (A.c - t);
	if (Ls(ra, 0) || Gr(ra, A.r) )
		return inf;
	double r = ra + m.r;
	return v / r;
}

const int maxn = 105;
S s[maxn];

void solve()
{
	int n;
	double v, x;
	scanf("%d%lf%lf", &n, &v, &x);
	for (int i = 0; i < n; i++)
	{
		s[i].read();
	}
	double ans = inf;
	sort(s, s + n);
	for (int i = 0; i < n; i++)
	{
		if (Eq(s[i].c, x) )
			ans = min(ans, v / s[i].r);
		S mid = S();
		for (int j = i + 1; j < n; j++)
		{
			ans = min(ans, getAns(s[i], mid + s[j], v, x) );
			ans = min(ans, getAns(s[j], mid + s[i], v, x) );
			mid = mid + s[j];
		}
	}
	if (ans > inf / 2.)
		printf("IMPOSSIBLE\n");
	else
		printf("%.9lf\n", ans);
}

void multitest()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		printf("Case #%d: ", i);
		eprintf("Case #%d .. %d\n", i, n);
		solve();
	}


}

int main(int argc, char **)
{
	if (argc == 1)
		multitest();
	else
		solve();

	return 0;
}


