#include <cstdio>
#include <cstring>

char buf[20022];
char S[20022];
int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int t; scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		scanf("%s", buf);
		int head = 0;
		S[head++] = buf[0];
		int ans = 0;
		int n = strlen(buf);
		for (int i = 1; i < n; i++){
			if (head == 0)
				S[head++] = buf[i];
			else {
				if (buf[i] == S[head - 1]) {
					ans += 10;
					head--;
				} else S[head++] = buf[i];
			}
		}
		ans += head / 2 * 5;
		printf("Case #%d: %d\n", cas, ans);
	}
}