
#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;
int vis[11];
int cnt;

int judge(int x) {
    while (x) {
        int m = x % 10;
        if(!vis[m]) {
            vis[m] = 1;
            cnt++;
        }
        if (cnt == 10) {
            return 1;
        }
        x /= 10;
    }
    return 0;
}

int main(int argc, const char * argv[]) {
    freopen("/Users/onroadrui/Desktop/A/A/A-large.in", "r", stdin);
    freopen("/Users/onroadrui/Desktop/A/A/A-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        int n;
        memset(vis, 0, sizeof(vis));
        cnt = 0;
        int ans = 0;
        scanf("%d", &n);
        for (int j = 1; j <= 100; j++) {
            if (judge(j * n)) {
                ans = j * n;
                break;
            }
        }
        printf("Case #%d: ", i);
        if (ans) {
            printf("%d\n", ans);
        } else {
            printf("INSOMNIA\n");
        }
    }
    return 0;
}
