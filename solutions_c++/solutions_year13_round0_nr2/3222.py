#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

const int Max = 10;

int reverseNumber(int x) {
	int rev = 0;
	int t = x;

	while (t > 0) {
		rev = rev * 10 + t % 10;
		t /= 10;
	}

	return x == rev;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int a[200][200];
	int row[200];
	int col[200];
	int testsNum;
	int n, m;

	scanf("%d", &testsNum);
	for (int t = 0; t < testsNum; t++) {
		memset(a, 0, sizeof(a));

		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				scanf("%d", &a[i][j]);
			}
		}

		bool ok = true;
		for (int i = 0; i < n; i++) {
			int mm = 0;
			for (int j = 0; j < m; j++) {
				mm = max(mm, a[i][j]);
			}
			row[i] = mm;
		}

		for (int i = 0; i < m; i++) {
			int mm = 0;
			for (int j = 0; j < n; j++) {
				mm = max(mm, a[j][i]);
			}
			col[i] = mm;
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (a[i][j] < row[i] && a[i][j] < col[j]) {
					ok = false;
				}
			}
		}

		printf("Case #%d: %s\n", t + 1, (ok ? "YES" : "NO"));
	}

	return 0;
}