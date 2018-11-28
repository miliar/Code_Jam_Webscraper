#include<stdio.h>
#include<stdlib.h>

int main()
{
	int T;
	scanf("%d", &T);

	for(int cases = 1; cases <= T; cases++){
		int answer1;
		scanf("%d", &answer1);

		int cards1[5][5];
		for(int i = 1; i <= 4; i++){
			for(int ii = 1; ii <= 4; ii++){
				scanf("%d", &cards1[i][ii]);
			}
		}

		int guess[5];
		for(int i = 1; i <= 4; i++){
			guess[i] = cards1[answer1][i];
		}

		int answer2;
		scanf("%d", &answer2);

		int cards2[5][5];
		for(int i = 1; i <= 4; i++){
			for(int ii = 1; ii <= 4; ii++){
				scanf("%d", &cards2[i][ii]);
			}
		}

		int possibleAnswer = 0;
		int count = 0;
		for(int i = 1; i <= 4; i++){
			for(int ii = 1; ii <= 4; ii++){
				if(guess[i] == cards2[answer2][ii]){
					possibleAnswer = cards2[answer2][ii];
					count++;
				}
			}
		}

		// Multiple possible answers
		if(count > 1) printf("Case #%d: Bad magician!\n", cases);

		// No consistent possible answers
		else if(count == 0) printf("Case #%d: Volunteer cheated!\n", cases);

		// Exactly only one possible answer
		else printf("Case #%d: %d\n", cases, possibleAnswer);
	}
	
	return 0;
}