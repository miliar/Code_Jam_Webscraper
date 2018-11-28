// Standing Ovation

#include <cstdio>

int main() {
	int testcase, t;
	
	int len;
	char input[1005];
	int ans, count;
	int i;

	scanf("%d", &testcase);
	for (t = 1; t <= testcase; t++) {
		scanf("%d %s", &len, input);

		ans = 0;
		count = 0;
		for (i = 0; i <= len; i++) {
			if (input[i] != '0') {
				if (count < i) {
					// There isn't enough man. Invite more.
					ans += i - count;
					count += i - count;
				}
				count += input[i] - '0';
			}
		}

		printf("Case #%d: %d\n", t, ans);
	}
	
	return 0;
}