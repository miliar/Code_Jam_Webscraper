/*
 * sol.cpp
 *
 *  Created on: May 11, 2014
 *      Author: song
 */

#include<math.h>
#include<stdio.h>
#include<string.h>

int main() {
	freopen("/home/song/Downloads/Code/input", "r", stdin);
	freopen("/home/song/Downloads/Code/output", "w", stdout);
	int T, count, i, j, k;
	long long lli, llj, llk, P, Q;
	scanf("%d", &T);
	for (count = 1; count <= T; count++) {
		scanf("%ld/%ld", &P, &Q);
		printf("Case #%d: ", count);
		while (Q % 2 == 0 && P % 2 == 0) {
			Q /= 2;
			P /= 2;
		}
		if (Q % 2 != 0) {
			printf("impossible\n");
			continue;
		}
		for (i = 0; i < 40; i++) {
			P *= 2;
		}
		if (P % Q != 0) {
			printf("impossible\n");
			continue;
		}
		for (j = 40; j >0; j--) {
			if (pow(2, j) * Q <= P)
				break;
		}
		printf("%d\n", 40 - j);
	}
	return 0;
}
