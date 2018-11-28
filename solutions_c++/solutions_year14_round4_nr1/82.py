#include <iostream>
#include <string>
#include <algorithm>


using namespace std;

int n, m;
int a[10500], b[10500];

void solve() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) cin >> a[i], b[i] = 0;
	int ans = 0;
	sort(a, a + n);
	reverse(a, a + n);
	for (int i = 0, j = 0; i < n; i++) {
		if (b[i]) continue;
		ans++;
		j = i + 1;
		while (j < n && (b[j] || a[j] + a[i] > m)) j++;
		if (j < n) b[j] = 1;
	}
	cout << ans;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
	}
}