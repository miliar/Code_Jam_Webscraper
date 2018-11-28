#include <bits/stdc++.h>
using namespace std;

void solve(int n) {
    if (n == 0) printf("INSOMNIA\n");
    else {
        int cnt = 10;
        bool vis[10];
        fill(vis, vis+10, false);
        int cur = 0;
        while (cnt != 0) {
            cur += n;
            string s = to_string(cur);
            for (const char &c : s) {
                if ( !vis[c-'0'] ) {
                    vis[c-'0'] = true;
                    cnt--;
                }
            }
        }
        printf("%d\n", cur);
    }
}

int main () {
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t, n;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        scanf("%d", &n);
        printf("Case #%d: ", i);
        solve(n);

    }
    return 0;
}