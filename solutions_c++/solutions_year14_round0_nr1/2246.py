

#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>

int A0[16], A1[16];
int r0, r1;
int C[8];

int compare(const void *a, const void *b) {
	int ia = * (int *) a;
	int ib = * (int *) b;
	return ia - ib;
}

int main(void) {
	int Q;
	scanf("%d", &Q);
	for (int q = 0; q < Q; q++) {
		scanf("%d", &r0);
		for (int i = 0; i < 16; i++) scanf("%d", &A0[i]);
		scanf("%d", &r1);
		for (int i = 0; i < 16; i++) scanf("%d", &A1[i]);

		r0--;
		r1--;
		for (int i = 0; i < 4; i++) {
			C[i] = A0[r0 * 4 + i];
			C[4 + i] = A1[r1 * 4 + i];
		}
		// printf("%d %d %d %d -- %d %d %d %d\n", C[0], C[1], C[2], C[3], C[4], C[5], C[6], C[7]);
		qsort(C, 8, sizeof(int), compare);
		// printf("%d %d %d %d -- %d %d %d %d\n", C[0], C[1], C[2], C[3], C[4], C[5], C[6], C[7]);
		int same = 0;
		int same_ = 0;
		for (int i = 1; i < 8; i++) {
			if (C[i] == C[i - 1]) {
				same++;
				same_ = C[i];
			}
		}
		if (same == 1) {
			printf("Case #%d: %d\n", q + 1, same_);
		} else if (same == 0) {
			printf("Case #%d: Volunteer cheated!\n", q + 1);
		} else {
			printf("Case #%d: Bad magician!\n", q + 1);
		}
	}
	return 0;
}
