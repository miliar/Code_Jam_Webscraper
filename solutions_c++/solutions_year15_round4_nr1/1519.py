#include <stdio.h>

int main(int argc, char const *argv[])
{
    int test, kase, row, col;
    int i, j, r, f;
    int rmin[101], rmax[101], cmin[101], cmax[101];
    char grid[101][101];

    scanf("%d\n", &test);
    for (kase = 1; kase <= test; kase++) {
        scanf("%d %d\n", &row, &col);
        for (i = 0; i < row; i++)
            gets(grid[i]);
        for (i = 0; i < row; i++) {
            rmin[i] = col;
            rmax[i] = -1;
        }
        for (j = 0; j < col; j++) {
            cmin[j] = row;
            cmax[j] = -1;
        }
        for (i = 0; i < row; i++)
        for (j = 0; j < col; j++)
        if (grid[i][j] != '.') {
            if (j < rmin[i]) rmin[i] = j;
            if (j > rmax[i]) rmax[i] = j;
            if (i < cmin[j]) cmin[j] = i;
            if (i > cmax[j]) cmax[j] = i;
        }
        r = f = 0;
        for (i = 0; i < row; i++)
        for (j = 0; j < col; j++)
        if (grid[i][j] != '.') {
            if (rmin[i] == j &&
                rmax[i] == j &&
                cmin[j] == i &&
                cmax[j] == i) {
                f = 1;
                continue;
            }
            if ((grid[i][j] == '<' && rmin[i] < j) ||
                (grid[i][j] == '>' && rmax[i] > j) ||
                (grid[i][j] == '^' && cmin[j] < i) ||
                (grid[i][j] == 'v' && cmax[j] > i)) {
                continue;
            }
            r++;
        }
        if (f)
            printf("Case #%d: IMPOSSIBLE\n", kase);
        else
            printf("Case #%d: %d\n", kase, r);
    }
    return 0;
}