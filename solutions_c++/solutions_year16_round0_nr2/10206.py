#include <cstdlib>
#include <cstdio>
#include <cstring>
const int S = 101;
int solve(const char *buf, int len) {
	int result = 0;
	if (buf[0] == '-') {
		result = 1;
	}
	for (int i = 1; i < len; i++) {
		if (buf[i] != buf[i-1] && buf[i] == '-') {
			result += 2;
		}
	}
	return result;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		char buf[S];
		scanf("%s", buf);
		printf("Case #%d: %d\n", t, solve(buf, strlen(buf)));
	}
	return 0;
}
