#include <stdio.h>
int u[20], cnt, num;
int main(){
    int T, ri = 1, i, j, x, t;
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        for (i = 0; i < 20; i++) u[i] = 0;
        scanf("%d", &t);
        for (i = 1; i <= 4; i++){
            for (j = 0; j < 4; j++){
                scanf("%d", &x);
                if (i == t) u[x]++;
            }
        }
        scanf("%d", &t);
        for (i = 1; i <= 4; i++){
            for (j = 0; j < 4; j++){
                scanf("%d", &x);
                if (i == t) u[x]++;
            }
        }
        cnt = 0;
        for (i = 0; i < 20; i++){
            if (u[i] == 2){
                cnt++;
                num = i;
            }
        }
        printf("Case #%d: ", ri++);
        if (cnt == 0) printf("Volunteer cheated!\n");
        else if (cnt == 1) printf("%d\n", num);
        else printf("Bad magician!\n");
    }
    return 0;
}
