#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main () {
    vector <bool> possible, actualrow;
    int T, possiblecards, numberofcard, significantrow, x;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        possiblecards = 0;
        possible.resize(16, true);
        actualrow.resize(16, false);
        scanf("%d", &significantrow);
        for (int j = 1; j <= 4; j++) {
            for (int k = 1; k <= 4; k++) {
                scanf("%d", &x);
                if (j == significantrow) actualrow [x - 1] = true;
            }
        }
        for (int j = 0; j < 16; j++) {
            possible [j] = actualrow [j];
        }
        actualrow.clear();
        actualrow.resize(16, false);
        scanf("%d", &significantrow);
        for (int j = 1; j <= 4; j++) {
            for (int k = 1; k <= 4; k++) {
                scanf("%d", &x);
                if (j == significantrow) actualrow [x - 1] = true;
            }
        }
        for (int j = 0; j < 16; j++) {
            if (possible [j] && actualrow [j]) {
                possiblecards ++;
                numberofcard = j + 1;
            }
        }
        printf("Case #%d: ", i);
        if (possiblecards >1) {
            printf ("Bad magician!\n");
        }
        else if (possiblecards < 1) {
            printf("Volunteer cheated!\n");
        }
        else printf("%d\n", numberofcard);
        possible.clear();
        actualrow.clear();
    }
}
