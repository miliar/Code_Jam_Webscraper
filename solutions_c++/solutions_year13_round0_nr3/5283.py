/*
 * Fair.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: Jason Wu
 */

#include "Fair.h"

void QR2013::Fair::solve() {
	int T;
	int t[5] = { 1, 4, 9, 121, 484 };
	int A, B;
	int ans;

	scanf("%d", &T);

	for (int c = 1; c <= T; c++) {
		scanf("%d%d", &A, &B);
		ans = 0;

		REP(i, 5) if (t[i] >= A && t[i] <= B) ++ans;

		printf("Case #%d: %d\n", c, ans);
	}
}
/* namespace QR2013 */
