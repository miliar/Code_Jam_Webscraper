#pragma comment(linker, "/STACK:32000000")
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <stdarg.h>
#include <memory.h>
#include <string.h>

using namespace std;

const double pi = 3.1415926535897932384626433832795;
#define ALL(x) x.begin(), x.end()
typedef long long LL;
#define MP make_pair
#define PB push_back
#define CLR(a,b) memset(a, b, sizeof(a))
template<class T> inline T Sqr(const T &x) { return x*x; }
template<class T> inline T Abs(const T &x) { return x >= 0 ? x : -x; }

void init()
{

}

#define maxn 1005

struct pt3
{
	double x, y, z;
	void read()
	{
		scanf("%lf%lf%lf", &x, &y, &z);
	}
	double dist2(const pt3 &other)
	{
		return Sqr(x - other.x) + Sqr(y - other.y) + Sqr(z - other.z);
	}
};

const double inf = 1e40;

int n, s;
pt3 p0[maxn], vel[maxn];
bool f[maxn];
//double dist[maxn];
double tmin[maxn], tmax[maxn];
int mode[maxn][maxn]; // 0 - can always, 1 = can never, 2 = t1 - t2
double jumpt1[maxn][maxn], jumpt2[maxn][maxn];

inline double get(int i, int j)
{
	return p0[i].dist2(p0[j]);
}


bool go(double maxd)
{
	for (int v = 0; v < n; v++)
		for (int j = 0; j < n; j++)
		{
			 mode[v][j] = 1;
			if (v == j) continue;

			double dx = p0[v].x - p0[j].x;
			double dy = p0[v].y - p0[j].y;
			double dz = p0[v].z - p0[j].z;
			double dvx = vel[v].x - vel[j].x;
			double dvy = vel[v].y - vel[j].y;
			double dvz = vel[v].z - vel[j].z;
			double a = Sqr(dvx) + Sqr(dvy) + Sqr(dvz);

			if (a < 1e-10)
			{
				mode[v][j] = get(v, j) <= maxd * maxd ? 0 : 1;
			}
			else
			{
				double b = 2 * (dx * dvx + dy * dvy + dz * dvz);
				double c = Sqr(dx) + Sqr(dy) + Sqr(dz) - Sqr(maxd);
				double D = b * b - 4 * a * c;
				if (D > 0)
				{
					D = sqrt(D);
					double t1 = (-b + D) / (2 * a);
					double t2 = (-b - D) / (2 * a);
					if (t1 > t2) swap(t1, t2);
					jumpt1[v][j] = t1;
					jumpt2[v][j] = t2;
					mode[v][j] = 2;
				}
			}
		}

	queue<int> q;
	auto push = [&](int v)
	{
		if (f[v]) return;
		f[v] = true;
		q.push(v);
	};
	for (int i = 0; i < n; i++)
	{
		f[i] = false;
		tmin[i] = inf;
		tmax[i] = -inf;
	}
	tmin[0] = 0;
	tmax[0] = s;
	push(0);
	int n_steps = 0;
	while (!q.empty())
	{
		n_steps++;
		if (n_steps > 2000000) return false;
		int v = q.front(); q.pop();
		f[v] = false;
		if (v == 1) return true;
		double a0 = tmin[v], a1 = tmax[v] + s;
		for (int j = 0; j < n; j++) if (mode[v][j] != 1)
		{
			if (mode[v][j] == 0)
			{
				if (a0 < tmin[j])
				{
					tmin[j] = a0;
					push(j);
				}
				if (a1 > tmax[j])
				{
					tmax[j] = a1;
					push(j);
				}
			}
			else
			{
				double b1 = max(a0, jumpt1[v][j]);
				double b2 = min(a1, jumpt2[v][j]);
				if (b1 < b2)
				{
					if (b1 < tmin[j]) { tmin[j] = b1; push(j); }
					if (b2 > tmax[j]) { tmax[j] = b2; push(j); }
				}
			}
		}
	}
	return false;
}

void solvecase()
{
	scanf("%d%d", &n, &s);
	for (int i = 0; i < n; i++)
	{
		p0[i].read();
		vel[i].read();
	}
	double l = 0, r = 2000;
	//double res = 1e9;
	while (r - l > 1e-6)
	{
		double maxd = (l + r) / 2;
		//dijkstra(maxd);
		if (go(maxd))
		{
			r = maxd;
		}
		else
		{
			l = maxd;
		}
	}
	//for (int i = 0; i < n; i++) printf("%.2lf ", dist[i]);
	printf("%.9lf", l);
}

void solve() {
	init();
	int n_tests;
	scanf("%d", &n_tests);
	for (int i = 1; i <= n_tests; i++)
	{
		printf("Case #%d: ", i);
		solvecase();
		printf("\n");
		cerr << i << endl;
	}
}

#define problem_letter "C"
//#define fname "testcpp"
//#define fname problem_letter "-small-attempt0"
//#define fname problem_letter "-small-attempt1"
//#define fname problem_letter "-small-attempt2"
#define fname problem_letter "-large"
//#define fname problem_letter "-small-practice"
//#define fname problem_letter "-large-practice"

int main()
{
	freopen(fname ".in", "r", stdin);
	freopen(fname ".out", "w", stdout);
	solve();
	return 0;
}
