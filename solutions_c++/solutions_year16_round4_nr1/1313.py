#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
// #include <queue>
#include <cmath>
//download TTMath from http://www.ttmath.org/
// #include "ttmath-0.9.3/ttmath/ttmath.h"
#undef max
#undef min

using namespace std;
// using namespace ttmath;
// typedef Int<100> num;

#define metafor(iter,container) \
	for ((iter) = (container).begin(); (iter) != (container).end(); ++(iter))
#define FOR(i,n) for (size_t i = 0; i < (n); ++i)
#define FORi(i,n) for (int i = 0; i < (n); ++i)
template<class C> void show(const C & v) { FOR(i,v.size()) cout << v[i] << ' '; cout << endl; }
ostream& operator<<(ostream& os, const pair<int,char> & v) { os << ' ' << v.first << v.second; return os; }
// ostream& operator<<(ostream& os, const vector<int> & v) { FOR(i, v.size()) os << ' ' << v[i]; return os; }

string solver(const int n, const int p, const int r, const int s)
{
	if (p > r+s) return string();
	if (r > p+s) return string();
	if (s > p+r) return string();
	if (n == 1) {
		if (s == 0) { assert(p == 1 && r == 1); return "PR"; }
		if (r == 0) { assert(p == 1 && s == 1); return "PS"; }
		if (p == 0) { assert(r == 1 && s == 1); return "RS"; }
		assert(false);
		return string();
	}
	if (n & 1) {
		if (p == r) { if (!(s == p-1 && (p&1))) return string(); string a = solver(n-1, p-s/2, s/2, s/2); if (a.empty()) return a; string b = solver(n-1, s/2, r-s/2, s/2); if (b.empty()) return b; return a+b; }
		if (p == s) { if (!(r == p-1 && (p&1))) return string(); string a = solver(n-1, p-r/2, r/2, r/2); if (a.empty()) return a; string b = solver(n-1, r/2, r/2, s-r/2); if (b.empty()) return b; return a+b; }
		if (r == s) { if (!(p == r-1 && (r&1))) return string(); string a = solver(n-1, p/2, r-p/2, p/2); if (a.empty()) return a; string b = solver(n-1, p/2, p/2, s-p/2); if (b.empty()) return b; return a+b; }
		return string();
	} else {
		if (r == s) { if (!(p == r+1 && (r&1))) return string(); string a = solver(n-1, p/2, p/2, s-p/2); if (a.empty()) return a; string b = solver(n-1, p/2, r-p/2, p/2); if (b.empty()) return b; return a+b; }
		if (p == s) { if (!(r == p+1 && (p&1))) return string(); string a = solver(n-1, r/2, r/2, s-r/2); if (a.empty()) return a; string b = solver(n-1, p-r/2, r/2, r/2); if (b.empty()) return b; return a+b; }
		if (p == r) { if (!(s == p+1 && (p&1))) return string(); string a = solver(n-1, s/2, r-s/2, s/2); if (a.empty()) return a; string b = solver(n-1, p-s/2, s/2, s/2); if (b.empty()) return b; return a+b; }
		return string();
	}
}
string solve_case(const int n, const int r, const int p, const int s)
{
	return solver(n, p, r, s);
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	out.precision(18);
	out.setf(std::ios_base::fixed, std::ios_base::floatfield);
	for (int t = 1; t <= TC_NCases; ++t)
	{
		int N, R, P, S;
		in >> N >> R >> P >> S; assert(N >= 1);
		assert(R+P+S == (1 << N));

		string result = solve_case(N, R, P, S);
		if (result.empty()) result = "IMPOSSIBLE";
		out << "Case #" << t << ": " << result << endl;
	}
}


int main()
{
	// ifstream in("A-sample.in");
	// ofstream out("A-sample-out.txt");

	// ifstream in("A-small-attempt0.in");
	// ofstream out("A-small-attempt0-out.txt");

	ifstream in("A-large.in");
	ofstream out("A-large-out.txt");

	solve(in,out);
	
	return 0;
}
