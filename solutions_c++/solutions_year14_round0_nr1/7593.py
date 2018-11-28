#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;


int main() {
	int T; scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		fprintf(stderr, "Case #%d of %d...\n", Ti, T);

		int answer1;
		scanf("%d", &answer1);
		answer1 -= 1;

		int cards1[4][4];
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				scanf("%d", &cards1[i][j]);
			}
		}

		int answer2;
		scanf("%d", &answer2);
		answer2 -= 1;
		
		int cards2[4][4];
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				scanf("%d", &cards2[i][j]);
			}
		}

		int choosed = -1;
		int count = 0;
		for (int i = 0; i < 4; ++i) {
			auto p = find(cards2[answer2], cards2[answer2] + 4, cards1[answer1][i]);
			if (p != cards2[answer2] + 4) {
				++count;
				choosed = *p;
			}
		}

		if (count == 0) {
			printf("Case #%d: Volunteer cheated!\n", Ti);
		} else if (count == 1) {
			printf("Case #%d: %d\n", Ti, choosed);
		} else {
			printf("Case #%d: Bad magician!\n", Ti);
		}
	}
	return 0;
}
