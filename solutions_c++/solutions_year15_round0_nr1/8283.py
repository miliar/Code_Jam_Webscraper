#include <stdio.h>

const int MAX_STR_LEN = 1024;

int main() {
    int t;
    int ret = scanf("%d", &t);
    char buf[MAX_STR_LEN];
    for (int i = 0; i < t; ++i) {
        int smax;
        ret = scanf("%d%s", &smax, buf);
        int ans = 0;
        int acc = 0;
        for (int j = 0; j <= smax; ++j) {
            int ac = buf[j] - '0';
            if (ac > 0) {
                if (acc < j) {
                    ans += (j - acc);
                    acc = j+ac;
                }
                else {
                    acc += ac;
                }
            }
        }

        printf("Case #%d: %d\n", i+1, ans);
    }

    return 0;
}
