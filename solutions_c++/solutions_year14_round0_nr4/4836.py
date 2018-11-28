//In the name of God
#include <algorithm>
#include <iostream>
#include <queue>
using namespace std;

int n;
deque<double> a, b, c, d;

int main() {
	ios_base::sync_with_stdio(false);
	int test; cin >> test;
	for (int k = 1; k <= test; k++) {
		cin >> n;
		a.resize(n), b.resize(n);
		for (int i = 0; i < n; i++)
			cin >> a[i];
		for (int i = 0; i < n; i++)
			cin >> b[i];
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		c = a; d = b;
		int ans1 = 0, ans2 = 0;
		while (!a.empty()) {
			if (b.back() > a.back())
				b.pop_back();
			else
				b.pop_front(), ans1++;
			a.pop_back();
		}
		a = c, b = d;
		for (int i = 0; i < n; i++) {
			if (a[i] > b.front()) {
				b.pop_front();
				ans2++;
			}
			else
				b.pop_back();
		}
		cout << "Case #" << k << ": " << ans2 << ' ' << ans1 << '\n';
	}
	return 0;
}
