#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t, it, d, i, j, current, min, ans, v[1000], maxim;
	cin >> t;
	for (it = 1; it <= t; it++) {
		cin >> d;
		maxim = -1;
		ans = INT_MAX;
		for (i = 0; i < d; i++) {
			cin >> v[i];
			if (v[i] > maxim) {
				maxim = v[i];
			}
		}
		for (i = 1; i <= maxim; i++) {
			current = i;
			for (j = 0; j < d; j++) {
				if (v[j] % i == 0) current += v[j] / i;
				else current += v[j] / i + 1;
				current--;
			}
			if (current < ans) {
				ans = current;
			}
		}
		cout << "Case #" << it << ": " << ans << '\n';
	}
	return 0;
}