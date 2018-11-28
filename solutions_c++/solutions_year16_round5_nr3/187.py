#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <utility>
#include <ctime>
#include <string>
#include <sstream>
#include <queue>
#include <cstring>
#include <functional>

using namespace std;
typedef long long ll;
typedef long double ld;
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))
#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))

struct point
{
	double x, y, z;
	point(double x, double y, double z) : x(x), y(y), z(z) {}
	point() {}
	void get()
	{
		cin >> x >> y >> z;
		int u;
		cin >> u;
		cin >> u;
		cin >> u;
	}
};

double dst(point a, point b)
{
	return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y) + (a.z - b.z) * (a.z - b.z));
}

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int te;
	cin >> te;
	for (int q = 0; q < te; q++)
	{
		int n;
		cin >> n;
		int s;
		cin >> s;

		vector<point> v(n);
		for (int i = 0; i < n; i++) v[i].get();

		double l = 0, r = 1e9;

		for (int w = 0; w < 800; w++)
		{
			double m = (l + r) / 2;

			queue<int> q;
			vector<char> was(n);

			for (int i = 0; i < n; i++) was[i] = 0;
			
			q.push(0);
			was[0] = 1;

			while (!q.empty())
			{
				int i = q.front();
				q.pop();
				for (int j = 0; j < n; j++)
				{
					if (was[j]) continue;
					if (dst(v[i], v[j]) <= m)
					{
						was[j] = 1;
						q.push(j);
					}
				}
			}

			if (was[1])
			{
				r = m;
			}
			else
			{
				l = m;
			}
		}

		printf("Case #%d: ", q + 1);

		printf("%.9lf\n", l);
	}

	return 0;
}