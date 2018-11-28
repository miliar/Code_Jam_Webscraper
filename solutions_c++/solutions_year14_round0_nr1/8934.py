#include <stdio.h>

using namespace std;
unsigned char cards[4][4];
unsigned char cards_two[4][4];

int main() {
	unsigned t, first, second, card;
	scanf("%d\n", &t);
	for (int i = 0; i < t; ++i) {
		unsigned char count = 0;
		scanf("%d\n", &first);
		for(int j = 0; j < 4; j++) {
			scanf("%d %d %d %d", &cards[j][0], &cards[j][1], &cards[j][2], &cards[j][3]);
		}
		scanf("%d\n", &second);
		for(int j = 0; j < 4; j++) {
			scanf("%d %d %d %d", &cards_two[j][0], &cards_two[j][1], &cards_two[j][2], &cards_two[j][3]);
		}

		for(int j = 0; j < 4; j++) {
			for(int h = 0; h < 4; h++) {
				if(cards[first-1][j] == cards_two[second-1][h]) {
					++count;
					card = cards[first-1][j];
				}
			}
		}
		if(count > 1) {
			printf("Case #%d: Bad magician!\n", i+1);
		}
		else if(count == 0) {
			printf("Case #%d: Volunteer cheated!\n", i+1);
		}
		else {
			printf("Case #%d: %d\n", i+1, card);
		}
	}

	return 0;

}