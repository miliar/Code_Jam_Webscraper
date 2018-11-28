#include <cstdio>
#include <cstdlib>
#include <cstring>

void original_sequence (char* s, int pattern) {
	while (pattern) {
		*s = pattern % 2 == 0 ? 'L' : '.';
		++s;
		pattern /= 2;
	}
}

unsigned long long ipow(unsigned long long a, unsigned long long n) {
	unsigned long long result = 1;
	for (; n; --n)
		result*= a;
	return result;
}

int main(int argc, char const *argv[]) {

	
	int T, K, C, S;
	scanf("%d", &T);

	for (int i = 0; i < T; ++i) {
		scanf("%d %d %d", &K, &C, &S);
		printf("Case #%d:", i+1);
		// printf("Case #%d (%d %d %d):\n", i+1, K, C, S);

		if (K == 1)  {
			printf(" %d\n", 1);
			continue;
		}
		unsigned long long coef = (ipow(K, C) - 1) / (K - 1);
		for (int i = 0; i < K; ++i) {
			printf(" %ld", i * coef + 1);
		}
		printf("\n");

	}

	return 0;
}
