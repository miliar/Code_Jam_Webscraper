#include <cstdio>

int grid1[4][4], grid2[4][4];
int r1, r2;

int main() {
    int test, cs, i, j, k, ans;
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    scanf("%d", &test);
    for(cs = 1; cs <= test; cs++) {
        scanf("%d", &r1);
        for(i = 0; i < 4; i++)
            for(j = 0; j < 4; j++)
                scanf("%d", &grid1[i][j]);
        scanf("%d", &r2);
        for(i = 0; i < 4; i++)
            for(j = 0; j < 4; j++)
                scanf("%d", &grid2[i][j]);
        r1--, r2--, k = 0;
        for(i = 0; i < 4; i++)
            for(j = 0; j < 4; j++)
                if(grid1[r1][i] == grid2[r2][j]) {
                    k++;
                    ans = grid1[r1][i];
                }
        if(k == 0) printf("Case #%d: Volunteer cheated!\n", cs);
        else if(k == 1) printf("Case #%d: %d\n", cs, ans);
        else printf("Case #%d: Bad magician!\n", cs);
    }
    return 0;
}
