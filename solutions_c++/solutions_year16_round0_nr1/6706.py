#include <stdio.h>
#include <stdint.h>

int main()
{
    int t;
    scanf("%d", &t);
    for (int cases = 1; cases <= t; cases++) {
        int n;
        scanf("%d", &n);
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", cases);
        } else {
            bool num[10] = {0};
            int count = 0;
            uint64_t ans = n;

            while (count < 10) {
                int tmp = ans;

                while (tmp > 0) {
                    if (!num[tmp % 10]) {
                        num[tmp % 10] = true;
                        count++;
                    }
                    tmp /= 10;
                }

                if (count == 10) {
                    break;
                }

                ans += n;
            }

            printf("Case #%d: %llu\n", cases, ans);
        }
    }
    return 0;
}
