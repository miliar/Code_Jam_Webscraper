#pragma comment(linker, "/STACK:512000000")
#include <iostream>
#include <vector>
#include <iomanip>
#include <set>
#include <queue>
#include <deque>
#include <map>
#include <list>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <cstring>
#include <ctime>
#include <string>
#include <sstream>
#include <math.h>
#include <stack>

using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

const long double EPS = 1e-6;

long double solve(long double v, long double x, vector< pair< long double, long double > > a) {
	if (a.size() == 1) {
		if (x != a[0].second) {
			return -10000;
		} else {
			return v / a[0].first;
		}
	}


	if (a.size() == 2) {
		if (a[0].second > a[1].second) {
			swap(a[0], a[1]);
		}

		if (x < a[0].second - EPS || x > a[1].second + EPS) {
			return -10000;
		} else {

			if (fabs(x - a[0].second) < EPS && fabs(x - a[1].second) < EPS) {
				return v / (a[0].first + a[1].first);
			}

			if (fabs(x - a[0].second) < EPS) {
				return v / (a[0].first);
			}

			if (fabs(x - a[1].second) < EPS) {
				return v / (a[1].first);
			}
			long double c0 = a[0].second;
			long double c1 = a[1].second;

			long double v1 = v * (x - c0) / (c1 - c0);
			long double v0 = v - v1;

			return max(v1 / a[1].first, v0 / a[0].first);
		}
	}
}

int main() {

	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
	    freopen("output.txt","w",stdout);
	#else
	#define taskname "cutting"
		//freopen(taskname".in","r",stdin);
		//freopen(taskname".out","w",stdout);
	#endif



	int tests_; cin >> tests_;
	for (int test_ = 1; test_ <= tests_; ++test_) {
		
		int n; cin >> n;
		long double v, x;
		cin >> v >> x;

		vector< pair< long double, long double > > a(n);

		for (int i = 0; i < n; ++i) {
			cin >> a[i].first >> a[i].second;
		}


		long double ans = solve(v, x, a);

		cout.precision(9);
		cout << fixed;
		cerr.precision(9);
		cerr << fixed;

		if (ans > -100) {
			cout << "Case #" << test_ << ": " << ans << endl;		
			cerr << "Case #" << test_ << ": " << ans << endl;
		} else {
			cout << "Case #" << test_ << ": " << "IMPOSSIBLE" << endl;		
			cerr << "Case #" << test_ << ": " << "IMPOSSIBLE" << endl;
		}
		
	}

	return 0;
}