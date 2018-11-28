#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char s[1010];

int main() {
	int T;
	int _42=1;
	scanf(" %d ", &T);
	while (T--) {
		scanf(" %*d %s ", s);
		int ans = 0;
		int sum = 0;
		int size = strlen(s);
		for (int i = 0; i < size; i++) {
			if (i > sum) {
				ans += i - sum;
				sum += (i - sum) + (s[i]-'0');
			}
			else {
				sum += (s[i] - '0');
			}
		}
		printf("Case #%d: %d\n", _42++, ans);
	}
	return 0;
}
