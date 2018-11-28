/*
 * Michał Łazowik
 *
 * Google Code Jam 2014
 * Qualification Round
 * Problem A. Magic Trick
 *
 */

#include <cstdio>

#define REP(x, n) for (int x = 0; x < n; ++x)
#define FOR(x, b, e) for (int x = b; x <= (e); ++x)

int main() {
	int q, row, a, tab[17], res;

	scanf("%d", &q);

	FOR(i, 1, q) {
		REP(i, 17) tab[i] = false;

		scanf("%d", &row);
		FOR(j, 1, 4) {
			REP(k, 4) {
				scanf("%d", &a);
				if (j == row) {
					tab[a] = true;
				}
			}
		}

		res = -1;
		scanf("%d", &row);
		FOR(j, 1, 4) {
			REP(k, 4) {
				scanf("%d", &a);
				if (j == row && tab[a]) {
					switch(res) {
						case -1: res = a; break;
						case 0: break;
						default: res = 0; break;
					}
				}
			}
		}

		printf("Case #%d: ", i);
		switch(res) {
			case -1: printf("Volunteer cheated!\n"); break;
			case 0: printf("Bad magician!\n"); break;
			default: printf("%d\n", res); break;
		}
	}

	return 0;
}
