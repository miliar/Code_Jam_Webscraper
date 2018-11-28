#include<cstdio>
#include<cstring>
int solve(int *a, int *b) {
    int res = -1, ct = 0;
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++) {
            if(a[i] == b[j]) {
                ct++;
                res = a[i];
            }
        }
    }
    if(ct > 1) return 0;
    return res;
}
int main() {
    freopen("D:\\offLineProcessing\\in", "r", stdin);
    freopen("D:\\offLineProcessing\\out.txt","w",stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while(T--) {
        int a[4][4], b[4][4];
        int ans1, ans2;
        scanf("%d", &ans1);
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                int tmp;scanf("%d", &tmp);
                a[i][j] = tmp;
            }
        }
        scanf("%d", &ans2);
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4;j ++) {
                int tmp;scanf("%d", &tmp);
                b[i][j] = tmp;
            }
        }
        int res = solve(a[ans1-1], b[ans2-1]);
        printf("Case #%d: ", ++cas);
        if(res == -1) {
            puts("Volunteer cheated!");
        } else if(res == 0) {
            puts("Bad magician!");
        } else {
            printf("%d\n", res);
        }
    }
}
