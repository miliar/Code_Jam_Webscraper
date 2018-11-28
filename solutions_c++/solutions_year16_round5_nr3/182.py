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
#include <stack>

using namespace std;
typedef long long ll;
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))
#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))

// template end

struct point
{
	int x, y, z;
	void scan()
	{
		cin >> x >> y >> z;
	}

	double dstto(const point& a) const
	{
		return this->minus(a).len();
	}

	point minus(const point& a) const
	{
		return point { x - a.x, y - a.y, z - a.z };
	}

	double len() const
	{
		return pow(x*x + y*y + z*z, 1.0 / 2);
	}
};

bool check(const vector<vector<double>>& dst, double maxd)
{
	vector<bool> visit(dst.size(), false);
	stack<int> tovisit;

	tovisit.push(0);
	visit[0] = true;

	while (!tovisit.empty())
	{
		int cur = tovisit.top();
		tovisit.pop();

		if (cur == 1)
		{
			return true;
		}

		for (int i = 0; i < dst.size(); ++i)
		{
			if (!visit[i] && dst[cur][i] < maxd)
			{
				visit[i] = true;
				tovisit.push(i);
			}
		}
	}

	return false;
}

vector<vector<double>> getdst(const vector<point>& pts)
{
	vector<vector<double>> dst(pts.size(), vector<double>(pts.size()));

	for (int i = 0; i < pts.size(); ++i)
	{
		for (int j = 0; j < pts.size(); ++j)
		{
			dst[i][j] = pts[i].dstto(pts[j]);
		}
	}

	return dst;
}

double solve(int N, int S, const vector<point>& pts, const vector<point>& vs)
{
	double l = 0.0;
	double r = 1e6;

	const int ITERS = 300;
	auto dst = getdst(pts);
	for (int iter = 0; iter < ITERS; ++iter)
	{
		double m = (l + r) / 2;
		if (check(dst, m))
		{
			r = m;
		}
		else
		{
			l = m;
		}
	}

	return l;
}

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#elif defined CONTEST
	freopen(CONTEST".in", "r", stdin);
	freopen(CONTEST".out", "w", stdout);
#endif

	//ios_base::sync_with_stdio(false);
	
	int tests;
	cin >> tests;
	
	for (int tc = 1; tc <= tests; ++tc)
	{
		printf("Case #%d: ", tc);
		int N, S;
		cin >> N >> S;
		vector<point> pts;
		vector<point> vs;

		for (int i = 0; i < N; ++i)
		{
			point pos;
			pos.scan();
			point v;
			v.scan();

			pts.push_back(pos);
			vs.push_back(v);
		}

		double ans = solve(N, S, pts, vs);
		printf("%.7lf\n", ans);
	}

	return 0;
}