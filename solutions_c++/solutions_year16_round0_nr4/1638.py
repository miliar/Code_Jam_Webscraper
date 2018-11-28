#include <cinttypes>
#include <cmath>
#include <cstdio>

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);

    for (int i = 1; i <= t; i++) {
        int k, c, s;
        scanf("%d %d %d", &k, &c, &s);
        printf("Case #%d: ", i);

        int64_t delta = pow((int64_t)k, c - 1);
        int64_t m = delta * k;

        for (int64_t t = 0; t < m; t += delta)
            printf("%" PRId64 " ", t + 1);
        puts("");
    }

    return 0;
}
