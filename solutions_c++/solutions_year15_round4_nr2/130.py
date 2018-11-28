#include <bits/stdc++.h>

using namespace std;

double c[128], r[128];

#define EPS 1e-8

inline int cmp(const double &x, const double &y) {
	if (y - x > EPS) return -1;
	return x - y > EPS;
}

int main(void) {
	long T;
	cin >> T;
	cout.setf(ios::fixed);
	cout.precision(9);
	for(long t = 1; t <= T; ++ t) {
		long N; double v, x;
		cin >> N >> v >> x;
		for(long i = 0; i < N; ++ i) {
			cin >> r[i] >> c[i];
		}
		cout << "Case #" << t << ": ";
		if (N == 1) {
			if (cmp(c[0], x)) {
				cout << "IMPOSSIBLE" << endl;
				continue;
			} else {
				cout << v / r[0] << endl;
				continue;
			}
		} else if (N == 2) {
			if (c[0] > c[1]) {
				swap(c[0], c[1]);
				swap(r[0], r[1]);
			}
			if (cmp(c[0], x) && cmp(c[0], x) == cmp(c[1], x)) {
				cout << "IMPOSSIBLE" << endl;
				continue;
			} else if(cmp(c[0], x) == 0 || cmp(c[1], x) == 0) {
				double R = cmp(c[0], x) == 0 ? r[0] : 0;
				R += cmp(c[1], x) == 0 ? r[1] : 0;
				cout << v / R << endl;
				continue;
			} else {
				double v1 = v * (x - c[0]) / (c[1] - c[0]);
				double v0 = v * (c[1] - x) / (c[1] - c[0]);
				cout << max(v0 / r[0], v1 / r[1]) << endl;
				continue;
			}
		}
	}
}
