#include <cstdio>
#include <cstring>

int mat[5][5], flag[17];

int main()
{
    // freopen("in", "r", stdin);
    // freopen("out", "w", stdout);
    int t, n, k = 1;
    scanf("%d", &t);
    while(t--) {
        memset(flag, 0, sizeof(flag));
        scanf("%d", &n);
        for(int i = 1; i <= 4; i++) {
            for(int j = 1; j <= 4; j++) {
                scanf("%d", mat[i] + j);
                if(i == n) flag[mat[i][j]]++;
            }
        }
        scanf("%d", &n);
        for(int i = 1; i <= 4; i++) {
            for(int j = 1; j <= 4; j++) {
                scanf("%d", mat[i] + j);
                if(i == n) flag[mat[i][j]]++;
            }
        }
        int cot = 0, ans = 0;
        for(int i = 1; i <= 16; i++) {
            if(flag[i] == 2) {
                cot++;
                ans = i;
            }
        }
        printf("Case #%d: ", k++);
        if(cot == 1) printf("%d\n", ans);
        else if(cot > 1) puts("Bad magician!");
        else puts("Volunteer cheated!");
    }
    return 0;
}
