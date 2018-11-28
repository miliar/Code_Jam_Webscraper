#include <bits/stdc++.h>

int main() {
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t, s, ans, card = -1, a[4][4], insec[4], i, j, k, flag = -1;
    scanf("%d", &t);
    for (s=1; s<=t; s++) {
        flag = -1;
        scanf("%d", &ans);
        for (i=0; i<4; i++) {
            for (j=0; j<4; j++) {
                scanf("%d", &a[i][j]);
                if (ans == i+1)
                    insec[j] = a[i][j];
            }
        }
        scanf("%d", &ans);
        for (i=0; i<4; i++) {
            for (j=0; j<4; j++) {
                scanf("%d", &a[i][j]);
                if (ans == i+1) {
                    for (k=0; k<4; k++) {
                        if (a[i][j] == insec[k]) {
                            flag++;
                            card = a[i][j];
                        }
                    }
                }
            }
        }
        if (flag < 0)
            printf("Case #%d: Volunteer cheated!\n", s);
        else if (flag == 0)
            printf("Case #%d: %d\n", s, card);
        else printf("Case #%d: Bad magician!\n", s);
    }
    return 0;
}
