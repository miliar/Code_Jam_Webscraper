#include <cstdio>
#include <cstring>
using namespace std;

int  main() {
    int T;

    freopen("fa.in", "r", stdin);
    freopen("fa.out", "w", stdout);
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        int smax, curr_sum, to_add = 0;
        char s[1009];

        scanf("%d %s", &smax, s);
        curr_sum = s[0] - '0';
        for (int s_it = 1; s_it <= smax; ++s_it) {
            //printf("%d %d %d\n", s[s_it], s_it, curr_sum);
            if (s[s_it] > '0' && s_it > curr_sum)
                to_add += s_it - curr_sum, curr_sum += s_it - curr_sum;
            curr_sum += s[s_it] - '0';
        }

        printf("Case #%d: %d\n", t, to_add);
    }
    return 0;
}
