#define _CRT_SECURE_NO_WARNINGS

#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

bool check(string a, int r, int p, int s) {
	REP(i, a.size()) {
		if (a[i] == 'R')
			r--;
		if (a[i] == 'P')
			p--;
		if (a[i] == 'S')
			s--;
	}

	return !r && !p && !s;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

	std::vector<string> rr, pp, ss;

	rr.pb("R");
	pp.pb("P");
	ss.pb("S");

	FOR(i, 1, 13) {
		rr.pb(min(rr[i - 1] + ss[i - 1], ss[i - 1] + rr[i - 1]));
		ss.pb(min(pp[i - 1] + ss[i - 1], ss[i - 1] + pp[i - 1]));
		pp.pb(min(rr[i - 1] + pp[i - 1], pp[i - 1] + rr[i - 1]));
	}
		 

	int tt;
	cin >> tt;
	REP(t, tt) {
		cout << "Case #" << t + 1 << ": ";

		int n, r, p, s;
		cin >> n >> r >> p >> s;
			
		std::vector<string> a;

		if (check(rr[n], r, p, s)) {
			a.pb(rr[n]);
		}
		if (check(pp[n], r, p, s)) {
			a.pb(pp[n]);
		}
		if (check(ss[n], r, p, s)) {
			a.pb(ss[n]);
		}

		SORT(a);
		if (!a.size())
			cout << "IMPOSSIBLE" << endl;
		else
			cout << a[0] << endl;
	}

	return 0;
}
