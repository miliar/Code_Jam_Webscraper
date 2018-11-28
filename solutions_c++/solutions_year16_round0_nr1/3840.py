#include <stdio.h>
#include <algorithm>
#include <set>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);

    for (int tc = 1; tc <= t; tc++) {
        printf("Case #%d: ", tc);
        long long n;
        scanf("%lld", &n);

        set < int > seen;
        long long i;
        for (i = 1; i < 100000; i++) {
            long long x = n * i;
            while (x) {
                seen.insert(x % 10);
                x /= 10;
            }
            if (seen.size() == 10) break;
        }
        if (i == 100000) printf("INSOMNIA\n");
        else printf("%lld\n", n*i);
    }
    return 0;
}
