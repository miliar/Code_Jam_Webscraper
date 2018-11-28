#include <stdio.h>
int n, r, p, s, a[9][9], w[9], b[9], answer[9];
// P R S

int rt(int first, int second) {
	if (first == second) { return -1; }
	if (first + second == 4) {
		return 3;
	}
	return first > second ? second : first;
}

bool recall(int k) {
	if (k > b[n]) {
		for (int i = n - 1; i >= 0; i--) {
			for (int j = 1; j <= b[i]; j++) {
				a[i][j] = rt(a[i + 1][j * 2 - 1], a[i + 1][j * 2]);
				if (a[i][j] < 0) {
					return false;
				}
			}
		}
		for (int i = 1; i <= b[n]; i++) {
			answer[i] = a[n][i];
		}
		return true;
	}
	else {
		for (int i = 1; i <= 3; i++) {
			if (w[i] > 0) {
				w[i]--;
				a[n][k] = i;
				bool flag = recall(k + 1);
				if (flag) {
					return true;
				}
				w[i]++;
			}
		}
	}
	return false;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);

	for (int tt = 1; tt <= t; tt++) {
		//scanf("%d %d %d %d", &n, &r, &p, &s);
		scanf("%d %d %d %d", &n, &w[2], &w[1], &w[3]);
		b[0] = 1;
		for (int i = 1; i <= n; i++) {
			b[i] = b[i - 1] * 2;
		}
		for (int i = 1; i <= b[n]; i++) {
			answer[i] = 0;
		}
		recall(1);
		printf("Case #%d: ", tt);
		if (answer[1] == 0) {
			printf("IMPOSSIBLE\n");
		}
		else {
			for (int i = 1; i <= b[n]; i++) {
				if (answer[i] == 1) {
					printf("P");
				}
				if (answer[i] == 2) {
					printf("R");
				}
				if (answer[i] == 3) {
					printf("S");
				}
			}
			printf("\n");
		}
	}
	return 0;
}
