#include <stdio.h>
#include <string.h>

int main() {
	int T;
	scanf("%d", &T);
	int temp = T;
	while (T--) {
		int count = 0;
		int a[6] = { 0, 1, 4, 9, 121, 484 };
		int min, max;
		scanf("%d %d", &min, &max);
		int i, j;
		for (i = min; i <= max; i++) {
			for (j = 0; j < 6; j++)
				if (i == a[j])
					count++;
		}
		printf("Case #%d: %d\n", temp - T, count);
	}
	return 0;
}
