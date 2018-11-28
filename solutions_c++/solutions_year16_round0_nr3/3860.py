#include <cmath>
#include <cstdio>
#include <cstring>

using namespace std;
#define ll long long
ll ans[11];

ll not_prime(ll v) {
    ll sqrt_v = sqrt(v);
    for (ll d = 2; d <= sqrt_v; ++d){
        if (v % d == 0){
            return d;
        }
    }
    return -1;
}

int main() {
    freopen("t.in", "r", stdin);
    freopen("t.out", "w", stdout);
    int t, n, j;
    scanf("%d%d%d", &t, &n, &j);
    printf("Case #1:\n");
    ll x = 1 << (n - 1);
    int cnt = 0;
    while (cnt < j) {
        bool ok = false;
        if ((x & 1) && (x & (1 << (n - 1)))) {
            ok = true;
        }
        for (int i = 2; ok && i <= 10; ++i) {
            ll y = x, v = 0, a = 1;
            for (int k = 0; k < n; ++k) {
                if (y & 1) {
                    v += a;
                }
                a *= i;
                y >>= 1;
            }
            ans[i] = not_prime(v);
            if (ans[i] == -1) {
                ok = false;
            }
        }
        if (ok) {
            ll y = x;
            for (int i = n - 1; i >= 0; --i) {
                putchar((y & (1 << i)) ? '1' : '0');
            }
            for (int i = 2; i <= 10; ++i) {
                printf(" %lld", ans[i]);
            }
            puts("");
            ++cnt;
        }
        ++x;
    }
    return 0;
}
