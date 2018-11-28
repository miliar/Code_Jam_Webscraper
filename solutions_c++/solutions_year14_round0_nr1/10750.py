/**
 * 2014 Google Code Jam R0 - A
 * https://code.google.com/codejam/contest/2974486/dashboard#s=p0
 */

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

#define N 16

int TRUE = 0; // Kenneth's trick

int appeared1[N+1];
int appeared2[N+1];

int main(int argc, char** argv) {

	int kase, serial = 0;
	int row1, row2;
	int x, card;

	scanf("%d", &kase);
	while (kase--) {
		// begin test case

		++TRUE;
		if (TRUE > 10000) {
			TRUE = 10000;
			memset(appeared1, 0, sizeof(appeared1));
			memset(appeared2, 0, sizeof(appeared2));
		}

		scanf("%d", &row1);
		for (int r=1; r<=4; ++r) {
			for (int c=0; c<4; ++c) {
				scanf("%d", &x);
				if (r == row1) {
					appeared1[x] = TRUE;
				}
			}
		}

		scanf("%d", &row2);
		for (int r=1; r<=4; ++r) {
			for (int c=0; c<4; ++c) {
				scanf("%d", &x);
				if (r == row2) {
					appeared2[x] = TRUE;
				}
			}
		}

		card = 0; //
		for (int i=1; i<=N; ++i) {
			if (appeared1[i] == TRUE && appeared2[i] == TRUE) {
				if (0 == card) {
					card = i;
				} else if (card > 0) {
					card = -1; // multiple collisions
				}
			}
		}

		printf("Case #%d: ", ++serial);
		if (card > 0) {
			printf("%d\n", card);
		} else if (-1 == card) {
			puts("Bad magician!");
		} else {
			puts("Volunteer cheated!");
		}

		// end test case
	}

	return 0;
}

