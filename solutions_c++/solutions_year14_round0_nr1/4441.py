#include<stdio.h>

int main() {
	int amount;
	scanf("%d",&amount);
	for (int x = 1; x <= amount; x++) {
		int chosenLine1, chosenLine2;
		int line1[4];
		int line2[4];
		scanf("%d",&chosenLine1);
		chosenLine1--;
		for (int i = 0; i < 4; i++) {
			int a, b,c,d;
			scanf("%d %d %d %d",&a,&b,&c,&d);
			if (i == chosenLine1) {
				line1[0] = a;
				line1[1] = b;
				line1[2] = c;
				line1[3] = d;
			}
		}

		scanf("%d",&chosenLine2);
		chosenLine2--;
		for (int i = 0; i < 4; i++) {
			int a, b,c,d;
			scanf("%d %d %d %d",&a,&b,&c,&d);
			if (i == chosenLine2) {
				line2[0] = a;
				line2[1] = b;
				line2[2] = c;
				line2[3] = d;
			}
		}

		int chosenCard = -1;
		int resultType = 0; // -1 is bad magician, 0 is cheater volunteer, 1 is ok
		for (int i = 0; i < 4; i++) {
			int stopLoop = 0;
			for (int j = 0; j < 4; j++) {
				if (line1[i] == line2[j]) {
					if (chosenCard == -1) {
						chosenCard = line1[i];
						resultType = 1;
					} else {
						stopLoop = 1;
						break;
					}
				}
			}
			if (stopLoop) {
				resultType = -1;
				break;
			}
		}

		if (resultType == -1) {
			printf("Case #%d: Bad magician!",x);
		} else if (resultType == 0) {
			printf("Case #%d: Volunteer cheated!",x);
		} else {
			printf("Case #%d: %d",x,chosenCard);
		}

		if (x != amount) {
			printf("\n");
		}
	}
	return 0;
}