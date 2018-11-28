#include <algorithm>
#include <cstdio>
#include <set>
using namespace std;

typedef long long ll;

int main() {
    int T;
    ll N;

    scanf("%d", &T);

    for (int j = 1; j <= T; ++j) {
        scanf("%lld", &N);
        printf("Case #%d: ", j);
        if (N == 0) {
            printf("INSOMNIA\n");
        } else {
            int check = 0;

            for (ll k = N, l;; k += N) {
                l = k;
                while (l > 0) {
                    int t = l % 10;
                    check |= 1 << t;
                    l /= 10;
                }

                if (check == (1 << 10) - 1) {
                    printf("%lld\n", k);
                    break;
                }
            }
        }
    }

    return 0;
}
