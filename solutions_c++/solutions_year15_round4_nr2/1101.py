

#if 1

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cassert>
#include <fstream>

using namespace std;
typedef int64_t int64;

typedef pair<int,int> pii;
typedef pair<double,double> pdd;
#define mp make_pair
#define X first
#define Y second
#define pb push_back

static void solve();

int computeSmall(int b, int n, deque<int> &m);

int main() {
	freopen("B.in.txt","r",stdin);
	freopen("B.out.txt","w",stdout);
	int test_case;
	cin >> test_case;
	for (int t = 1; t <= test_case; ++t) {
//		cerr << endl << t << endl;
		cout << "Case #" << t << ": ";
		solve();
		cout << '\n';
	}
	return 0;
}

static int64 gcd(int64 a, int64 b) {
	if (a < 0 || b < 0)
		return -1;
	while (b != 0) {
		int64 x = a % b;
		a = b;
		b = x;
	}
	return a;
}

static int64 lcm(int64 a, int64 b) {
	if (a < 0 || b < 0)
		return -1;  // bad input
	if (a == 0 || b == 0)
		return 0;
	int64 k = a / gcd(a, b) * b;
	if (k < 0 || a < 0 || b < 0 || k % a != 0 || k % b != 0)
		k = -1;  // overflow
	return k;
}

// returns lowest number, n, for which f(n) >= value
// f must be non-decreasing
template<typename I, class T, typename Func>
I lower_bound_argument(I first, I last, const T& value, Func f) {
	I count = last - first;
	while (count > 0) {
		I i = first;
		I step = count / 2;
		i += step;
		if (f(i) < value) {
			first = ++i;
			count -= step + 1;
		}
		else
			count = step;
	}
	return first;
}

// returns lowest number, n, for which f(n) <= value
// f must be non-decreasing
template<typename I, class T, typename Func>
I upper_bound_argument(I first, I last, const T& value, Func f) {
	I count = last - first;

	while (count > 0) {
		I i = first;
		I step = count / 2;
		i += step;
		if (!(f(i) < value)) {
			first = ++i;
			count -= step + 1;
		}
		else
			count = step;
	}
	return first;
}

static int nextInt() {
	int i;
	cin >> i;
	return i;
}

static int64 nextInt64() {
	int64 i;
	cin >> i;
	return i;
}

static double nextDouble() {
	double i;
	cin >> i;
	return i;
}

static void solve() {
	int n;
	double vTarget, cTarget;
	cin >> n >> vTarget >> cTarget;
//	cerr << n << " " << " " << vTarget << " " << cTarget << endl;
	vector<double> r, c;
	for (int i = 0; i < n; ++i) {
		r.pb(nextDouble());
		c.pb(nextDouble());
//		cerr << i << " " << " " << r[i] << " " << c[i] << endl;
	}
	double t = -1;
	if (n == 1) {
		if (cTarget == c[0]) {
			t = vTarget / r[0];
		}
	} else if (n == 2) {
		if (cTarget <= max(c[0], c[1]) && cTarget >= min(c[0], c[1])) {
			if (c[0] == c[1]) {
				if (cTarget == c[0]) {
					t = vTarget / (r[0] + r[1]);
				}
			}
			else {
				double a = (cTarget - c[1]) / (c[0] - c[1]);
				for (int i = 0; i < n; ++i) {
					double vi = vTarget * a;
					double ti = vi / r[i];
					t = max(t, ti);
					a = 1 - a;
				}
			}
		}
	}
	else {
		t = -1;
	}
	if (t < 0)
		cout << "IMPOSSIBLE";
	else {
//		cout.precision(6);
		char buff[100];
		sprintf(buff, "%.6f", t);
//		cout << t;
		cout << setw(-1) << buff;
	}
}

#endif

