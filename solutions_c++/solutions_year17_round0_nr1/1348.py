#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>

char buff[10000];

void solve() {
	int size;
	scanf("%s %d", buff, &size);
	int ans = 0;
	int len = strlen(buff);
	for (int i = 0; i < len; ++i) {
		if (buff[i] == '+') {
			continue;
		}
		if (i + size > len) {
			printf("IMPOSSIBLE\n");
			return;
		}
		ans += 1;
		for (int j = 0; j < size; ++j) {
			int pos = i + j;
			if (buff[pos] == '-') {
				buff[pos] = '+';
			} else {
				buff[pos] = '-';
			}
		}
	}
	printf("%d\n", ans);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}