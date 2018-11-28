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
#include <gmpxx.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (n); ++i)
#define foreach(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)

template<typename T> inline void ignore(T) {
}

int solve(const string &s) {
	char c = s[0];
	int acc = 0;
	forn(i, (int) s.size()) {
		if (c != s[i]) {
			++acc;
			c = s[i];
		}
	}
	if (c == '-') { ++acc; }
	return acc;
}

int main(void) {
	int t; cin >> t;
	forn(k, t) {
		string s; cin >> s;
		int ans = solve(s);
		cout << "Case #" << (k+1) << ": " << ans << endl;
	}
	return 0;
}
