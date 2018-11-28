#include <iostream>

using namespace std;

void solve()
{
	int k, c, s;
	cin >> k >> c >> s;
	if (s == 1) {
		if (k > 1) cout << "IMPOSSIBLE\n";
		else cout << "1\n";
		return;
	}
	if (c == 1) {
		if (s < k) cout << "IMPOSSIBLE\n";
		else {
			for (int i = 1; i < k; i++) cout << i << " ";
			cout << k << endl;
		}
		return;
	}
	long long kc = 1;
	for (int i = 2; i <= min(s, k); i++) cout << i << " ";
	for (int i = 0; i < c; i++) kc *= k;
	cout << kc - 1 << endl;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
