#include <cstdio>
#include <cstring>
#include <cassert>

int main () {

    assert(freopen("tiles.in", "r", stdin));
    assert(freopen("tiles.out", "w", stdout));

    int c;
    int j = 0;

    scanf("%d\n", &c);

    while ( j++ < c ) {

        int k, c, s;
        scanf("%d%d%d", &k, &c, &s);

        printf("Case #%d: ", j);
        for (int i = 0; i < k; ++i) {
            printf("%d", i+1);
            i != k - 1 ? printf(" ") : printf("\n");
        }
    }

    return 0;
}
