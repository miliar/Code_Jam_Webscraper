#include <stdio.h>

void read_matrix(int poss[4][4]) {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            scanf("%i", &poss[i][j]);
        }
    }
}

int main(int argc, char **argv) {
    int T, matrix[4][4], first_row[4], the_number, num_possible, row_number;
    scanf("%i", &T);
    for (int i = 0; i < T; i++) {
        scanf("%i", &row_number);
        row_number--;
        read_matrix(matrix);
        for (int col = 0; col < 4; col++) {
            first_row[col] = matrix[row_number][col];
        }
        scanf("%i", &row_number);
        row_number--;
        read_matrix(matrix);
        num_possible = 0;
        for (int col = 0; col < 4; col++) {
            int candidate = matrix[row_number][col];
            for (int colf = 0; colf < 4; colf++) {
                if (first_row[colf] == candidate) {
                    the_number = candidate;
                    num_possible++;
                    break;
                }
            }
        }
        printf("Case #%i: ", i + 1);
        if (num_possible == 1) {
            printf("%i", the_number);
        } else if (num_possible == 0) {
            printf("Volunteer cheated!");
        } else {
            printf("Bad magician!");
        }
        printf("\n");
    }
    return 0;
}
