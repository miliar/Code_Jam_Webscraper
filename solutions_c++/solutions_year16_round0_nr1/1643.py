#include <cinttypes>
#include <cstdio>

using namespace std;

const int BASE = 10;

int64_t find(int n)
{
    int cnt = 0;
    bool seen[BASE];
    int64_t k = 0;

    if (n == 0)
        return -1;

    while (cnt < BASE) {
        k += n;
        int64_t z = k;

        while (z > 0) {
            if (!seen[z % BASE]) {
                seen[z % BASE] = true;
                cnt++;
            }
            z /= BASE;
        }
    }

    return k;
}

int main()
{
    int t;
    scanf("%d", &t);

    for (int i = 1; i <= t; i++) {
        int n;
        scanf("%d", &n);
        printf("Case #%d: ", i);

        int64_t ans = find(n);
        if (ans != -1)
            printf("%" PRId64 "\n", ans);
        else puts("INSOMNIA");
    }

    return 0;
}
