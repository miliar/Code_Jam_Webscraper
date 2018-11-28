#include <stdio.h>
#include <string.h>

int n;
char s[1010];

bool check(int cnt) {
	for (int i = 0; s[i]; i++) {
		//printf("cnt = %d\n", cnt);
		if (cnt < i) return false;
		cnt += s[i] - '0';
	}
	return true;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		int smax;
		scanf("%d", &smax);
		scanf("%s", s);
		//puts(s);
		for (int ans = 0; ans <= smax; ans++) {
			if (check(ans)) {
				printf("Case #%d: %d\n", cas, ans);
				break;
			}
		}
	}
}