#include <bits/stdc++.h>

using namespace std;

#define double long double

const int M = 120;
const double eps = 1e-13;

int n;
double V, X;
double r[M], x[M];

void read() {
	cin >> n;
	cin >> V >> X;
	for (int i = 0; i < n; ++i) {
		cin >> r[i] >> x[i];
	}

	for (int i = 0; i < n; ++i)
		for (int j = 0; j + 1 < n; ++j)
			if (x[j + 1] < x[j])
				swap(x[j + 1], x[j]),
				swap(r[j + 1], r[j]);
}

bool pos(double m) {
	double mint = 0, maxt = 0;

	double sum = 0;
	for (int i = 0; i < n; ++i) {
		double d = min(1.0 - sum, m * r[i]);
		mint += d * x[i];
		sum += d;
	}

	if (sum < 1 - eps)
		return false;

	sum = 0;
	for (int i = n - 1; i >= 0; --i) {
		double d = min(1.0 - sum, m * r[i]);
		maxt += d * x[i];
		sum += d;
	}

	if (sum < 1 - eps)
		return false;


	return mint - eps <= X && X <= maxt + eps;
}

void kill() {
	double l = 0, r = 123456789, m;
	for (int i = 0; i < 200; ++i) {
		m = (l + r) / 2.0;
		if (pos(m))
			r = m;
		else
			l = m;
	}
	//cerr << l << " " << r << "\n";
	if (pos(r))
		cout << l * V << "\n";
	else
		cout << "IMPOSSIBLE\n";
}

int main() {
	cout.precision(9);
	cout << fixed;
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		read();
		cout << "Case #" << i << ": ";
		kill();
	}
}