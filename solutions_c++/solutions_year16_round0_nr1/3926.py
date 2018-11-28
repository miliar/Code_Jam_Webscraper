#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int vis[20];

int main() {
    int t, cas = 1;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: ", cas++);
        int n, cnt = 0;
        scanf("%d", &n);
        memset(vis, 0, sizeof(vis));
        for (int i = 1; i <= 1000000; i++) {
            long long now = 1ll * i * n;
            while (now) {
                int t = now % 10;
                now /= 10;
                if (!vis[t]) cnt++, vis[t] = 1;
            }
            if (cnt == 10) {
                printf("%lld\n", i * n);
                break;
            }
        }
        if (cnt != 10) {
            printf("INSOMNIA\n");
        }
    }
}
