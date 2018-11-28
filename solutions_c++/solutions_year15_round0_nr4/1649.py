#include <cstdio>
#include <cstdlib>
#include <cstring>

const int N = 5;

bool vict[N][N][N];

void init(void)
{
    memset(vict, false, sizeof(vict));
    for (int i = 1; i < N; i++) {
        for (int j = 1; j < N; j++)
            vict[1][i][j] = true;
    }
    for (int i = 1; i < N; i++) {
        for (int j = 1; j < N; j++) {
            if ((i * j & 1) != 1)
                vict[2][i][j] = true;
        }
    }
    vict[3][2][3] = vict[3][3][2] = true;
    vict[3][3][4] = vict[3][4][3] = true;
    vict[3][3][3] = vict[4][4][4] = true;
    vict[4][3][4] = vict[4][4][3] = true;
}

int main(void)
{
    int T;
    scanf("%d", &T);
    init();
    for (int cases = 1; cases <= T; cases++) {
        int X, R, C;
        scanf("%d %d %d", &X, &R, &C);
        printf("Case #%d: %s\n", cases, vict[X][R][C] ? "GABRIEL" : "RICHARD");
    }
    return EXIT_SUCCESS;
}
