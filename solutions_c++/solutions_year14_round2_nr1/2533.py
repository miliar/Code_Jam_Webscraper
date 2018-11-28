// Round 1B 2014
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
	#define VAR(v,i) auto (i) v=(i)
#else
	#define VAR(v,i) __typeof(i) v=(i)
#endif
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()

#define ADD_EDGE(g,u,v) g[u].push_back(v),g[v].push_back(u)

#define ST first
#define ND second
#define PB push_back
#define INF 1000000000
#define INFL 1000000000000000000LL
#define EPS 1e-5

void shorten(string &s, pair<string, vint> &d)
{
	d.ST = s.substr(0, 1), d.ND.PB(1);
	REP(i, SIZE(s) - 1)
		if(s[i] != s[i + 1])
			d.ST += s.substr(i + 1, 1), d.ND.PB(1);
		else
			++d.ND.back();
}

llong solve(vector<string> &S, int N)
{
	vector<pair<string, vint> > D(N);

	REP(i, N)
		shorten(S[i], D[i]);

	REP(i, N)
		FOR(j, i + 1, N - 1)
			if(D[i].ST != D[j].ST)
				return INF;

	int out = 0;
	REP(i, SIZE(D[0].ND))
	{
		int sum = 0, r = 0;
		REP(j, N)
			sum += D[j].ND[i];
		r = sum % N, sum /= N;
		if(r > N / 2)
			sum++;

		REP(j, N)
			out += max(D[j].ND[i] - sum, sum - D[j].ND[i]);
	}
	return out;
}

int main()
{
	int T;
	
	cin >> T;
	REP(t, T)
	{
		int N;
		cin >> N;

		vector<string> S(N);
		REP(i, N)
			cin >> S[i];
		
		int out = solve(S, N);
		if(out == INF)
			printf("Case #%d: Fegla Won\n", t + 1);
		else
			printf("Case #%d: %d\n", t + 1, out);
	}
	
	return 0;
}
