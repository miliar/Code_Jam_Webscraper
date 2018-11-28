#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

typedef vector<double> vd;

double f(vd d) {
	int n = d.size();
	vector<vd> f(n + 1, vd(n + 1));
	f[0][0] = 1;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j <= i; ++j) {
			f[i + 1][j] += f[i][j] * d[i];
			f[i + 1][j + 1] += f[i][j] * (1 - d[i]);
		}
	}
	return f[n][n / 2];
}

double f1(int k, vd d) {
	double res = 0;
	for (int m = 1; m < (1 << d.size()); ++m) {
		vd x;
		for (int i = 0; i < d.size(); ++i) if (m & (1 << i))
			x.push_back(d[i]);
		if (x.size() == k)
			res = max(res, f(x));
	}
	return res;
}

double f2(int k, vd d) {
	double res = 0;
	sort(d.begin(), d.end());
	for (int i = 0; i <= k; ++i) {
		vd x(d.begin(), d.begin() + i);
		for (int j = i+1; j <= k; ++j)
			x.push_back(d[d.size() - 1 + j - k]);
		res = max(res, f(x));
	}

	for (int i = 0; i + k <= d.size(); ++i) {
		vd x(d.begin() + i, d.begin() + i + k);
		res = max(res, f(x));
	}
	return res;
}

void solve() {
	int n, k;
	cin >> n >> k;
	vd d(n);
	for (int i = 0; i < n; ++i) cin >> d[i];

	cerr << fixed;
	cerr.precision(20);
	if (d.size() <= 22)
		cerr << abs(f1(k, d) - f2(k, d)) << endl;
	
	static int test_id;
	cout << fixed;
	cout.precision(15);
	cout << "Case #" << ++test_id << ": " << f2(k, d) << endl;
}

int main() {
	int t;
	cin >> t;
	while (t-->0)solve();
	return 0;
}