#include <cstdio>

int main() {
	int T;
	scanf("%d", &T);
	for (int testCase = 1; testCase <= T; ++testCase) {
		int sMax;
		char s;
		scanf("%d ", &sMax);
		int req = 0;
		int cumSum = 0;
		for (int i = 0; i <= sMax; ++i) {
			scanf("%c", &s);
			int cur = s - '0';
			if (cumSum < i) {
				req += i - cumSum;
				cumSum = i;
			}
			cumSum += cur;
		}
		printf("Case #%d: %d\n", testCase, req);
	}
}