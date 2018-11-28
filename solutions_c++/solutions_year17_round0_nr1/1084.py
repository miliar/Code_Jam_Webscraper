#include <cstdio>
#include <cstring>

int main() {
	char buf[1024];
	int T;
	int i, j, k;

	memset(buf, 0x00, sizeof(buf));
	fgets(buf, 1024, stdin);

	sscanf(buf, "%d", &T);

	for (i = 0; i < T; ++i) {
		char S[1024];
		int K;
		int flips = 0;
		memset(buf, 0x00, sizeof(buf));
		memset(S, 0x00, sizeof(S));

		fgets(buf, 1024, stdin);

		sscanf(buf, "%s %d", S, &K);

		int len = strlen(S);

		for (j = 0; j <= len - K; ++j) {
			if (S[j] == '-') {
				++flips;

				for (k = j; k < j + K; ++k) {
					if (S[k] == '+')
						S[k] = '-';
					else
						S[k] = '+';
				}
			}
		}

		for (j = len - K; j < len; ++j) {
			if (S[j] == '-') {
				flips = -1;
				break;
			}
		}

		if (flips >= 0)
			printf("Case #%d: %d\n", i + 1, flips);
		else
			printf("Case #%d: IMPOSSIBLE\n", i + 1);
	}

	return 0;
}
