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

ldouble solve()
{
	int N;
	ldouble V, X;
	cin >> N >> V >> X;
	
	vldouble R(N), C(N);
	REP(i, N)
		cin >> R[i] >> C[i];
		
	if(N == 1)
	{
		if(fabs(C[0] - X) < EPS)
			return V / R[0];
		return -1;
	}
	else if(N == 2)
	{
		if(fabs(C[0] - C[1]) < EPS)
		{
			if(fabs(C[0] - X) < EPS)
				return V / (R[0] + R[1]);
			return -1;
		}
		else
		{
			ldouble t0 = (X - C[1]) / (R[0] * (C[0] - C[1])), t1 = (X - C[0]) / (R[1] * (C[1] - C[0]));
			if(min(t0, t1) >= 0)
				return V * max(t0, t1);
			return -1;
		}
	}
	
	// TODO
	return -1;
}

int main()
{
	int T;
	
	cin >> T;
	REP(t, T)
	{
		printf("Case #%d: ", t + 1);
		ldouble out = solve();
		out >= 0 ? printf("%.8Lf\n", out) : puts("IMPOSSIBLE");
	}
	
	return 0;
}
