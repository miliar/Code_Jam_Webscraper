#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main() {
	int t, n;
	vector <int> a;
	cin >> t;
	int T = t;
	while (t-->0) {
		cin >> n;
		a.resize(n);
		for (int i = 0; i < n; i++) {
			cin >> a[i];
		}
		sort(a.begin(), a.end());
		int res = 10000000;
		for (int h = 1; h <= 1000; h++) {
			int cur = h;
			for (int i = 0; i < n; i++) {
				cur += (a[i] - 1) / h;
			}
			// cerr << "tst " << T- t << " ";
			// cerr << "h = " << h << " cur " << cur <<  "\n";
			res = min(res, cur);
		}
	
		cout << "Case #" << T - t << ": " << res << "\n";
	}
	return 0;
}
