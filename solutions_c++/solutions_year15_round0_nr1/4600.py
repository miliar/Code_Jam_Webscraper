#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t, T, i, sum, n, ans, p;
	char c;
	cin >> T;
	
	for (t = 0; t < T; ++t) {
		ans = 0;
		sum = 0;
		cin >> n;
		for (i = 0; i <= n; ++i) {
			cin >> c;
			p = c - '0';
			if (i)
				if (sum < i && p) {
					ans += (i - sum);
					sum = i;
				}
			sum += p;
		}
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
	return 0;
}