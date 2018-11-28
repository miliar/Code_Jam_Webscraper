#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve_war(vector<double> a, vector<double> b) {
	int n = 0;
	for (int i = 0; i < int(a.size()); ++i) {
		double wa, wb;
		wa = a[i];
		auto it = lower_bound(b.begin(), b.end(), wa);
		if (it == b.end()) {
			wb = b.front();
			b.erase(b.begin());
		} else {
			wb = *it;
			b.erase(it);
		}
		if (wa > wb) ++n;
	}
	return n;
}

int solve_dec(vector<double>& a, vector<double>& b) {
	int n = 0;
	for (int i = 0; i < int(a.size()); ++i) {
		double wa, wb;
		if (a[i] > b.front()) {
			wa = 1;
		} else {
			wa = max(a[i], b.back() - 1e-9);
		}
		auto it = lower_bound(b.begin(), b.end(), wa);
		if (it == b.end()) {
			wb = b.front();
			b.erase(b.begin());
		} else {
			wb = *it;
			b.erase(it);
		}
		if (wa > wb) ++n;
	}
	return n;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int N;
		cin >> N;
		vector<double> a(N), b(N);
		for (auto &x : a) cin >> x;
		for (auto &x : b) cin >> x;
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		cout << "Case #" << t << ": " << solve_dec(a, b) << " " << solve_war(a, b) << endl;
	}
}
