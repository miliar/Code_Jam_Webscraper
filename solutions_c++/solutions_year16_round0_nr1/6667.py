#include <cstdio>
using namespace std;
int main()
{
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        long long n;
        scanf("%lld", &n);
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", i + 1);
            continue;
        }
        int h[10] = {0}, count = 0;
        long long m = n;
        while (count < 10) {
            long long t = n;
            while (t != 0) {
                if (! h[t % 10])
                    h[t % 10] = 1, count = count + 1;
                t /= 10;
            }
            if (count < 10)
                n += m;
        }
        printf("Case #%d: %lld\n", i + 1, n);
    }
    return 0;
}
