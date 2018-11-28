#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <sstream>
#include <fstream>
#include <functional>
#include <cassert>
#include <complex>
#include <valarray>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long long ll;
typedef pair<int, int> pii;
#define X first
#define Y second
#define mp make_pair

typedef long double ld;

const ld eps = 1e-10;
const ld INF = 1e20;

bool Eq(ld a, ld b)
{
	return fabsl(a - b) < eps;
}

bool Ls(ld a, ld b)
{
	return a < b && !Eq(a, b);
}

bool LsEq(ld a, ld b)
{
	return a < b || Eq(a, b);
}

ld mySqrt(ld a)
{
	if (a < 0)
		return 0;
	return sqrtl(a);
}

struct Point
{
	ld x, y, z;
	Point () : x(), y(), z() {}
	Point (ld _x, ld _y, ld _z) : x(_x), y(_y), z(_z) {}
	Point operator + (const Point &a) const
	{
		return Point(x + a.x, y + a.y, z + a.z);
	}
	Point operator - (const Point &a) const
	{
		return Point(x - a.x, y - a.y, z - a.z);
	}
	Point operator * (ld k) const
	{
		return Point(x * k, y * k, z * k);
	}
	Point operator / (ld k) const
	{
		return Point(x / k, y / k, z / k);
	}
	ld operator % (const Point &a) const
	{
		return x * a.x + y * a.y + z * a.z;
	}
	ld length()
	{
		return mySqrt(*this % *this);
	}
	void scan()
	{
		scanf("%Lf %Lf %Lf", &x, &y, &z);
	}
	void print()
	{
		printf("%Lf %Lf %Lf\n", x, y, z);
	}
};

const int N = (int)1e5 + 10;

Point p[N];
Point V[N];
int n;
ld S;

void read()
{
	scanf("%d%Lf", &n, &S);
	for (int i = 0; i < n; i++)
	{
		p[i].scan();
		V[i].scan();
	}
}

bool used[N];

bool dfs(int v, ld r)
{
	if (v == 1)
		return true;
	if (used[v])
		return false;
	used[v] = true;
	for (int i = 0; i < n; i++)
	{
		ld dist = (p[i] - p[v]).length();
		if (dist <= r)
		{
			if (dfs(i, r))
				return true;
		}
	}
	return false;
}

bool check(ld r)
{
	fill(used, used + n, 0);
	return dfs(0, r);
}

void solve()
{
	ld l = 0, r = INF;
	int IT = 300;
	for (int i = 0; i < IT; i++)
	{
		ld mid = (l + r) / 2;
		if (check(mid))
			r = mid;
		else
			l = mid;
	}
	printf("%.10Lf\n", r);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d: ", i + 1);
		read();
		solve();
	}
	return 0;
}
