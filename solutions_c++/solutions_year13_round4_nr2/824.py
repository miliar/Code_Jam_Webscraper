#include <stdio.h>

int best[1024];
int worst[1024];

void
calcBest(int N, int k) {
	int S = k;	
	int B = (1 << N) - (k + 1);
	int place = 0;
	for (int i = 0; i < N; i++) {
		if (B == 0) {
			place = (place << 1) + 1;
		} else {
			place = (place << 1);
			// update B, S
			int tot = (B + S + 1) / 2;

			S = (S + 1) / 2;
			B = tot - 1 - S; 
		}
	}
	best[k] = place;
}

void calcWorst(int N, int k) {
	int S = k;
	int B = (1 << N) - (k + 1);
	int place = 0;
	for (int i = 0; i < N; i++) {
		// printf("S %d, B %d\n", S, B); // TODO
		if (S == 0) {
			place = (place << 1);
		} else {
			place = (place << 1) + 1;
			// update B, S
			int tot = (B + S + 1) / 2;

			/*
			if (S - 1 <= B) {
				S = S - 1;
			} else {
				S = B + (S - 1 - B) / 2;
			}
			B = tot - 1 - S;
			 */
			S = (S - 1) / 2;
			B = tot - 1 - S;
		}
	}
	// printf("place %d\n", place); // TODO
	worst[k] = place;
}

int 
main(void) {
	int T, seq;
	int N, P;

	// calcWorst(3, 2); return 0; // TODO
	scanf("%d", &T);
	for (seq = 1; seq <= T; seq++) {
		scanf("%d%d", &N, &P);

		for (int i = 0; i < (1 << N); i++) {
			calcBest(N, i);
			calcWorst(N, i);
		}
	
		int a = 0, b = 0;
		// fprintf(stderr, "Dump places\n"); // TODO
		for (int i = 0; i < (1 << N); i++) {
			// fprintf(stderr, "-[%d] %d %d\n", i, best[i], worst[i]);
			if (best[i] < P) {
				b = i;
			}
			if (worst[i] < P) {
				a = i;
			}
		}
		printf("Case #%d: %d %d\n", seq, a, b);
	}
	return 0;
}
