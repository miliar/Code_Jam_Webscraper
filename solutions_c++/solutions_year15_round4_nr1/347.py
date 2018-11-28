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

int solve() {
	next(int, n);
	next(int, m);
	
	auto f = readVector<string>(n);
	int ans = 0;
	
	FOR (y, 0, n) FOR (x, 0, m) if (f[y][x] != '.') {
		int dx = 0, dy = 0;
		char c = f[y][x];
		if (c == '<') dx = -1;
		else if (c == '>') dx++;
		else if (c == 'v') dy++;
		else dy--;
		
		int x2 = x + dx;
		int y2 = y + dy;
		while (x2 >= 0 && y2 >= 0 && x2 < m && y2 < n && f[y2][x2] == '.') {
			x2 += dx;
			y2 += dy;
		}
		if (x2 >= 0 && y2 >= 0 && x2 < m && y2 < n) {
			continue;
		}
		
		int cnt = 0;
		FOR (x2, 0, m) if (f[y][x2] != '.') cnt++;
		FOR (y2, 0, n) if (f[y2][x] != '.') cnt++;
		if (cnt == 2) return -5;
		ans++;
	}
	
	return ans;
}

int main() {
	srand (time(NULL));
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	next(int, t);
	FOR (i, 0, t) {
		auto ans = solve();
		cout << "Case #" << i + 1 << ": ";
		if (ans < 0) cout << "IMPOSSIBLE";
		else cout << ans;
		cout << endl;
	}
}