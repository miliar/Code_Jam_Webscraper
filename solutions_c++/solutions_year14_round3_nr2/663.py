#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n;
char s[105][105], str[10005];
int a[105];
int flag[128];

int valid(char *s) {
    memset(flag, 0, sizeof(flag));
    for (int i = 0; s[i]; ++i) {
        if (flag[s[i]])
            return 0;
        flag[s[i]] = 1;
        while (s[i+1] == s[i]) ++i;
    }
    return 1;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%s", s[i]);
            a[i] = i;
        }
        int ans = 0;
        do {
            int sz = 0;
            for (int i = 0; i < n; ++i)
                for (int j = 0; s[a[i]][j]; ++j)
                    str[sz++] = s[a[i]][j];
            str[sz] = 0;
            if (valid(str))
                ans++;
        } while (next_permutation(a, a+n));
        printf("Case #%d: %d\n", t, ans);
    }
}
