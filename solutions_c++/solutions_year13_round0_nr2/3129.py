#include <stdio.h>

int lawn[100][100] = { 0 };
int rowmax[100] = { 0 };
int colmax[100] = { 0 };
bool max(int row, int col) {
    for (int i = 0; i < row; i++) {
        rowmax[i] = 0;
        for (int j = 0; j < col; j++)
            if (lawn[i][j] > rowmax[i])
                rowmax[i] = lawn[i][j];
    }
    for (int i = 0; i < col; i++) {
        colmax[i] = 0;
        for (int j = 0; j < row; j++)
            if (lawn[j][i] > colmax[i])
                colmax[i] = lawn[j][i];
    }
}
bool check(int row, int col) {
    max(row, col);
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            if (lawn[i][j] < rowmax[i] && lawn[i][j] < colmax[j])
                return false;
        }
    }
    return true;
}

int main() {
    int count;
    int row, col;
    scanf("%d", &count);
    for (int c = 0; c < count; c++) {
        scanf("%d %d", &row, &col);
        for (int i = 0; i < row; i++)
            for (int j = 0; j < col; j++)
                scanf("%d", &lawn[i][j]);
        printf("Case #%d: %s\n", c+1, check(row, col) ? "YES" : "NO");
    }
    return 0;
}
