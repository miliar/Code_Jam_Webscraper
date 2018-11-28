#include <stdio.h>

int main() {
	int T, N;

	scanf("%d", &T);

	for(int i = 1; i <= T; ++i) {
		scanf("%d", &N);

		int index, number, result;
		int named[10] = {0, };

		for(number = N, index = 2, result = 0; result < 10 && number > 0; index++) {
			for(;number > 0; number /= 10) {
				int digit = number % 10;

				if(named[digit] == 0) {
					named[digit] = 1;
					result++;
				}
			}
			number = N * index;
		}

		if(result == 10) { 
			int answer = N*(index-2);
			printf("Case #%d: %d\n", i, answer);
		}
		else {
			printf("Case #%d: INSOMNIA\n", i);
		}
	}

	return 0;
}