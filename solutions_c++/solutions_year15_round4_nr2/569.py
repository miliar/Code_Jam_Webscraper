#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <cmath>
using namespace std;

const double zero = 1e-6;

int cmp(double a, double b) {
	if (fabs(a - b) <= zero) return 0;
	if (a < b) return -1; else return 1;
}

int main() {
	int testcases;
	cin >> testcases;
	for (int testcase = 0; testcase < testcases; testcase ++) {
		int n;
		double V, C;
		double o;
		cin >> n >> V >> C;
		vector<double> r;
		vector<double> c;

		r.resize(n);
		c.resize(n);

		for (int i = 0; i < n; i ++) {
			cin >> r[i] >> c[i];
		}

		if (n == 1) {
			if (cmp(C, c[0]) == 0) {
				o = V / r[0];
			} else {
				o = -1.0;
			}
		} else {
			if (cmp(c[0], c[1]) == 0) {
				if (cmp(C, c[0]) == 0) {
					o = V / (r[0] + r[1]);
				} else {
					o = -1.0;
				}
			} else {
				double t1 = - V / r[0] * (c[1] - C) / (c[0] - c[1]);
				double t2 = V / r[1] * (c[0] - C) / (c[0] - c[1]);
				if (t1 >= 0 && t2 >= 0) {
					o = t1;
					if (t2 > o) o = t2;
				} else {
					o = -1.0;
				}
			}
		}

		cout << "Case #" << testcase + 1 << ": ";
		if (o >= 0) {
			cout << setprecision(9) << fixed << o;
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
	return 0;
}