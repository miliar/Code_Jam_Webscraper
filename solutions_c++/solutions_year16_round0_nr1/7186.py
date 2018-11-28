#include <cstdio>

int main(int argc, char** argv) {
	int numLines;
	scanf("%d", &numLines);
	for (int l = 1; l <= numLines; l++) {
		int N;
		scanf("%d", &N);

		printf("Case #%d: ", l);

		if (N == 0) {
			printf("INSOMNIA\n");
			continue;
		}

		bool seen[10]; // digits 0-9
		for (int i = 0; i < 10; i++) {
			seen[i] = false;
		}
		int numSeen = 0;
		int lastNum = N;
		int originalN = N;
		while (numSeen < 10) {
			int num = N;
			lastNum = N;
			while (num > 0) {
				int sd = num % 10;
				if (!seen[sd]) {
					seen[sd] = true;
					numSeen++;
				}
				num /= 10;
			}
			N += originalN;
		}
		printf("%d\n", lastNum);
	}

	return 0;
}
