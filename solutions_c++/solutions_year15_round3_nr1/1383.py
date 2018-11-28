#include <cstdio>
int main() {
    int T, tcase = 1;
    scanf("%d", &T);
    while(T--) {
        int r, c, w;
        scanf("%d%d%d", &r, &c, &w);
        if(c % w) {
            printf("Case #%d: %d\n", tcase++, r * (c / w) + w);
        } else {
            printf("Case #%d: %d\n", tcase++, r * (c / w) + w - 1);
        }
    }
    return 0;
}
