#include <cstdio>

int main() {
	int tests, N;
	scanf("%d", &tests);

	for (int case_no = 1; case_no <= tests; ++case_no) {
		printf("Case #%d: ", case_no);
		scanf("%d", &N);

		if (N == 0) {
			printf("INSOMNIA\n");
			continue;
		}

		bool flag[10] = {0};
		long long last = -1;

		for (int i = 1; ; ++i) {
			long long mul = i * (long long) N;
			do {
				flag[mul % 10] = 1;
				mul /= 10;
			} while (mul > 0);

			int total = 0;

			for (int d = 0; d < 10; ++d) {
				total += flag[d];
			}

			if (total == 10) {
				last = i * (long long) N;
				break;
			}
		}

		printf("%lld\n", last);
	}
}