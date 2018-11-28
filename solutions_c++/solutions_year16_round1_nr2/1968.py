#include<stdio.h>
#include<stdlib.h>

int check[3000];
int answer[3000];

int compare(const void * a, const void * b) {
	if (*(int *)a > *(int*)b) {
		return 1;
	}
	else if (*(int *)a < *(int*)b) {
		return -1;
	}
	else {
		return 0;
	}
}

int main(void) {
	int T;
	int N;
	int i, j, k;
	int temp;

	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &T);

	for (i = 1; i <= T; i++) {
		for (j = 0; j < 3000; j++) {
			check[j] = 0;
			answer[j] = 0;
		}
		scanf("%d", &N);
		for (j = 0; j < 2 * N - 1; j++) {
			for (k = 0; k < N; k++) {
				scanf("%d", &temp);
				check[temp]++;
			}
		}

		for (j = 0, k = 0; j < 3000; j++) {
			if (check[j] % 2 != 0) {
				answer[k++] = j;
			}
		}

		qsort(answer, N, sizeof(int), compare);

		printf("Case #%d:", i);
		for (j = 0; j < N; j++) {
			printf(" %d", answer[j]);
		}
		printf("\n");
	}


}