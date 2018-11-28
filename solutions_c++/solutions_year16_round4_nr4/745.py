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

using namespace std;

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

template<typename T> inline void swap(pair<T, T> &p) { swap(p.first , p.second ); }

#define all(v) v.begin(),v.end()

#define endl '\n'
template<typename T> struct argument_type;
template<typename T, typename U> struct argument_type<T(U)> { typedef U type; };
#define next(t, i) argument_type<void(t)>::type i; cin >> i;

template <typename T1, typename T2> istream& operator >>(istream& is, pair<T1, T2>& s) { is >> s.first >> s.second; return is; }
template <typename T> ostream& operator << (ostream& os, const vector<T> &v) { for (int i = 0 ; i < v.size() ; i++) { if (i) os << ' '; os << v[i]; } os << endl; return os; }
template <typename T1, typename T2> ostream& operator << (ostream& os, const vector<pair<T1, T2>> &v) { for (int i = 0 ; i < v.size() ; i++) { os << v[i] << endl; } return os; }
template <typename T1, typename T2> ostream& operator <<(ostream& s, const pair<T1, T2>& t) { s << t.first << ' ' << t.second; return s; }
template <typename T> vector<T> readVector(int n) { vector<T> res(n); for (int i = 0 ; i < n ; i++) cin >> res[i]; return res; }

vector<vector<LL>> min_costs(5);

int solve() {
	next(int, n);
	int mask = 0;

	FOR (i, 0, n) {
		next(string, str);
		for (auto c : str) {
			mask = mask << 1;
			if (c == '1') mask |= 1;
		}
	}
	return min_costs[n][mask];
}

int he_can(int n, int mask, int w) {
	// cout << mask << endl;
	mask = mask >> (w * n);
	// cout << mask << endl;
	mask = mask & ((1 << n) - 1);
	// cout << mask << endl;
	return mask;
}

int main() {
	srand (time(NULL));
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	fixed(cout); cout << setprecision(10);
	
	FOR (n, 1, 5) {
		vector<int> perm;
		int maxMask = 1 << (n * n);
		min_costs[n] = vector<LL>(maxMask, 0);

		FORD (mask, maxMask - 1, 0) {
			FOR (last, 0, n) {
				int can_work_on = he_can(n, mask, last);

				vector<int> covered = { 0 };
				FOR (i, 0, n) if (i != last) {
					int cur_can = he_can(n, mask, i);
					if (cur_can == 0) continue;
					vector<int> covered2;
					FOR (j, 0, n) if (cur_can & (1 << j)) for (auto m1 : covered) covered2.push_back(m1 | (1 << j));
					covered = covered2;
					sort(all(covered));
					covered.resize(unique(all(covered)) - covered.begin());
				}
				bool ok = can_work_on > 0;
				for (auto m1 : covered) if ((m1 & can_work_on) == can_work_on) ok = false;
				if (!ok) min_costs[n][mask] = IntMaxVal;
			}

			if (min_costs[n][mask] != IntMaxVal) continue;
			
			FOR (i, 0, n * n) if ((mask & (1 << i)) == 0) minimize(min_costs[n][mask], 1 + min_costs[n][mask | (1 << i)]);
		}
	}

	next(int, t);
	FOR (i, 1, t + 1) {
		auto sol = solve();
		cout << "Case #" << i << ": ";
		cout << sol;
		cout << endl;
	}
}