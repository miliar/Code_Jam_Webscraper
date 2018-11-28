/*
	Alva Thomson
*/
#include <stdio.h>
int main() {
	int TC;
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		int n;
		char dummy, ch = '#';
		scanf("%d%c", &n, &dummy);

		int sum = 0;
		int ans = 0;
		for (int s = 0; s <= n; s++) {
			scanf("%c", &ch);
			int now = ch - '0';
			if (now == 0) continue;
			if (sum < s) {
				ans += s - sum;
				sum = s;
			} 

			sum += now;
		}

		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}