#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int T, k, c, s;
ll pw[100];

void load() {
	cin >> k >> c >> s;
}

ll find(int pos, int C = 1) {
	if (C == c) return pos;
	return pw[c - C] * (pos - 1) + find(pos, C + 1);
}

void solve(int tc) {
	assert(s == k);
	pw[0] = 1;
	for (int i = 1; i < 100; ++i) {
		pw[i] = pw[i - 1] * k;
	}
	cout << "Case #" << tc << ":";
	for (int i = 1; i <= k; ++i) {
		cout << ' ' << find(i);
	}
	cout << endl;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios_base::sync_with_stdio(false);
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		load();
		solve(tc);
	}
	return 0;
}