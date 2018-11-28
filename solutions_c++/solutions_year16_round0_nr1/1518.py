#include <bits/stdc++.h>

using namespace std;

bool vis[10];

bool check(long long x) {
    while (x) {
        vis[x % 10] = 1;
        x /= 10;
    }
    return vis[0] && vis[1] && vis[2] && vis[3] && vis[4] && vis[5] && vis[6] && vis[7] && vis[8] && vis[9];
}

int main() {
    int t, tcase = 0;
    cin >> t;
    while (t--) {
        long long n;
        cin >> n;
        memset(vis, 0, sizeof(vis));
        int mul = 1;
        bool flag = true;
        while (!check(mul * n)) {
            mul++;
            if (mul > 100) {
                flag = false;
                break;
            }
        }
        if (flag)
            printf("Case #%d: %d\n", ++tcase, mul*n);
        else printf("Case #%d: INSOMNIA\n", ++tcase);
    }
    return 0;
}