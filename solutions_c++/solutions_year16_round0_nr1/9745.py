#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

bool vis[12];

void solve(ll N) {
    memset(vis, false, sizeof vis);
    int tot = 0;
    for(int i = 1; ; ++i) {
        ll n = N * i;
        while(n > 0) {
            ll t = n % 10;
            n /= 10;
            if(!vis[t]) {
                vis[t] = true;
                ++tot;
            }
        }
        if(tot >= 10) {
            printf("%lld\n", N * i);
            return;
        }
    }
}

int main() {
    freopen("C:\\Users\\kun\\Desktop\\A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, kase = 0; scanf("%d", &T);
    while(T--) {
        ll N; scanf("%lld", &N);
        printf("Case #%d: ", ++kase);
        if(N == 0) {
            printf("INSOMNIA\n");
        } else {
            solve(N);
        }
    }
    return 0;
}
