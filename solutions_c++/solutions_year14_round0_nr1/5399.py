#include <cstdio>

int mat[4][4];

int main() {
    int T;
    scanf("%d", &T);
    for (int kase = 0; kase < T; ++ kase) {
        int m1 = 0, m2 = 0;
        int r;
        scanf("%d", &r);
        for (int i = 0; i < 4; ++ i)
            for (int j = 0; j < 4; ++ j) {
                scanf("%d", &mat[i][j]);
                if (i == r - 1) m1 |= 1 << mat[i][j];
            }
        scanf("%d", &r);
        for (int i = 0; i < 4; ++ i)
            for (int j = 0; j < 4; ++ j) {
                scanf("%d", &mat[i][j]);
                if (i == r - 1) m2 |= 1 << mat[i][j];
            }
        int m = m1 & m2;
        int c = __builtin_popcount(m);
        printf("Case #%d: ", kase + 1);
        if (c == 1) printf("%d\n", __builtin_ctz(m));
        else if (c == 0) printf("Volunteer cheated!\n");
        else printf("Bad magician!\n");
    }
    return 0;
}
