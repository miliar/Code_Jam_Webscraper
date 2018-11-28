#include <cstdio>

int main() {
	int tests, cards_init[4][4], cards_final[4][4], line_init, line_final, match, match_count;
	scanf("%d", &tests);
	for (int t = 1; t <= tests; t++) {
		scanf("%d", &line_init);
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d", &cards_init[i][j]);
			}
		}
		scanf("%d", &line_final);
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d", &cards_final[i][j]);
			}
		}
		line_init--; // the matricex cards_init is 0-indexed
		line_final--; // the matricex cards_final is 0-indexed
		match_count = 0;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				//printf("%d %d : %d %d\n", i, cards_init[line_init][i], j, cards_final[line_final][j]);
				if (cards_init[line_init][i] == cards_final[line_final][j]) {
					match_count++;
					match = cards_init[line_init][i];
				}
			}
		}
		if (match_count == 0)
			printf("Case #%d: Volunteer cheated!\n", t);
		else if (match_count > 1)
			printf("Case #%d: Bad magician!\n", t);
		else
			printf("Case #%d: %d\n", t, match);
	}
	return 0;
}