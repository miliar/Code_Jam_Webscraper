#include<stdio.h>
#include<stdlib.h>

int getMinMinutes(int *arr, int d) {
	int max = 0, maxind;

	for (int j = 0; j < d; ++j) {
		if (arr[j] > max) {
			max = arr[j];
			maxind = j;
		}
	}

	if (max <= 3) {
		return max;
	}

	int half = max / 2, retmin = max, max_split;
	int* narr = (int *) malloc((d + 1) * sizeof(int));

	for (int i = 0; i < d; ++i) {
		narr[i] = arr[i];
	}

	for (int i = 2; i <= half; ++i) {
		narr[maxind] = i;
		narr[d] = max - i;

		max_split = 1 + getMinMinutes(narr, d + 1);
		if (max_split < retmin) {
			retmin = max_split;
		}
	}

	free(narr);

	return retmin;
}

int main() {
	int t, d, arr[6];

	scanf("%d", &t);

	for (int i = 0; i < t; ++i) {
		scanf("%d", &d);

		for (int j = 0; j < d; ++j) {
			scanf("%d", &arr[j]);
		}

		printf("Case #%d: %d\n", i + 1, getMinMinutes(arr, d));

	}
}
