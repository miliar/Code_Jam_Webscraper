#include <cstdio>
#include <cstdlib>
#include <cstring>

int a[20];

int main(){
    int T, tcase, i, j, row, tmp;

    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small.out", "w", stdout);

    scanf("%d", &T);
    for (tcase=1; tcase<=T; tcase++){
        memset(a, 0, sizeof(a));
        scanf("%d", &row);
        for (i=1; i<=4; i++){
            for (j=1; j<=4; j++){
                scanf("%d", &tmp);
                if (i==row) a[tmp]++;
            }
        }
        scanf("%d", &row);
        for (i=1; i<=4; i++){
            for (j=1; j<=4; j++){
                scanf("%d", &tmp);
                if (i==row) a[tmp]++;
            }
        }
        int cnt=0, ans;
        for (i=1; i<=16; i++){
            if (a[i]==2) {
                cnt++;
                ans = i;
            }

        }
        printf("Case #%d: ", tcase);
        if (cnt==0) printf("Volunteer cheated!\n");
        else if (cnt==1) printf("%d\n", ans);
        else printf("Bad magician!\n");
    }
    return 0;
}
