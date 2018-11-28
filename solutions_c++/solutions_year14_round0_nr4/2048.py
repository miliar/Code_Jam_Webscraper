#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>

double A[2000], B[2000];
int N;

int compare(const void *a, const void *b) {
	double ia = * (double *) a;
	double ib = * (double *) b;
	return ia < ib ? -1 : 1;
}

int main(void) {
	int Q;
	scanf("%d", &Q);
	for (int q = 0; q < Q; q++) {
		scanf("%d", &N);
		for (int i = 0; i < N; i++) {
			scanf("%lf", &A[i]);
		}
		for (int i = 0; i < N; i++) {
			scanf("%lf", &B[i]);
		}
		qsort(A, N, sizeof(double), compare);
		qsort(B, N, sizeof(double), compare);


		// deceit;

		int deceitWin = 0;
		int Amin = 0, Amax = N - 1;
		int Bmin = 0, Bmax = N - 1;
		for (int i = 0; i < N; i++) {
			if (A[Amin] > B[Bmin]) {  // force win;
				Amin++;
				Bmin++;
				deceitWin++;
			} else {
				Amin++;
				Bmax--;
			}
		}

		int warWin = 0;

		Amin = 0, Amax = N - 1;
		Bmin = 0, Bmax = N - 1;
		for (int i = 0; i < N; i++) {
			double a = A[Amin]; Amin++;
			if (a > B[Bmax]) {  // well, B choose to lose to A;
				Bmin++;
				warWin++;
			} else {
				int j = Bmin;
				while (a > B[j]) j++;
				;  // beats A with B[j];
				for (int k = j; k > Bmin; k--) B[k] = B[k - 1];
				Bmin++;
			}
		}

		printf("Case #%d: %d %d\n", q + 1, deceitWin, warWin);
	}
	return 0;
}
