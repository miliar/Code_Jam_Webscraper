#include <cstdio>

int main() {
	int T;
	scanf("%d", &T);

	for (int ct = 1; ct <= T; ct++) {
		int n;
		scanf("%d", &n);

		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", ct);
			continue;
		}

		int digits[10] = {0};
		long long N = 0;

		while (!digits[0] || !digits[1] \
			|| !digits[2] || !digits[3] \
			|| !digits[4] || !digits[5] \
			|| !digits[6] || !digits[7] \
			|| !digits[8] || !digits[9]) {
			N += n;
			long long aux = N;
			while (aux) {
				digits[aux % 10]++;
				aux /= 10;
			}
		}

		printf("Case #%d: %lld\n", ct, N);
	}


	return 0;
}