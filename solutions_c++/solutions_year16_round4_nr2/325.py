#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <limits>
#include <algorithm>
#include <ctime>
#include <unordered_map>
#include <unordered_set>
#include <cstring>

using namespace std;

const int MAXN = 205;

int cs = 0, n, ans, k;
double p[MAXN];
double f[MAXN][MAXN][MAXN * 2];

vector<double> ps;
double calc() {
	vector<double> f1, f2;
	f1.push_back(1);
	for (size_t i = 0; i < ps.size(); ++i) {
		f2.resize(f1.size() + 2);
		fill_n(f2.begin(), f2.size(), 0.0);
		for (size_t j = 0; j < f1.size(); ++j) {
			f2[j] += (1 - ps[i]) * f1[j];
			f2[j + 2] += ps[i] * f1[j];
		}
		f1.swap(f2);
	}
	return f1[f1.size() / 2];
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	cin >> t;
	while (t--) {
		cin >> n >> k;
		for (int i = 0; i < n; ++i) {
			cin >> p[i];
		}
		sort(p, p + n);
		double ans = 0.0;
		for (int i = 0; i <= k; ++i) {
			ps.clear();
			for (int j = 0; j < i; ++j)
				ps.push_back(p[j]);
			for (int j = 0; j < k - i; ++j)
				ps.push_back(p[n - 1 - j]);
			ans = max(ans, calc());
		}
		printf("Case #%d: ", ++cs);
		printf("%.10f\n", ans);

	}
	return 0;
}
