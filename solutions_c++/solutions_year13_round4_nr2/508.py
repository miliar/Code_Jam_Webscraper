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
#define debug(x) cerr << #x << ": " << (x) << endl;

typedef long long int64;

typedef vector <int> vi;
typedef vector <vi> vvi;


int64 pow2(int64 n) {
	return (1ll << n);
}

bool chance(int64 num, int64 n, int64 p) {
	// cerr << "chance of num " << num << " at " << pow2(n) << " p = " << p << endl;
	assert (1 <= p && p <= pow2(n));
	if (n == 0) {
		return true;
	}

	int64 part = pow2(n - 1);
	int64 last = pow2(n) - 1;
	if (p >= part) {
		if (p == pow2(n)) {
			return true;
		}
		return num != last;
	}
	return chance( (num - 1) / 2 + 1, n - 1, p);
}


int64 chance(int64 n, int64 p) {
	int64 lo = 0;
	int64 hi = (1ll << n);

	while (lo + 1 < hi) {
		int64 mid = (lo + hi) / 2;

		// cerr << "checking " << mid  << endl;
		if (chance(mid, n, p)) {
			lo = mid;
		} else {
			hi = mid;
		}
	}
	return lo;
}


bool guarantee(int64 num, int64 n, int64 p) {
	// cerr << "chance of num " << num << " at " << pow2(n) << " p = " << p << endl;
	assert (1 <= p && p <= pow2(n));
	if (n == 0) {
		return true;
	}

	int64 part = pow2(n - 1);
	int64 last = pow2(n) - 1;
	if (p <= part) {
		return num == 0;
	}
	return guarantee( (num - 1) / 2, n - 1, p - part);
}

int64 guarantee(int64 n, int64 p) {
	int64 lo = 0;
	int64 hi = (1ll << n);

	while (lo + 1 < hi) {
		int64 mid = (lo + hi) / 2;

		// cerr << "checking " << mid  << endl;
		if (guarantee(mid, n, p)) {
			lo = mid;
		} else {
			hi = mid;
		}
	}
	return lo;
}


void solve() {
	int64 n, p;
	cin >> n >> p;

	cout << guarantee(n, p) << " " << chance(n, p) << endl;

}



int main () {
	//freopen("", "rt", stdin);
	//freopen("", "wt", stdout);
	//std::ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cout << "Case #" << t + 1 << ": ";
		solve();
	}

    return 0;
}

