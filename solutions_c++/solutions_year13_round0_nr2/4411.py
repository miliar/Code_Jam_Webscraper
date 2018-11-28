#include <cstdio>
#include <cstring>


int grid[100][100];
int vertical[100][100];
int horizontal[100][100];


int main() {
    int N;
    scanf("%d", &N);

    int r, c;

    for (int caseN = 1; caseN <= N; caseN++) {
        scanf("%d%d", &r, &c);
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                scanf("%d", &grid[i][j]);

        memset(vertical, 127, sizeof(vertical));
        memset(horizontal, 127, sizeof(horizontal));

        for (int i = 0; i < r; i++) {
            int max = grid[i][0];
            int min = grid[i][0];
            for (int j = 1; j < c; j++) {
                if (grid[i][j] > max) max = grid[i][j];
                if (grid[i][j] < min) min = grid[i][j];
            }

            if (min == max) continue;

            for (int j = 0; j < c; j++)
                if (grid[i][j] != max)
                    horizontal[i][j] = 0;
        }

        for (int i = 0; i < c; i++) {
            int min = grid[0][i];
            int max = grid[0][i];
            for (int j = 1; j < r; j++) {
                if (grid[j][i] < min) min = grid[j][i];
                if (grid[j][i] > max) max = grid[j][i];
            }

            if (min == max) continue;

            for (int j = 0; j < r; j++)
                if (grid[j][i] != max)
                    vertical[j][i] = 0;
        }

        int can = 1;
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                if (!horizontal[i][j] && !vertical[i][j])
                    can = 0;

        printf("Case #%d: ", caseN);
        if (can) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
