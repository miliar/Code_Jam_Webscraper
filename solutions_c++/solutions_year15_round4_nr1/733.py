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

char dir[4] = { '>', '<', '^', 'v' };

bool check(const vstring &A, const char &direction, const int &x, const int &y)
{
	if(direction == '>')
	{
		FOR(i, y + 1, SIZE(A[x]) - 1)
			if(A[x][i] != '.')
				return true;
	}
	else if(direction == '<')
	{
		FORD(i, y - 1, 0)
			if(A[x][i] != '.')
				return true;
	}
	else if(direction == '^')
	{
		FORD(i, x - 1, 0)
			if(A[i][y] != '.')
				return true;
	}
	else
	{
		FOR(i, x + 1, SIZE(A) - 1)
			if(A[i][y] != '.')
				return true;
	}
		
	return false;
}

int solve()
{
	int R, C;	
	cin >> R >> C;
	
	vstring A(R);
	REP(i, R)
		cin >> A[i];
	
	int out = 0;
	
	REP(i, R) REP(j, C)
		if(A[i][j] != '.' && !check(A, A[i][j], i, j))
		{
			int dirs = 0;
			REP(k, 4)
				dirs += check(A, dir[k], i, j);
			if(dirs == 0)
				return -1;
			out++;
		}
	
	return out;
}

int main()
{
	int T;
	
	cin >> T;
	REP(t, T)
	{
		printf("Case #%d: ", t + 1);
		int out = solve();
		out >= 0 ? printf("%d\n", out) : puts("IMPOSSIBLE");
	}
	
	return 0;
}
