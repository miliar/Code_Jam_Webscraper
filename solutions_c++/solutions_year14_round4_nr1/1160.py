//In the name of God
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 1e5 + 5;

int n, x, a[N];

int main() {
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int test = 1; test <= T; test++) {
		cout << "Case #" << test << ": ";
		cin >> n >> x;
		for (int i = 0; i < n; i++)
			cin >> a[i];
		sort(a, a + n);
		int ans = n, st = 0, ed = n - 1;
		while (st < ed) {
			if (a[st] + a[ed] <= x) {
				ans--;
				st++;
				ed--;
			}
			else
				ed--;
		}
		cout << ans << '\n';
	}
	return 0;
}
