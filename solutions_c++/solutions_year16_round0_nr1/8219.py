#include <cstdio>
#include <algorithm>
using namespace std;

bool cnt[10];

typedef long long ll;

int main(void) {
    freopen("A-large.in", "r", stdin);
    freopen("A-large-out.txt", "w", stdout);
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        
        ll n; scanf("%lld", &n);
        if (n == 0) { puts("INSOMNIA"); continue; }
        
        fill(cnt, cnt+10, false);
        int ans = 1;
        while (1) {
            ll tmp = ans * n;
            while (tmp > 0) {
                cnt[tmp%10] = true;
                tmp /= 10;
            }
            bool tag = true;
            for (int i = 0; i < 10; i++)
                tag &= cnt[i];
            if (tag) { printf("%lld\n", ans*n); break; }
            ans++;
        }
    }
    return 0;
}