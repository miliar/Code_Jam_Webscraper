#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

int t;
LL n;

int calc(LL n) {
    bool vis[10];
    memset(vis, 0, sizeof(vis));

    int count = 0;
    for (int i = 1; ; ++i) {
        LL tmp = n * i;
        while (tmp) {
            int lst = tmp % 10;
            tmp /= 10;
            if (!vis[lst]) {
                ++count;
                vis[lst] = true;
            }
        }
        if (count == 10) return n * i;
    }
}

int main() {
    cin >> t;
    for (int cas = 0; cas < t; ++cas) {
        cin >> n;
        printf("Case #%d: ", cas + 1);
        if (n == 0) cout << "INSOMNIA" << endl;
        else cout << calc(n) << endl;
    }
}
