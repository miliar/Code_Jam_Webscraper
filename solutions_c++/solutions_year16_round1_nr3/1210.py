#include <stdio.h>

int T;
int N;
int list[1002];
bool chk[1002];
int arr[1002];
int res;

void Solve(int len, int pos) {
	int i;
	if (pos > len) {
		arr[0] = arr[len];
		arr[len + 1] = arr[1];
		bool err = false;
		for (i = 1; i <= len; i++) {
			if (!(list[arr[i]] == arr[i + 1] || list[arr[i]] == arr[i - 1])) {
				err = true; break;
			}
		}
		if (!err) res = len;
		arr[0] = 0;
		arr[len + 1] = 0;
		return;
	}
	for (i = 1; i <= N; i++) {
		if (!chk[i]) {
			chk[i] = true;
			arr[pos] = i;
			Solve(len, pos + 1);
			chk[i] = false;
			arr[pos] = 0;
		}
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	int i, j;

	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		scanf("%d", &N);
		for (i = 1; i <= N; i++)
			scanf("%d", &list[i]);

		res = 0;
		for (i = N; i >= 1; i--) {
			Solve(i, 1);
			if (res > 0) break;
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}