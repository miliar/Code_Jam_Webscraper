#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstdio>
#include <cstdlib>
using namespace std;

int cas, n, t, si, bad, ans, st;
vector <int> a;

int main () {
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	cin >> cas;
	for (int o = 1; o <= cas; o++) {
		cin >> si >> n;
		a.clear();
		a.resize(n + 1);
		st = si;
		for (int i = 1; i <= n; i++) {
			cin >> a[i];
		}
		sort(a.begin() + 1, a.begin() + 1 + n);
		int i = 1;
		for (i = 1; i <= n; i++) {
			if (si > a[i]) {
				si += a[i];
			} else {
				break;
			}
		}
		bad = n - i + 1;
		int cnt = 0;
		ans = bad;
		if (i != n + 1) {
			for (; i <= n; i++) {
				if (si == 1) {
					break;
				}
				if (si > a[i]) {
					si += a[i];
					bad--;
				} else {
					si += si - 1;
					cnt++;
					i--;
				}
				ans = min(ans, cnt  + bad);
			}
		}
		cout << "Case #" << o << ": " << ans << "\n";
	}
	return 0;
}