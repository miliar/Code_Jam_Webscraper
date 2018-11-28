/*
 * b.cpp
 *
 */

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

using namespace std;

#define forn(i, n) for (int i = 0; i < (n); ++i)
#define foreach(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)

template<typename T> inline void ignore(T) {}

double solve(double c, double f, double x) {
	double best = x / 2.0;
	double accu = 0;
	for (int m = 0;; ++m) {
		accu += c / (2.0 + m * f);
		if (accu > best) {
			break;
		} else {
			best = min(best, accu + x / (2.0 + (m + 1) * f));
		}
	}
	return best;
}

int main(void) {
	int t; cin >> t;
	forn(k, t) {
		double c, f, x;
		cin >> c >> f >> x;
		double ans = solve(c, f, x);
		cout.precision(10);
		printf("Case #%d: %.7f\n", k+1, ans);
		//cout << "Case #" << (k+1) << ": " << ans << endl;
	}
	return 0;
}
