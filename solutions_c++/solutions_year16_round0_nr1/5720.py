#include <bits/stdc++.h>

using namespace std;

int main() {
	int T, N, cur, d;
	scanf("%d", &T);

	bool digits[10];
	int left;
	int mult;
	for (int i = 0; i < T; i++) {
		memset(digits, false, sizeof digits);
		left = 10;
		mult = 0;

		scanf("%d", &N);

		if (N == 0) {
			printf("Case #%d: INSOMNIA\n", i + 1);
			continue;
		}

		do {
			cur = ++mult * N;
			while (cur > 0) {
				d = cur % 10;
				if (!digits[d]) {
					digits[d] = true;
					left--;
				}
				cur /= 10;
			}
		} while (left > 0);

		printf("Case #%d: %d\n", i + 1, mult * N);
	}

	return 0;
}