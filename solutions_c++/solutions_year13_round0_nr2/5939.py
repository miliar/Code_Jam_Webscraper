#if 1	// folding: default stuff
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <utility>
#include <numeric>
#include <bitset>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <ext/numeric>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
using namespace std;
using namespace rel_ops;
using namespace __gnu_cxx;
using namespace tr1;

#define FOR(x, b, e)    for (int x = (b); x <= (e); ++x)
#define FORD(x, b, e)   for (int x = (b); x >= (e); --x)
#define REP(x, n)       for (int x = 0; x < (n); ++x)
#define VAR(v, n)       typeof(n) v = (n)
#define ALL(c)          (c).begin(), (c).end()
#define SIZE(x)         ((int) (x).size())
#define EACH(i, c)      for (VAR(i, (c).begin()); i != (c).end(); ++i)
#define REACH(i, c)     for (VAR(i,(c).rbegin()); i != (c).rend(); ++i)
#define UNIQUE(v)	{ sort(ALL(v)); (v).resize(unique(ALL(v)) - (v).begin()); }
#define skip    continue
#define say     Cout,
#define dump    Cerr,
#define ever    ( ; ; )

const int INF = 1000000001;

typedef long long LL;
typedef unsigned long long ULL;

template <class T, class U>
ostream &operator, (ostream &out, const pair<T,U> &p) {
	return out, p.first, ' ', p.second;
}
template <class T, class U>
istream &operator, (istream &in, pair<T,U> &p) {
	return in, p.first, p.second;
}
template <class T>
ostream &operator, (ostream &out, const vector<T> &v) {
	EACH (i, v) {
		out, *i, ' ';
	}
	return out;
}
template <class T>
istream &operator, (istream &in, vector<T> &v) {
	EACH (i, v) {
		in, *i;
	}
	return in;
}
template <class T>
ostream &operator, (ostream &out, const T &t) {
	return out << t;
}
template <class T>
istream &operator, (istream &in, T &t) {
	return in >> t;
}
struct Ostream {
	ostream &out;
	Ostream(ostream &_out) : out(_out) {}
	static const void *lastLine;
	struct Line {
		ostream &out;
		bool first;
		Line(ostream &_out, bool _first = false) : out(_out), first(_first) {
			lastLine = this;
		}
		~Line() {
			if (this == lastLine) {
				out << '\n';
				lastLine = 0;
			}
		}
	};
};
const void *Ostream::lastLine = 0;
template <class T>
Ostream::Line operator, (const Ostream::Line &out, const T &t) {
	if (!out.first) {
		out.out << ' ';
	}
	out.out, t;
	return Ostream::Line(out.out);
}
template <class T>
Ostream::Line operator, (const Ostream &out, const T &t) {
	return Ostream::Line(out.out, true), t;
}
Ostream Cout(cout), Cerr(cerr);
int io_init() {
#ifdef ONLINE_JUDGE
	cin.tie(0);
	cout.tie(0);
#endif
	ios_base::sync_with_stdio(false);
	cout << fixed << setprecision(9);
	return 1;
}
int _io_dummy = io_init();

template <class T, class U>
bool remin(T &a, const U &b) {
	return b < a ? a = b, true : false;
}
template <class T, class U>
bool remax(T &a, const U &b) {
	return b > a ? a = b, true : false;
}
template <class T>
T fromString(const string &s) {
	T t;
	istringstream(s) >> t;
	return t;
}
template <class T>
string toString(const T &t) {
	ostringstream oss;
	oss << t;
	return oss.str();
}
#endif	// folding: default stuff

bool f(const vector<vector<int> > &v, int r, int c) {
	const int R = SIZE(v);
	const int C = SIZE(v[0]);
	const int x = v[r][c];
	
	bool rok = 1, cok = 1;
	REP (i, R) {
		rok = rok && v[i][c] <= x;
	}
	REP (i, C) {
		cok = cok && v[r][i] <= x;
	}
	return rok || cok;
}

int main() {
	int tests;
	cin, tests;
	FOR (tt, 1, tests) {
		int R, C;
		cin, R, C;
		vector<vector<int> > v(R, vector<int>(C));
		cin, v;
		bool ok = 1;
		REP (r, R) {
			REP (c, C) {
				ok = ok && f(v, r, c);
			}
		}
		cout, "Case #", tt;
		say ':', ok ? "YES" : "NO";
	}
}
