#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <functional>
#include <sstream>
#include <fstream>
#include <valarray>
#include <complex>
#include <queue>
#include <cassert>
#include <bitset>
using namespace std;

#ifdef LOCAL
	#define debug_flag true
#else
	#define debug_flag false
#endif

#define dbg(args...) { if (debug_flag) { _print(_split(#args, ',').begin(), args); cerr << endl; } else { void(0);} }

vector<string> _split(const string& s, char c) {
	vector<string> v;
	stringstream ss(s);
	string x;
	while (getline(ss, x, c))
		v.emplace_back(x);
	return v;
}

void _print(vector<string>::iterator) {}
template<typename T, typename... Args>
void _print(vector<string>::iterator it, T a, Args... args) {
    string name = it -> substr((*it)[0] == ' ', it -> length());
    if (isalpha(name[0]))
	    cerr << name  << " = " << a << " ";
	else
	    cerr << name << " ";
	_print(++it, args...);
}

#ifdef LOCAL
    #define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
    #define eprintf(...) 42;
#endif

typedef long long int int64;

struct Point
{
	double x, y, z;
	Point() : x(), y(), z() {}
	Point(double _x, double _y, double _z) : x(_x), y(_y), z(_z) {}

	void scan()
	{
		scanf("%lf%lf%lf", &x, &y, &z);
	}

	Point operator - (const Point &p) const
	{
		return Point(x - p.x, y - p.y, z - p.z);
	}

	double operator % (const Point &p) const
	{
		return x * p.x + y * p.y + z * p.z;
	}

	double length() const
	{
		return sqrtl(*this % *this);
	}

	double dist_to(const Point &p) const
	{
		return (*this - p).length();
	}
};

const int N = 2000;

int n, s;
Point P[N], V[N];
bool used[N];

void dfs(int v, double m)
{
	used[v] = true;
	for (int to = 0; to < n; to++)
		if (!used[to] && P[v].dist_to(P[to]) <= m)
			dfs(to, m);
}

bool can(double m)
{
	fill(used, used + n, false);
	dfs(0, m);
	return used[1];
}

void solve(int test)
{
	scanf("%d%d", &n, &s);
	for (int i = 0; i < n; i++)
	{
		P[i].scan();
		V[i].scan();
	}

	double l = 0;
	double r = 1e9;
	for (int it = 0; it < 200; it++)
	{
		double m = (l + r) / 2;
		if (can(m))
			r = m;
		else
			l = m;
	}

	printf("Case #%d: %.10lf\n", test, r);
}

int main()
{
#ifdef LOCAL
	freopen ("input.txt", "r", stdin);
#endif

    int tests;
    scanf("%d", &tests);
    for (int test = 0; test < tests; test++)
    {
        dbg(test);
        solve(test + 1);
    }

	return 0;
}
