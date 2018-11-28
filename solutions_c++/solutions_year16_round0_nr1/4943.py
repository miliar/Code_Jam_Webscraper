#include<stdio.h>
#include<string.h>
bool chk[10];
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc; scanf("%d", &tc);
	for (int test = 1; test <= tc; test++) {
		int n; scanf("%d", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", test);
			continue;
		}
		int t = 0;
		int cnt = 0;
		memset(chk, 0, sizeof(chk));
		while (cnt < 10) {
			t += n;
			int tmp = t;
			while (tmp) {
				if (!chk[tmp % 10]) {
					cnt++;
					chk[tmp % 10] = true;
				}
				tmp /= 10;
			}
		}
		printf("Case #%d: %d\n", test, t);
	}
	fclose(stdin);
	fclose(stdout);
}