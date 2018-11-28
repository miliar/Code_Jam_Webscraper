#include <cstdio>
#include <cassert>
#define MAX_D 1010

int digitToNumber(char c) {
    return c - '0';
}

int solve(int m, char *s) {
    assert(s[m] > 0);

    int standing_cnt = 0, invited = 0;
    for(int shyness = 0; shyness <= m; shyness++) {
        int people = digitToNumber(s[shyness]);

        if(standing_cnt < shyness) {
            invited += shyness - standing_cnt;
            standing_cnt += shyness - standing_cnt;
        }
        assert(standing_cnt >= shyness);

        standing_cnt += people;
    }

    return invited;
}

int main() {
    int T, n;
    char digits[MAX_D];
    scanf("%d", &T);

    for(int t=1; t<=T; t++) {
        scanf("%d", &n);
        scanf("%s", digits);
        printf("Case #%d: %d\n", t, solve(n, digits));
    }

    return 0;
}
