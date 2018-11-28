#include <iostream>
#include <algorithm>

using namespace std;

int cnt[1002];
int time, ans = 0;

void solve(int p) {
	if (p < 3) return;
	int i;
	for (i = 2; i <= p / 2; ++i) {
		cnt[i]++;
		cnt[p - i]++;
		cnt[p]--;
		time++;
		int r = p;
		while (!cnt[r]) r--;
		ans = min(ans, time + r);
		solve(r);
		cnt[i]--;
		cnt[p - i]--;
		cnt[p]++;
		time--;
	}
}

int main() {
//	freopen("input.txt", "r", stdin);
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);
	int t, T, i, j, d, p, m, h;
	cin >> T;

	for (t = 0; t < T; ++t) {
		for (i = 0; i < 1002; ++i) cnt[i] = 0;
		cin >> d;
		m = 0;
		ans = 0;
		time = 0;
		for (i = 0; i < d; ++i) {
			cin >> p;
			cnt[p]++;
			m = max(m, p);
		}
		ans = m;
		solve(m);
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
	return 0;
}