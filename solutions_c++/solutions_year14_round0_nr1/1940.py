#include <stdio.h>
void check(int* cardset1, int* cardset2, int testcase){
	int count = 0, index;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (cardset1[i] == cardset2[j]){
				index = i;
				count++;
			}
	if (count > 1)
		printf("Case #%d: Bad magician!\n", testcase);
	if (count == 1)
		printf("Case #%d: %d\n", testcase, cardset1[index]);
	if (count < 1)
		printf("Case #%d: Volunteer cheated!\n", testcase);
	return;
}
int main(void){
	int t;
	int cardset1[4][4], cardset2[4][4], row1, row2;
	scanf("%d", &t);
	for (int i = 0; i < t; i++){
		scanf("%d", &row1);
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				scanf("%d", &cardset1[j][k]);
		scanf("%d", &row2);
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				scanf("%d", &cardset2[j][k]);
		check(cardset1[row1 - 1], cardset2[row2 - 1], i + 1);
	}
	return 0;
}
