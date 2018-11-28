#include <cstdio>

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		long long N, num;
		int mtp;
		bool digit[10] = {0};
		scanf("%lld", &N);
		if (N == 0) {
			printf("Case #%d: INSOMNIA\n", i);
			continue;
		}
		
		mtp = 0;
		for (int j = 0; j < 10; j++) {
			while (!digit[j]) {
				mtp++;
				num = N * mtp;
				while (num) {
					digit[(int) (num % 10)] = 1;
					num /= 10;
				}
			}
		}
		
		printf("Case #%d: %lld\n", i, N * mtp);

	}
	return 0;
}
