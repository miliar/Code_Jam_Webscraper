
#include <stdio.h>

int intersection( int row1[4], int row2[4], int * value ) {
    int matched = 0;
    for (int i=0; i<4; ++i) {
        for (int j=0; j<4; ++j) {
            if (row1[i] == row2[j]) {
                matched += 1;
                *value = row1[i];
            }
        }
    }
    return matched;
}

int main( int argc, char * argv[] ) {
    int cases;
    scanf("%d", &cases);
    for (int i=0; i<cases; ++i) {
        int n0, n1, n2, n3;
        int row_num1;
        int row1[4];
        scanf("%d", &row_num1);
        for (int j=1; j<=4; ++j) {
            scanf("%d %d %d %d", &n0, &n1, &n2, &n3);
            if (j == row_num1) { row1[0] = n0; row1[1] = n1; row1[2] = n2; row1[3] = n3; }
        }
        int row_num2;
        int row2[4];
        scanf("%d", &row_num2);
        for (int j=1; j<=4; ++j) {
            scanf("%d %d %d %d", &n0, &n1, &n2, &n3);
            if (j == row_num2) { row2[0] = n0; row2[1] = n1; row2[2] = n2; row2[3] = n3; }
        }
        int value = 0;
        int common = intersection(row1, row2, &value);
        printf("Case #%d: ", i+1);
        if (common == 0) printf("Volunteer cheated!\n");
        if (common == 1) printf("%d\n", value);
        if (common > 1) printf("Bad magician!\n");
    }
}
