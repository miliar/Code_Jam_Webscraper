#include <cstdio>
#include <cstring>
#include <set>
using namespace std;
int main(){
    int card1[4][4], card2[4][4];
    int T;
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    const char gg[] = "Bad magician!";
    const char cheat[] = "Volunteer cheated!";
    scanf("%d", &T);
    for (int ct = 1; ct <= T; ct++) {
        printf("Case #%d: ", ct);
        int ans[20] = {0};
        int ans_ct = 0;
        int r1, r2;
        set <int> s1, s2;
        scanf("%d", &r1);
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf("%d", &card1[i][j]);
            }
        }
        scanf("%d", &r2);
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf("%d", &card2[i][j]);
            }
        }
        for (int i = 0; i < 4; i++) {
            int tmp = card1[r1-1][i];
            for (int j = 0; j < 4; j++) {
                if (tmp == card2[r2-1][j]) {
                    ans[ans_ct++] = tmp;
                }
            }
        }
        if (ans_ct == 0) {
            printf("%s\n", cheat);
        } else if (ans_ct == 1) {
            printf("%d\n", ans[0]);
        } else {
            printf("%s\n", gg);
        }
    }
    return 0;
}
