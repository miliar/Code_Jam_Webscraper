#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
    int first_arr[4][4];
    int second_arr[4][4];
    int first_row;
    int second_row;
    int T;
    int num_same = 0;
    int card;

    scanf("%d", &T);
    int c = 1;
    while (c <= T) {
        scanf("%d", &first_row);
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf("%d", &first_arr[i][j]);
            }
        }

        scanf("%d", &second_row);
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf("%d", &second_arr[i][j]);
            }
        }

        first_row--;
        second_row--;

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (first_arr[first_row][i] == second_arr[second_row][j]) {
                    num_same++;
                    card = first_arr[first_row][i];
                }
            }
        }


        printf("Case #%d: ", c);
        if (num_same == 0) {
            printf("Volunteer cheated!\n");
        } else if (num_same > 1) {
            printf("Bad magician!\n");
        } else {
            printf("%d\n", card);
        }

        num_same = 0;
        c++;
    }

    return 0;
}