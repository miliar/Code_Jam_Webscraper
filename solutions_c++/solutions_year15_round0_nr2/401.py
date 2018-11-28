#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

void solve() {
	int D; cin >> D;
	vector<int> p(D); for (int i = 0; i < D; ++i) cin >> p[i];

	int res = 1 << 30;

	for (int k = 1; k <= 1000; ++k) {
		int cur = k;
		for (int i = 0; i < D; ++i) cur += (p[i] + k - 1) / k - 1;
		res = min(res, cur);
	}

	static int test;
	cout << "Case #" << ++test << ": " << res << endl;
	cerr << "Case #" << test << ": " << res << endl;
}

int main() {
	int t;
	cin >> t;
	while (t --> 0)
		solve();
	return 0;
}