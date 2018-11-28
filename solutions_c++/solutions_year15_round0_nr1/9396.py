#include <cstdio>


int standing_ovation(int s_max, char* digits) {
    int addendum = 0;
    int cnt = 0;

    for (int i = 0; i <= s_max; ++i) {
        int num = digits[i] - '0';
        if (cnt < i) {
            int inc = i - cnt;
            cnt += inc;
            addendum += inc;
        }
        cnt += num;
    }

    return addendum;
}


int main() {
    int t, s_max;
    char digits[1002];

    scanf("%d", &t);

    for (int i = 0; i < t; ++i) {
        scanf("%d", &s_max);
        scanf("%s", digits);

        printf("Case #%d: %d\n", i + 1, standing_ovation(s_max, digits));
    }
}
