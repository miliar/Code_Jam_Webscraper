#include <bits/stdc++.h>
using namespace std;

void solve() {
	int n, k;
	cin >> n >> k;
	vector<double> p(n);
	for(double &i : p) {
		cin >> i;
	}
	double best = 0;
	for(int mask = 0; mask < 1 << n; ++mask) {
		vector<double> select;
		for(int i = 0; i < n; ++i) {
			if(mask & 1 << i) {
				select.push_back(p[i]);
			}
		}
		if(select.size() == k) {
			double total = 0;
			for(int mask = 0; mask < 1 << k; ++mask) {
				int count = 0;
				double p = 1;
				for(int i = 0; i < k; ++i) {
					count += !!(mask & 1 << i);
					p *= mask & 1 << i ? select[i] : 1 - select[i];
				}
				if(count == k / 2) {
					total += p;
				}
			}
			best = max(best, total);
		}
	}
	cout << ' ' << best << '\n';
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ':';
		solve();
	}
	return 0;
}
