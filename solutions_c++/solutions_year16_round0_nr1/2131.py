#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int dp[10];

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t ++) {
        ll n;
        cin >> n;
        if(n == 0) {
            printf("Case #%d: INSOMNIA\n", t);
            continue;
        }
        memset(dp, 0, sizeof(dp));
        int i, cnt = 0;
        for(i = 1; i < 1000000; i ++) {
            ll m = n * i;
            bool ok = false;
            while(m) {
                int val = m % 10;
                if(dp[val] == 0) {
                    dp[val] = 1;
                    cnt ++;
                    if(cnt == 10) {
                        ok = true;
                        printf("Case #%d: %d\n", t, n * i);
                        break;
                    }
                }
                m /= 10;
            }
            if(ok) break;
        }
    }
    return 0;
}
