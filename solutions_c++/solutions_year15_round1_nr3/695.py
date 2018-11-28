// Round 1A 2012
// Problem X.

#ifdef _MSC_VER
	#define _CRT_SECURE_NO_WARNINGS
#endif

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <iostream>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <vector>
#include <algorithm>
#include <iterator>
#include <cassert>

using namespace std;

typedef unsigned long long llong;
typedef long double ldouble;
typedef pair<int, int> pint;
typedef pair<double, double> pdouble;
typedef vector<int> vint;
typedef vint::iterator vit;
typedef vector<double> vdouble;
typedef vdouble::iterator vdit;
typedef vector<ldouble> vldouble;
typedef vector<string> vstring;
typedef vector<llong> vllong;
typedef vector<vint> graph;

#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#ifdef _MSC_VER
	#define VAR(v,i) auto v=(i)
#else
	#define VAR(v,i) __typeof(i) v=(i)
#endif
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()

#define ADD_EDGE(g,u,v) g[u].push_back(v),g[v].push_back(u)

#define ST first
#define ND second
#define INF 1000000000
#define INFL 1000000000000000000LL
#define EPS 1e-5

struct Point
{
	double x, y;
	
	bool operator< (const Point& p) const
	{
		return x < p.x || (x == p.x && y < p.y);
	}
};

double cross(const Point &O, const Point &A, const Point &B)
{
	return (A.x - O.x) * (B.y - O.y) - (A.y - O.y) * (B.x - O.x);
}

bool convex_hull(vector<Point> &P, Point &X)
{
	int n = P.size(), k = 0;
	vector<Point> H(2 * n);

	for (int i = 0; i < n; ++i) {
		while (k >= 2 && cross(H[k - 2], H[k - 1], P[i]) < -1e-6) k--;
		H[k++] = P[i];
	}

	for (int i = n-2, t = k+1; i >= 0; i--) {
		while (k >= t && cross(H[k - 2], H[k - 1], P[i]) < -1e-6) k--;
		H[k++] = P[i];
	}
 
	REP(i, k)
		if (fabs(H[i].x - X.x) < 1e-6 && fabs(H[i].y - X.y) < 1e-6)
			return true;
	return false;
}

int solve(Point &X, vector<Point> &P, vector<Point> &S, int i)
{
	if(i == SIZE(P))
	{
		if(convex_hull(S, X))
			return SIZE(P) - SIZE(S);
		return INF;
	}
	
	int out = INF;
	
	if (!(fabs(P[i].x - X.x) < 1e-6 && fabs(P[i].y - X.y) < 1e-6))
		out = solve(X, P, S, i + 1);
	
	S.push_back(P[i]);
	out = min(out, solve(X, P, S, i + 1));
	S.pop_back();
	
	return out;
}

int solve(Point &X, vector<Point> P)
{
	vector<Point> S;
	sort(ALL(P));
	return solve(X, P, S, 0);
}

void solve()
{
	int N;
	cin >> N;
	
	vector<Point> P(N);
	REP(i, N)
		cin >> P[i].x >> P[i].y;

	cout << endl;
	REP(i, N)
		cout << solve(P[i], P) << endl;
}

int main()
{
	int T;
	
	cin >> T;
	REP(t, T)
	{
		printf("Case #%d:", t + 1);
		solve();
	}
	
	return 0;
}
