#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
#include <time.h>
#include <bitset>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#ifdef WIN32
#define dbg(...) {fprintf(stderr, __VA_ARGS__); fflush(stderr);}
#define dbgx(x) {cerr << #x << " = " << x << endl;}
#define dbgv(v) {cerr << #v << " = {"; for (typeof(v.begin()) it = v.begin(); it != v.end(); it ++) cerr << *it << ", "; cerr << "}"; cerr << endl;}
#else
#define dbg(...) { }
#define dbgx(x) { }
#define dbgv(v) { }
#endif

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-10;

void prepare()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

const int nmax = 105;

struct Pipe
{
	double rate, c;
	void read()
	{
		scanf("%lf%lf",&rate,&c);
	}

	bool operator < (const Pipe &oth) const
	{
		return c < oth.c;
	}
};

int n;
double X, V;
double maxC, minC;
Pipe p[nmax];

void read()
{
	scanf("%d%lf%lf",&n,&V,&X);
	maxC = 0;
	minC = INF;
	for (int i = 0; i < n; i ++)
	{
		p[i].read();
		minC = min(minC, p[i].c);
		maxC = max(maxC, p[i].c);
		p[i].c /= V;
	}

	sort(p, p + n);
}

double cap[nmax];

double getMinTemp()
{
	double vLeft = V, resultTemp = 0.0;
	for (int i = 0; i < n; i ++)
	{
		double vDelta = min(cap[i], vLeft);
		resultTemp += vDelta * p[i].c;
		vLeft -= vDelta;
		if (fabs(vLeft) < eps)
			break;
	}
	//assert(fabs(vLeft) < eps);
	return resultTemp;
}

double getMaxTemp()
{
	reverse(p, p + n);
	reverse(cap, cap + n);

	double result = getMinTemp();
	
	reverse(p, p + n);
	reverse(cap, cap + n);

	return result;
}

bool check(double T)
{
	double capSum = 0;
	for (int i = 0; i < n; i ++)
	{
		cap[i] = T * p[i].rate;
		capSum += cap[i];
	}
	if (capSum < V - eps)
	{
		return false;
	}

	double L = getMinTemp();
	double R = getMaxTemp();
	return L - eps <= X && X <= R + eps;
}

bool solve()
{
	if (maxC < X - eps || minC > X + eps)
	{
		printf("IMPOSSIBLE\n");
		return false;
	}

	double l = 0.0, r = INF * 2.0 * 2.0 * 2.0 * 2.0, mid;
	for (int it = 0; it < 1000; it ++)
	{
		mid = (l + r) / 2.0;
		if (check(mid))
			r = mid;
		else
			l = mid;
	}
	printf("%.12lf\n", r);
	return false;
}

int main()
{
	prepare();
	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; i ++)
	{
		dbg("Test %d\n", i);
		printf("Case #%d: ", i + 1);
		read();
		solve();
	}
	return 0;
}
