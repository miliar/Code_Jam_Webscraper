#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <complex>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <gmpxx.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (n); ++i)
#define foreach(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)

template<typename T> inline void ignore(T) { }

char bestof(char a, char b) {
	switch (a) {
	case 'R':
		switch (b) {
		case 'R':
			return ' ';
		case 'P':
			return 'P';
		case 'S':
			return 'R';
		default:
			return ' ';
		}
	case 'P':
		switch (b) {
		case 'R':
			return 'P';
		case 'P':
			return ' ';
		case 'S':
			return 'S';
		default:
			return ' ';
		}
	case 'S':
		switch (b) {
		case 'R':
			return 'R';
		case 'P':
			return 'S';
		case 'S':
			return ' ';
		default:
			return ' ';
		}
	default:
		return ' ';
	}
}

map<array<int, 4>, pair<string, char> > memo;

pair<string, char> solve(int n, int r, int p, int s) {
	string best = "";
	char result = ' ';
	if (n == 1) {
		if (r == 2 || p == 2 || s == 2) { return {"", ' '}; }
		if (p == 1 && s == 1) { return {"PS", 'S'}; }
		if (p == 1 && r == 1) { return {"PR", 'P'}; }
		if (s == 1 && r == 1) { return {"RS", 'R'}; }
		assert(false);
	}
	array<int, 4> key = {{n, r, p}};
	if (memo.count(key)) { return memo[key]; }
	forn(rr, r+1) {
		forn(pp, p+1) {
			int ss = (1 << (n - 1)) - rr - pp;
			if (ss < 0 || ss > s) { continue; }
			assert(rr + pp + ss == (1 << (n -1)));
			auto left = solve(n - 1, rr, pp, ss);
			if (left.first.empty()) { continue; }
			auto right = solve(n - 1, r - rr, p - pp, s - ss);
			if (right.first.empty()) { continue; }
			if (left.second == right.second) { continue; }
			char winner = bestof(left.second, right.second);
			string current = left.first + right.first;
			if (best.empty()) { best = current; result = winner; }
			if (current < best) { best = current; result = winner; }
		}
	}
	memo[key] = {best, result};
	return {best, result};
}

int main(void) {
	int t; cin >> t;
	forn(k, t) {
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		string ans = solve(n, r, p, s).first;
		if (ans.empty()) { ans = "IMPOSSIBLE"; }
		cout << "Case #" << (k+1) << ": " << ans << endl;
	}
	return 0;
}
