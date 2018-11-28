#include <cstdio>


int main() 
{
    int caseCount;
    int answer1, answer2;
    int card1[5][5], card2[5][5];
   
    scanf(" %d", &caseCount);
    for(int caseIndex = 1; caseIndex <= caseCount; caseIndex++) {
        scanf(" %d", &answer1);
        for(int i = 1; i <= 4; i++) {
            for(int j = 1; j <= 4; j++) {
                scanf(" %d", &card1[i][j]);
            }
        }

        scanf(" %d", &answer2);
        for(int i = 1; i <= 4; i++) {
            for(int j = 1; j <= 4; j++) {
                scanf(" %d", &card2[i][j]);
            }
        }

        int possible = 0;
        int answer;
        for(int i = 1; i<= 4; i++) {
            for(int j = 1; j <= 4; j++) {
                if(card1[answer1][i] == card2[answer2][j]) {
                    possible++;
                    answer = card1[answer1][i];
                }
            }
        }

        printf("Case #%d: ", caseIndex);
        if(possible == 0) {
            printf("Volunteer cheated!\n");
        }
        else if(possible == 1) {
            printf("%d\n", answer);
        }
        else {
            printf("Bad magician!\n");
        }
    }

    return 0;
}
