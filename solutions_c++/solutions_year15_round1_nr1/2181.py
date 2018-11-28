#include <stdio.h>


int main() {
	int t;
	scanf("%d", &t);

	for(int i = 1; i <= t; i++) {
		int n, numbers[1001];
		scanf("%d", &n);

		for(int j = 0; j < n; j++) {
			scanf("%d", &numbers[j]);
		}

		int method1 = 0, max = 0;
		for(int j = 1, k = 0; j < n; j++, k++) {
			int temp = numbers[k] - numbers[j];

			if(temp > 0) {
				method1 += temp;

				if(temp > max)
					max = temp;
			}
		}

		int method2 = 0, finish = n-1;
		for(int j = 0; j < finish; j++) {
			if(numbers[j] > max)
				method2 += max;
			else
				method2 += numbers[j];
		}

		printf("Case #%d: %d %d\n", i, method1, method2);
	}

	return 0;
}