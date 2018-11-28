#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
    int t;
    scanf("%d", &t);

    for (int cs = 1; cs <= t; ++cs) {
        ll n;
        scanf("%lld", &n);

        if (n == 0LL) {
            printf("Case #%d: INSOMNIA\n", cs);
            continue;
        }

        ll result = 0;

        bool seen[10];
        memset(seen, 0, sizeof(seen));

        ll x = 0;
        ll y = 0;

        while (true) {
            x += n;

            ll q = x;
            while (q) {
                ll r = (q % 10);
                q /= 10;

                if (!seen[r]) {
                    seen[r] = true;
                    ++y;
                }
            }

            if (y == 10) {
                result = x;
                break;
            }
        }

        printf("Case #%d: %lld\n", cs, result);
    }
}
