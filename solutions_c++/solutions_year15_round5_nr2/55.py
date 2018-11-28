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

LL getMinL(LL s, int k) {
	if (s >= 0) return (s + k - 1) / k;
	else return s / k;
}

LL getMaxL(LL s, int k) {
	if (s >= 0) return s / k;
	else return (s - k + 1) / k;
}


int solve() {
	next(int, n);
	next(int, k);
	
	auto sums = readVector<int>(n - k + 1);
	vector<int> dRoot(n);
	FOR (i, k, n) dRoot[i] = dRoot[i - k] + sums[i - k + 1] - sums[i - k];
	vector<pair<int, int>> rootDiff(k, { 0 , 0 });
	FOR (i, k, n) {
		minimize(rootDiff[i % k].first, dRoot[i]);
		maximize(rootDiff[i % k].second, dRoot[i]);
	}
	
	int dl = -1;
	FOR (i, 0, k) maximize(dl, rootDiff[i].second - rootDiff[i].first - 1);
	int dr = 20000000;
	
	while (dl + 1 < dr) {
		int d = (dl + dr) / 2;
				
		vector<pair<int, int>> add_ranges(k);
		FOR (i, 0, k) {
			add_ranges[i] = { -rootDiff[i].first , d - rootDiff[i].second };
		}
		
		LL totalAddMin = 0;
		LL totalAddMax = 0;
		FOR (i, 0, k) {
			totalAddMin += add_ranges[i].first;
			totalAddMax += add_ranges[i].second;
		}
		auto maxL = getMaxL(sums.front() - totalAddMin, k);
		auto minL = getMinL(sums.front() - totalAddMax, k);
		
		if (minL <= maxL) dr = d;
		else dl = d;
	}
	
	return dr;
}

int main() {
	srand (time(NULL));
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	fixed(cout);
	cout << setprecision(10);
	
	next(int, t);
	FOR (i, 1, t + 1) cout << "Case #" << i << ": " << solve() << endl;
}