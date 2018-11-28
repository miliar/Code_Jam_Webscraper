#include <stdio.h>
char a[199][199];

int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, 1, 0, -1 };

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int test, n, m;
	scanf("%d", &test);

	for (int t = 1; t <= test; t++) {
		scanf("%d %d", &n, &m);
		for (int i = 1; i <= n; i++) {
			scanf("%s", a[i] + 1);
		}

		int count = 0;

		int s = 0;
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				if (a[i][j] == '^') {
					s = 0;
				}
				else if (a[i][j] == '>') {
					s = 1;
				}
				else if (a[i][j] == 'v') {
					s = 2;
				}
				else if (a[i][j] == '<') {
					s = 3;
				}
				else {
					s = -1;
				}

				if (s < 0) { continue; }


				int r, c;
				bool flag = false;

				for (int k = 1;; k++) {
					r = i + dx[s] * k;
					c = j + dy[s] * k;
					if (r < 1 || c < 1 || r > n || c > m) { break; }
					
					if (a[r][c] != '.') {
						flag = true;
						break;
					}
				}

				if (flag == false) {
					for (int l = 1; l <= 3; l++) {
						s = (s + 1) % 4;
						for (int k = 1;; k++) {
							r = i + dx[s] * k;
							c = j + dy[s] * k;
							if (r < 1 || c < 1 || r > n || c > m) { break; }

							if (a[r][c] != '.') {
								flag = true;
								count++;
								break;
							}
						}

						if (flag) { break; }
					}
				}

				if (flag == false) {
					count = -1;
					break;
				}
			}
			if (count < 0) { break; }
		}

		if (count < 0) {
			printf("Case #%d: IMPOSSIBLE\n", t);
		}
		else {
			printf("Case #%d: %d\n", t, count);
		}
	}
}