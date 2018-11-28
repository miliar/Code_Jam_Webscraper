#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int mat1[5][5], mat2[5][5], cnt[17];

int main()
{
    freopen("A-small.in", "r", stdin);
    freopen("A-small.out", "w", stdout);

    int ci, cn;
    scanf("%d", &cn);

    for(ci = 1; ci <= cn; ci++) {
        int r1, r2, i, j;

        memset(cnt, 0, sizeof(cnt));

        scanf("%d", &r1) ;
        for(i = 1; i <= 4; i++)
            for(j = 1; j <= 4; j++) {
                scanf("%d", &mat1[i][j]);
                if(r1 == i) cnt[mat1[i][j]] ++;
            }

        scanf("%d", &r2);
        for(i = 1;i <= 4; i++)
            for(j = 1;j <= 4; j++) {
                scanf("%d", &mat2[i][j]);
                if(r2 == i) cnt[mat2[i][j]] ++;
            }

        int tot = 0, ans = -1;
        for(i = 1; i <= 16; i++)
            if(cnt[i] == 2) { tot++; ans = i; }
        if(tot == 0)
            printf("Case #%d: Volunteer cheated!\n", ci);
        else if(tot == 1)
            printf("Case #%d: %d\n", ci, ans);
        else
            printf("Case #%d: Bad magician!\n", ci);
    }
    return 0;
}
