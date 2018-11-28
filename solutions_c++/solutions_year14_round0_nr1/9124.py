#include <stdio.h>
#include <stdlib.h>

int process(int caseNum) {
	int n, j, k, num;
	int card = NULL;
	int check[17] = {0, };

	scanf("%d", &n);
	for(j = 1; j <= 4; j++) {
		for(k = 0; k < 4; k++) {
			scanf("%d", &num);
			if(j == n) {
				check[num]++;
			}
		}
	}
	scanf("%d", &n);
	for(j = 1; j <= 4; j++) {
		for(k = 0; k < 4; k++) {
			scanf("%d", &num);
			if(j == n) {
				check[num]++;
			}
		}
	}

	for(j = 1; j <= 16; j++) {
		if(check[j] == 2) {
			if(card != NULL) {
				printf("Case #%d: Bad magician!\n", caseNum);
				return 0;
			}
			card = j;
		}
	}

	if(card == NULL) {
		printf("Case #%d: Volunteer cheated!\n", caseNum);
	}
	else {
		printf("Case #%d: %d\n", caseNum, card);
	}

	return 0;
}

int main() {
	int i, t;
	scanf("%d", &t);
	for(i = 1; i <= t; i++) {
		process(i);
	}
	return 0;
}