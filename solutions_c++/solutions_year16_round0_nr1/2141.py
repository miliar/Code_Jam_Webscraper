#include <bits/stdc++.h>

using namespace std;

int T, cas, n, vis[10];

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> T;
    while (T --) {
        scanf("%d", &n);
        printf("Case #%d: ", ++ cas);
        if (n == 0) {
            puts("INSOMNIA");
            continue;
        }
        memset(vis, 0, sizeof(vis));
        int cnt = 10;
        long long cur = n;
        while (1) {
            long long temp = cur;
            while (temp) {
                int digit = temp % 10;
                if (vis[digit] == 0) {
                    vis[digit] = 1;
                    cnt --;
                }
                temp /= 10;
            }
            if (cnt == 0) break;
            cur += n;
        }
        printf("%lld\n", cur);
    }
}
