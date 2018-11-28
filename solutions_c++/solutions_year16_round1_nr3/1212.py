#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <time.h>

using namespace std;
const int N = 12;

vector <int> p;
int n;
bool used[N];
int mi[N];
int ans = 0;

bool check(int len) {
	if (ans >= len) return true;
	for (int i = 0; i < len; i++) {
		if (p[mi[i]] != mi[(i + 1) % len] && p[mi[i]] != mi[(i - 1 + len) % len])
			return false;
	}
	return true;
}
void calc(int pos) {
	if (pos > 0) {
		if (check(pos)) ans = max(ans, pos);
	}
	if (pos == n) return;
	for (int i = 0; i < n; i++) {
		if (!used[i]) {
			mi[pos] = i;
			used[i] = true;
			calc(pos + 1);
			used[i] = false;
		}
	}
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin.tie(0);
	cout.sync_with_stdio(false);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		memset(used, 0, sizeof used);
		cin >> n;
		p.clear();
		p = vector <int>(n);
		for (int j = 0; j < n; j++) {
			cin >> p[j];
			p[j]--;
		}
		ans = 0;
		calc(0);
		cout << "Case #" << i << ": " << ans << endl;
	}
	return t;
}