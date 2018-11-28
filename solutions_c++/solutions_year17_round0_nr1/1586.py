#include <cstdio>
#include <cstring>

char buf[1 << 20];

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        int k;
        scanf("%s %d", buf, &k);
        int l = strlen(buf);
        int steps = 0;
        bool ok = true;
        for (int i = 0; i < l; ++i) {
            if (buf[i] == '-') {
                if (i + k - 1 < l) {
                    ++steps;
                    for (int j = 0; j < k; ++j) {
                        buf[i + j] = (char) ((int) '+' + (int) '-' - (int) buf[i + j]);
                    }
                } else {
                    ok = false;
                }
            }
        }
        printf("Case #%d: ", t);
        if (ok) {
            printf("%d\n", steps);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
