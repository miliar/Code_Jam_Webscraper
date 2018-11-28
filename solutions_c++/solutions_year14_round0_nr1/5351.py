
#include <cstring>
#include <cstdio>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for (int no = 0; no < T; no ++) {
        int r;
        scanf("%d", &r);
        r --;
        bool a[17];
        memset(a, false, sizeof(a));
        for (int i = 0; i < 4; i ++) {
            for (int j = 0; j < 4; j ++) {
                int x;
                scanf("%d", &x);
                if (i == r) a[x] = true;
            }
        }
        scanf("%d", &r);
        r --;
        int ans = -1, cnt = 0;
        for (int i = 0; i < 4; i ++) {
            for (int j = 0; j < 4; j ++) {
                int x;
                scanf("%d", &x);
                if (i == r && a[x]) {
                    ans = x;
                    cnt ++;
                }
            }
        }
        printf("Case #%d: ", no + 1);
        if (cnt == 0) {
            printf("Volunteer cheated!\n");
        } else if (cnt == 1) {
            printf("%d\n", ans);
        } else {
            printf("Bad magician!\n");
        }
    }
    return 0;
}