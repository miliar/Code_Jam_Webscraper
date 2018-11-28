#include "stdio.h"

int main() {
    int t;
    scanf("%i", &t);
    for (int ti = 1; ti<=t; ti++) {
        int rowNum, row[4];
        scanf("%i", &rowNum);
        for (int i=1; i<=4; i++) {
            if (i == rowNum) {
                for (int j=0; j<4; j++)
                    scanf("%i", row+j);
            } else {
                int dump;
                for (int j=0; j<4; j++)
                    scanf("%i", &dump);
            }
        }
        int matchingNum = 0, matchingValue = 0;
        scanf("%i", &rowNum);
        for (int i=1; i<=4; i++) {
            int cardValue;
            if (i == rowNum) {
                for (int j=0; j<4; j++) {
                    scanf("%i", &cardValue);
                    for (int k=0; k<4; k++)
                        if (cardValue == row[k]) {
                            matchingNum ++;
                            matchingValue = cardValue;
                        }
                }
            } else {
                for (int j=0; j<4; j++)
                    scanf("%i", &cardValue);
            }
        }

        if (matchingNum == 0) {
            printf("Case #%i: Volunteer cheated!\n", ti);
        } else if (matchingNum == 1) {
            printf("Case #%i: %i\n", ti, matchingValue);
        } else {
            printf("Case #%i: Bad magician!\n", ti);
        }
    }
    return 0;
}
