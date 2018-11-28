#include <cstdio>

char s[1005];
char b[1005];
char a[1005];

int main() {
    int t;
    scanf("%d\n", &t);
    for (int c = 1; c <= t; ++c) {
        scanf("%s\n", s);
        int l = 0, r = 0, cur = 0;
        b[l++] = s[cur++];
        while (s[cur]) {
            if (s[cur] >= b[l - 1]) {
                b[l++] = s[cur++];
            } else {
                a[r++] = s[cur++];
            }
        }

        printf("Case #%d: ", c);
        --l;
        while (l >= 0) {
            printf("%c", b[l--]);
        }
        for (int i = 0; i < r; ++i) {
            printf("%c", a[i]);
        }
        printf("\n");
    }
}
