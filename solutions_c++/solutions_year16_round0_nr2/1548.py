#include <cstdio>
#include <cstring>
#include <cassert>

char s[120];

int main () {
    assert(freopen("cake.in", "r", stdin));
    assert(freopen("cake.out", "w", stdout));

    int c;
    int j = 0;

    scanf("%d\n", &c);

    while ( j++ < c ) {

        gets(s);
        int len = strlen(s);
        int cnt = 0;

        for (int i = 0; i < len - 1; ++i) {
            if (s[i] != s[i + 1]) {
                cnt++;
            }
        }

        if (s[len - 1] == '-') {
            cnt++;
        }

        printf("Case #%d: %d\n", j, cnt);
    }

    return 0;
}
