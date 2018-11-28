#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

int T, x, y;

int main() {
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small.out", "w", stdout);
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);
        scanf("%d%d", &x, &y);
        if (y > 0) {
            for (int i = 0; i < y; ++i) {
                printf("SN");
            }
        } else {
            for (int i = 0; i < -y; ++i) {
                printf("NS");
            }
        }
        if (x > 0) {
            for (int i = 0; i < x; ++i) {
                printf("WE");
            }
        } else {
            for (int i = 0; i < -x; ++i) {
                printf("EW");
            }
        }
        puts("");
    }
    return 0;
}

