#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <bitset>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <queue>
#include <assert.h>
#include <deque>
#include <string.h>


using namespace std;

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long int64;

typedef vector <int> vi;
typedef vector <vi> vvi;

const double eps = 1e-8;


bool can_do_it(double t, double c, double f, double x, double rate) {
	if (rate * t >= x) return true;
	
	double profit = 0;
	if (rate * t > c) {
		double profit = f * (t - c / rate) - c;
		if (profit <= 0) {
			return (rate * t >= x);
		}
		return can_do_it(t - c / rate, c, f, x, rate + f);
	}
	return (rate * t >= x);
}

void solve() {
	double c, f, x;
	double lo = 0;
	double hi = 1e9;
	cin >> c >> f >> x;

	while (hi - lo > eps) {
		double mid = (lo + hi) / 2;
		bool ok = can_do_it(mid, c, f, x, 2);
		if (ok) {
			hi = mid;
		} else {
			lo = mid;
		}
	}

	printf("%.9lf\n", hi);
}




int main () {
	//freopen("", "rt", stdin);
	//freopen("", "wt", stdout);
	//std::ios::sync_with_stdio(false);

	// cout << can_do_it(1, 30, 1, 2) << endl;

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cout << "Case #" << t + 1 << ": ";
		solve();
	}


    return 0;
}

