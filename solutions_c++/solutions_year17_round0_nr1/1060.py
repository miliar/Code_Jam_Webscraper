#include <cstdio>
#include <cstring>

const int MAXN = 1010;

char s[MAXN];
int T, n, m;

bool change(int idx) {
    if (n - idx < m) {
        return false;
    }
    for (int i = idx; i < idx+m; i++) {
        if (s[i] == '-') {
            s[i] = '+';
        } else {
            s[i] = '-';
        }
    }
    return true;
}

int main() {
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%s%d", s, &m);
        n = strlen(s);
        int ret = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == '-') {
                if (!change(i)) {
                    ret = -1;
                    break;
                } else {
                    ret++;
                }
            }
        }
        if (ret == -1) {
            printf("Case #%d: IMPOSSIBLE\n", t);
        } else {
            printf("Case #%d: %d\n", t, ret);
        }
    }
    return 0;
}
