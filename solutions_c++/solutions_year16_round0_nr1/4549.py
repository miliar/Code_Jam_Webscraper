#include <bitset>
#include <cstdio>
#include <cstring>

using namespace std;
typedef long long ll;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, cas = 0;
    ll n;
    scanf("%d", &t);
    while (t--) {
        scanf("%lld", &n);
        printf("Case #%d: ", ++cas);
        if (n) {
            ll v = n;
            bitset<10> b;
            b.reset();
            ll tmp = v;
            while (tmp) {
                b[tmp % 10] = 1;
                tmp /= 10;
            }
            while (b.count() != 10) {
                v += n;
                ll tmp = v;
                while (tmp) {
                    b[tmp % 10] = 1;
                    tmp /= 10;
                }
            }
            printf("%lld\n", v);
        } else {
            puts("INSOMNIA");
        }
    }
    return 0;
}