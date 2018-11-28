#include <iostream>
#include <cstdio>

using namespace std;

int T, ans1, ans2, a[4][4], b[4][4], ans, cnt;

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	cin >> T;
	for (int t = 0; t < T; t++) {
		cin >> ans1;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> a[i][j];
			}
		}
		cin >> ans2;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> b[i][j];
			}
		}
		cnt = 0;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (a[ans1 - 1][i] == b[ans2 - 1][j]) {
					cnt++;
					ans = a[ans1 - 1][i];
				}
			}
		}
		if (cnt == 0) {
			printf("Case #%d: Volunteer cheated!\n", t + 1);
		} else if (cnt == 1) {
			printf("Case #%d: %d\n", t + 1, ans);
		} else {
			printf("Case #%d: Bad magician!\n", t + 1);
		}
	}
	return 0;
}