

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
	double C, F, X;
	for (int q = 0; q < Q; q++) {
		scanf("%lf", &C);
		scanf("%lf", &F);
		scanf("%lf", &X);
		double bestt = -1;
		double edget = 0;
		double r = 2.0 - F;
		while (true) {
			double t = edget + X / (r + F);
			if (bestt == -1 || t < bestt) {
				r += F;
				edget += C / r;
				bestt = t;
			} else {
				break;  // found;
			}
		}
		printf("Case #%d: %.7lf\n", q + 1, bestt);
	}
	return 0;
}
