
#include <iostream>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <functional>
#include <cctype>
#include <climits>
#include <set>
#include <vector>
#include <queue>
#include <map>
#include <deque>
#include <stack>
#include <utility>
#include <string>
using namespace std;


void prn(int t, long double ans, bool bad = false) {
	cout << "Case #" << t << ": ";
	if (bad) {
		cout << "IMPOSSIBLE";
	} else {
		cout << setprecision(10) << fixed << ans;
	}
	cout << "\n";
}

long double eps = 1e-10;
bool iszero(long double a) {
	return abs(a) < eps;
}

int main () {

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int test;
	cin >> test;
	int n;
	long double v, x;
	long double r[2], c[2];
	long double t0, t1;
	for (int t = 1; t <= test; ++t ) {
		cin >> n >> v >> x;
		for (int i = 0; i < n; ++i) {
			cin >> r[i] >> c[i];	
		}
		if (n == 2 && iszero(c[0] - c[1])) {
			n = 1;
			r[0] += r[1];
		}
		if (n == 1) {
			if (!iszero(x - c[0])) {
				prn(t, c[0], true);
			} else {
				prn(t, v / r[0]);
			}
		} else {
			if (c[0] < c[1]) {
				swap(c[0], c[1]);
				swap(r[0], r[1]);
			}
			if (x < c[1] || x > c[0]) {
				prn(t, c[0], true);
			} else {
				t0 = v * (x - c[1]) / (c[0] - c[1]);
				t1 = v * (c[0] - x) / (c[0] - c[1]);
				prn(t, max(t0 / r[0], t1 / r[1]));
			}
		}
	}

	return 0;
}
