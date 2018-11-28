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

struct generator {
	int cur;
	int mult; 
	int add;
	int mod;
	
	void read() {
		cin >> cur >> mult >> add >> mod;
	}
	
	int get_and_move() {
		int res = cur;
		cur = (cur * mult + add) % mod;
		return res;
	}
};

generator s_gen, m_gen;

int solve() {
	next(int, n);
	next(int, d);
	
	s_gen.read();
	m_gen.read();
	
	vector<int> salaries(n);
	FOR (i,0 , n) salaries[i] = s_gen.get_and_move();
	
	m_gen.get_and_move();
	
	vector<pair<int, int>> full_fork(n, { salaries[0] , salaries[0] });
	FOR (i, 1, n) {
		int p = m_gen.get_and_move() % i;
		full_fork[i] = full_fork[p];
		minimize(full_fork[i].first, salaries[i]);
		maximize(full_fork[i].second, salaries[i]);
	}
	
	vector<int> possible_starts(1e6);
	for (auto p : full_fork) {
		if (p.second - p.first <= d) {
			int mn = p.second - d;
			maximize(mn, 0);
			int mx = p.first;
			possible_starts[mn]++;
			if (mx + 1 != possible_starts.size()) possible_starts[mx + 1]--;
		}
	}
	
	FOR (i, 1, possible_starts.size()) possible_starts[i] += possible_starts[i - 1];
	int ans = 1;
	for (auto x : possible_starts) maximize(ans, x);
	return ans;
}

int main() {
	srand (time(NULL));
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	next(int, t);
	FOR (i, 1, t + 1) cout << "Case #" << i << ": " << solve() << endl;
}