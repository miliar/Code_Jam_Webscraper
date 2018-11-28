#include <stdio.h>

int main () {
	int T, max, total, counter, val;
	char data[1100];

	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		scanf("%d %s", &max, data);
		total = counter = 0;

		for (int j = 0; j <= max; j++) {
			val = (int) data[j] - 48;
			if (j > total && val != 0) {
				counter += j - total;
				total += j - total;
			}

			total += val;
		}

		printf("Case #%d: %d\n", i, counter);
	}

	return 0;
}
