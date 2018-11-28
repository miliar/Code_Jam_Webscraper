#include <cstdio>
#include <cstring>
using namespace std;

int main() {
    int T, r1, r2, g1[5][5], g2[5][5], flag[20];

    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &r1);
        for (int i = 1; i <= 4; i++)
            for (int j = 1; j <= 4; j++)
                scanf("%d", &g1[i][j]);
        scanf("%d", &r2);
        for (int i = 1; i <= 4; i++)
            for (int j = 1; j <= 4; j++)
                scanf("%d", &g2[i][j]);

        memset(flag, 0, sizeof(flag));
        for (int j = 1; j <= 4; j++)
            flag[g1[r1][j]]++, flag[g2[r2][j]]++;
        int cnt = 0, id;
        for (int i = 1; i <= 16; i++) {
            if (flag[i] == 2) {
                cnt++;
                id = i;
            }
        }
        
        printf("Case #%d: ", t);
        if (cnt == 1)
            printf("%d\n", id);
        else if (cnt > 1)
            printf("Bad magician!\n");
        else
            printf("Volunteer cheated!\n");
    }
}
