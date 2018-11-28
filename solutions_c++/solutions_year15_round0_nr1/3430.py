#include <cstdio>

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int S;
        scanf("%d", &S);
        getchar();
        char c;
        int now = 0;
        int need = 0;
        for (int i = 0; i <= S; i++) {
            if (now < i) {
                need += i-now;
                now += i-now;
            }
            int n = getchar()-'0';
            now += n;
        }
        printf("Case #%d: %d\n", t, need);
    }
    return 0;
}
