#include "assert.h"
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <time.h>
#include <vector>

#if LOCAL
	#define DO_NOT_SEND
#endif

typedef long long LL;

int IntMaxVal = (int) 1e20;
int IntMinVal = (int) -1e20;
LL LongMaxVal = (LL) 1e20;
LL LongMinVal = (LL) -1e20;

#define FOR(i, a, b) for(int i = a; i < b ; ++i)
#define FORD(i, a, b) for(int i = a; i >= b; --i)

template<typename T> inline void minimize(T &a, T b) { a = std::min(a, b); }
template<typename T> inline void maximize(T &a, T b) { a = std::max(a, b); }

#define all(v) v.begin(),v.end()

using namespace std;

#define endl '\n'
template<typename T> struct argument_type;
template<typename T, typename U> struct argument_type<T(U)> { typedef U type; };
#define next(t, i) argument_type<void(t)>::type i; cin >> i;

template <typename T1, typename T2> istream& operator >>(istream& is, pair<T1, T2>& s) { is >> s.first >> s.second; return is; }
template <typename T> ostream& operator << (ostream& os, const vector<T> &v) { for (int i = 0 ; i < v.size() ; i++) os << v[i] << ' '; os << endl; return os; }
template <typename T1, typename T2> ostream& operator <<(ostream& s, const pair<T1, T2>& t) { s << t.first << ' ' << t.second; return s; }
template <typename T> vector<T> readVector(int n) { vector<T> res(n); for (int i = 0 ; i < n ; i++) cin >> res[i]; return res; }

double eps = 1e-6;
double eps2 = 1e-12;

double solve() {
	next(int, n);
	next(double, v_req);
	next(double, t_req);
	
	auto ps2 = readVector<pair<double, double>>(n);
	for (auto &p : ps2) swap(p.first, p.second);
	deque<pair<double, double>> ps(all(ps2));
	sort(all(ps));
	
	if (t_req < ps.front().first - eps) return -10;
	if (t_req > ps.back().first + eps) return -20;
	
	double cur_flow = 0;
	
	while (ps.size()) {
		if (ps.front().first < t_req - eps2 && ps.back().first > t_req + eps2) {
			double t1 = ps.front().first;
			double t2 = ps.back().first;
			double k = (t_req - t1) / (t2 - t_req);
			double v1 = min(ps.front().second, ps.back().second / k);
			double v2 = k * v1;
			cur_flow += v1 + v2;
			ps.front().second -= v1;
			if (ps.front().second < eps2) ps.pop_front();
			ps.back().second -= v2;
			if (ps.back().second < eps2) ps.pop_back();
		} else if (fabs(ps.front().first - t_req) < eps2) {
			cur_flow += ps.front().second;
			ps.pop_front();
		} else if (fabs(ps.back().first - t_req) < eps2) {
			cur_flow += ps.back().second;
			ps.pop_back();
		} else break;
	}
	return v_req / cur_flow;
}

int main() {
	srand (time(NULL));
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	next(int, t);
	fixed(cout);
	cout << setprecision(10);
	FOR (i, 1, t + 1) {
		auto ans = solve();

		cout << "Case #" << i << ": ";		
		if (ans < 0) cout << "IMPOSSIBLE";
		else cout << ans;
		cout << endl;
	}
}