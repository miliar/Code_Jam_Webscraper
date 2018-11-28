#define _CRT_SECURE_NO_WARNINGS 1

#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>
#include <algorithm>

int A[20000];

void solve(int CASE) {
	int N;
	int C;
	scanf("%d%d", &N, &C);
	for (int i = 0; i < N; i++) scanf("%d", &A[i]);
	std::sort(A, A + N);

	int d = 0;
	int r = N;
	for (int i = N - 1; i >= 0; i--) {
		if (A[i] == 0) continue;
		int u = A[i];
		A[i] = 0;
		int j = i - 1;
		for (; j >= 0; j--) {
			if (A[j] == 0) continue;
			if (u + A[j] <= C)
				break;
		}
		if (j == -1) {
			;  // use;
		} else {
			A[j] = 0;
		}
		d++;
	}

	printf("Case #%d: %d\n", CASE, d);
}

int main(void) {
	int Q;
	scanf("%d", &Q);
	for (int q = 0; q < Q; q++) {
		solve(q + 1);
	}
	return 0;
}
