#include <cstdio>
#include <cstdlib>
#include <cstring>

const int N = 1010;

char shy[N];

int main(void)
{
    int T, S;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        scanf("%d %s", &S, shy);
        int res = 0, now = shy[0] - '0';
        for (int j = 1; j <= S; j++) {
            if (now < j) {
                res += j - now;
                now = j;
            }
            now += shy[j] - '0';
        }
        printf("Case #%d: %d\n", i, res);
    }
    return EXIT_SUCCESS;
}
