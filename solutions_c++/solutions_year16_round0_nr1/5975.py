#include <bits/stdc++.h>
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	vector<long long> ans(1000005);
	for (long long i = 1; i <= 1000000; ++i) {
		vector<bool> d(10, false);
		int c = 0;
		long long n = i, sum = 0;
		while (c != 10) {
			sum += n;
			long long x = sum;
			while (x > 0) {
				int digit = x % 10;
				x /= 10;
				if (!d[digit]) {
					c++;
					d[digit] = true;
				}
			}
		}
		ans[i] = sum;
	}
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		int n;
		cin >> n;
		if (n == 0) {
			cout << "Case #" << i + 1 << ": INSOMNIA\n";
		} else {
			cout << "Case #" << i + 1 << ": " << ans[n] << '\n';
		}
	}
	return 0;
}
