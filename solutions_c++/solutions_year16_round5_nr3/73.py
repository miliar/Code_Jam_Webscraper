#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

const int N = 1010;

struct Point
{
	double x, y, z;

	Point() : x(), y(), z() {}
	Point(double _x, double _y, double _z) : x(_x), y(_y), z(_z) {}

	void scan()
	{
		scanf("%lf%lf%lf", &x, &y, &z);
	}

	Point operator - (const Point &a) const
	{
		return Point(x - a.x, y - a.y, z - a.z);
	}
	double len() const
	{
		return sqrt(x * x + y * y + z * z);
	}
	double distTo(const Point &a) const
	{
		return (*this - a).len();
	}
};

const double INF = 1e4;
int n;
Point p[N];
Point vel[N];
double dist[N];
bool used[N];
double S;

double solve()
{
	scanf("%d%lf", &n, &S);
	for (int i = 0; i < n; i++)
	{
		p[i].scan();
		vel[i].scan();
	}
	for (int i = 0; i < n; i++)
	{
		used[i] = 0;
		dist[i] = INF;
	}
	dist[0] = 0;
	while(!used[1])
	{
		int v = -1;
		for (int i = 0; i < n; i++)
		{
			if (used[i]) continue;
			if (v == -1 || dist[v] > dist[i])
				v = i;
		}
		used[v] = 1;
		for (int u = 0; u < n; u++)
		{
			if (used[u]) continue;
			dist[u] = min(dist[u], max(dist[v], p[v].distTo(p[u])));
		}
	}
	return dist[1];
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: %.13lf\n", i, solve());
	}

	return 0;
}