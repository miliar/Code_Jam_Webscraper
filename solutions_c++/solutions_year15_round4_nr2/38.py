#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std; 

#define DEBUG(x) cerr << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1<<29;
typedef long long ll;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }

template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////

const int MAX = 100;
int N;
double V, X;

struct rec {
	double R, X;
	bool operator<(const rec & r) const { return X < r.X; }
} in[MAX];
vector<rec> neg, neu, pos;

bool check(double t) {
	double v = 0.0;
	double sneg = 0, spos = 0;
	REP(i, neg.size())
		sneg += neg[i].R * t * (X-neg[i].X);
	REP(i, neu.size())
		v += neu[i].R * t;
	REP(i, pos.size())
		spos += pos[i].R * t * (pos[i].X-X);

	if (sneg < spos) {
		REP(i, neg.size())
			v += neg[i].R*t;
		REP(i, pos.size()) {
			double x = min(pos[i].R * t * (pos[i].X-X), sneg);
			v += x / (pos[i].X-X);
			sneg -= x;
		}
	} else {
		REP(i, pos.size())
			v += pos[i].R*t;
		REP(i, neg.size()) {
			double x = min(neg[i].R * t * (X-neg[i].X), spos);
			v += x / (X-neg[i].X);
			spos -= x;
		}
	}

	return v >= V;
}

void Solve(int tc)
{
	scanf("%d%lf%lf", &N, &V, &X);
	neg.clear(); neu.clear(); pos.clear();
	REP(i, N) {
		scanf("%lf%lf", &in[i].R, &in[i].X);
		if (EQ(in[i].X, X)) neu.push_back(in[i]);
		else if (in[i].X < X) neg.push_back(in[i]);
		else pos.push_back(in[i]);
	}
	sort(neg.begin(), neg.end());
	reverse(neg.begin(), neg.end());
	sort(pos.begin(), pos.end());

	bool ok = false;
	double be = 0, en = 1e12;
	REP(step, 500) {
		double t = (be+en) / 2;
		if (check(t)) { en = t; ok = true; }
		else be = t;
	}

	double res = (be+en)/2;
	printf("Case #%d: ", tc);
	if (ok)
		printf("%.9lf\n", res);
	else
		printf("IMPOSSIBLE\n");
}

int main()
{
	int T;
	scanf("%d\n", &T);
	FOR(tc,1,T) {
		cerr << "Test case: " << tc << endl;
		Solve(tc);
	}

	return 0;
}