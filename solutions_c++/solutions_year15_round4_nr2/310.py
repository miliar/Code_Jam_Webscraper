#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <cmath>

using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long double ld;

const int IT = 1000;
const int N = (int)1e4 + 10;
const ld INF = 1e8;
const ld eps = 1e-15;

int n;
ld V, X;
ld R[N], C[N];
ld maxV[N];
ld curV[N];
int perm[N];

bool Eq(ld a, ld b)
{
	return fabs(a - b) < eps;
}

bool Ls(ld a, ld b)
{
	return a < b && !Eq(a, b);
}

bool LsEq(ld a, ld b)
{
	return a < b || Eq(a, b);
}

bool Gr(ld a, ld b)
{
	return a > b && !Eq(a, b);
}

bool GrEq(ld a, ld b)
{
	return a > b || Eq(a, b);
}

bool cmp(int a, int b)
{
	return fabsl((C[a] - X)) > fabsl((C[b] - X));
}

bool check(ld tme)
{
	for (int i = 0; i < n; i++)
		maxV[i] = R[i] * tme;
	ld delta = 0;
	for (int i = 0; i < n; i++)
	{
		ld d = C[i] - X;
		delta += d * maxV[i];
		perm[i] = i;
		curV[i] = maxV[i];
	}
	sort(perm, perm + n, cmp);
	for (int i = 0; i < n; i++)
	{
		int p = perm[i];
		ld d = C[p] - X;
		if (Ls(delta, 0) && Ls(d, 0))
		{
			ld dv = maxV[p];
			dv = min(dv, delta / d);
			curV[p] -= dv;
			delta -= d * dv;
		}
		else if (Gr(delta, 0) && Gr(d, 0))
		{
			ld dv = maxV[p];
			dv = min(dv, delta / d);
			curV[p] -= dv;
			delta -= d * dv;
		}
	}
	if (!Eq(delta, 0))
		return false;
	ld vol = 0;
	for (int i = 0; i < n; i++)
		vol += curV[i];
	return GrEq(vol, V);
}

bool simpleCheck(double tme)
{
	if (n == 1)
	{
		ld t1 = V / R[0];
		ld x1 = C[0];
		return Eq(x1, X) && GrEq(tme, t1);
	}
	ld d1 = C[0] - X;
	ld d2 = C[1] - X;
	if (Eq(d1, 0) && Eq(d2, 0))
	{
		ld t1 = V / (R[0] + R[1]);
		return GrEq(tme, t1);
	}
	else if (Eq(d1, 0))
	{
		ld t1 = V / R[0];
		return GrEq(tme, t1);
	}
	else if (Eq(d2, 0))
	{
		ld t1 = V / R[1];
		return GrEq(tme, t1);
	}
	else
	{
		if (Ls(d1, 0) && Ls(d2, 0))
			return false;
		if (Gr(d1, 0) && Gr(d2, 0))
			return false;
		ld rate10 = -d1 / d2;
		ld v0 = V / (1 + rate10);
		ld v1 = v0 * rate10;
		return LsEq(v0, R[0] * tme) && LsEq(v1, R[1] * tme);
	}
}

void solve()
{
	double _V, _X;
	scanf("%d%lf%lf", &n, &_V, &_X);
	V = _V, X = _X;
	for (int i = 0; i < n; i++)
	{
		double _R, _C;
		scanf("%lf%lf", &_R, &_C);
		R[i] = _R;
		C[i] = _C;
	}
	ld l = 0, r = INF;
	for (int it = 0; it < IT; it++)
	{
		ld m = (l + r) / 2;

		if ((n <= 2 && simpleCheck(m)) || check(m))
		{
			r = m;
		}
		else
			l = m;
	}
	if (r > INF / 2)
		puts("IMPOSSIBLE");
	else
		printf("%.10lf\n", (double)r);
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
