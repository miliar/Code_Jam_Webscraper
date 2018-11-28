#include <cstdio>
#include <bitset>

#define SQUARE_SIZE 4
#define NUM_NUMBERS 16

using namespace std;

int main(int arg, char *argv[]) {
    int T, firstQ, secondQ, square[4][4];
    int c = 1;
    int i, j;
    scanf("%d", &T);
    while(T--) {
        bitset<NUM_NUMBERS> set1, set2;

        scanf("%d", &firstQ);
        for (i = 0; i < SQUARE_SIZE; i++) {
            for (j = 0; j < SQUARE_SIZE; j++) {
                scanf("%d", &square[i][j]);
            }
        }
        for (i = 0; i < SQUARE_SIZE; i++) {
            set1[square[i][firstQ - 1]] = 1;
        }

        scanf("%d", &secondQ);
        for (i = 0; i < SQUARE_SIZE; i++) {
            for (j = 0; j < SQUARE_SIZE; j++) {
                scanf("%d", &square[i][j]);
            }
        }
        for (i = 0; i < SQUARE_SIZE; i++) {
            set2[square[i][secondQ - 1]] = 1;
        }

        bitset<NUM_NUMBERS> result = set1 & set2;
        printf("Case #%d: ", c++);
        if (result.none()) {
            printf("Volunteer cheated!");
        } else if (result.count() > 1) {
            printf("Bad magician!");
        } else {
            i = 1;
            while(result[0] != 1) {
                result >>= 1;
                i++;
            }
            printf("%d", i);
        }
        printf("\n");

    }
    return 0;
}