#include <cstdio>

int main() {
    int xx[2][10] = {{ 0, 0, 0, 0, 0, 1, 0, 1, 1, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 }};

    int T, x, r, c;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        scanf("%d%d%d", &x, &r, &c);
        if (r > c) {
            int a = r;
            r = c;
            c = a;
        }
        switch (x) {
            case 1:
                puts("GABRIEL");
                break;
            case 2:
                if (r * c & 1) puts("RICHARD");
                else puts("GABRIEL");
                break;
            case 3:
            case 4:
                if (xx[x - 3][(10 - r) * (r - 1) / 2 + (c - r)]) puts("GABRIEL");
                else puts("RICHARD");
                break;
        }
    }
    return 0;
}