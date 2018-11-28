#include <cstdio>
#include <cstring>

int isIn[0x20];

int check() {
    int ret, ret2;
    for (ret = 1; ret <= 16 && isIn[ret] != 2; ++ret) ;
    if (ret > 16) return -1;
    for (ret2 = ret + 1; ret2 <= 16 && isIn[ret2] != 2; ++ret2) ;
    if (ret2 > 16) return ret;
    return 0;
}

int main() {
    int t;

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    scanf("%d", &t);
    for (int cas = 1; cas <= t; ++cas) {
        memset(isIn, 0, sizeof(isIn));
        int pick, num;
        scanf("%d", &pick);
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                scanf("%d", &num);
                if (i + 1 == pick) isIn[num]++;
            }
        }
        scanf("%d", &pick);
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                scanf("%d", &num);
                if (i + 1 == pick) isIn[num]++;
            }
        }

        int ret = check();
        if (ret == -1) printf("Case #%d: Volunteer cheated!\n", cas);
        else if (ret == 0) printf("Case #%d: Bad magician!\n", cas);
        else printf("Case #%d: %d\n", cas, ret);
    }

    return 0;
}
