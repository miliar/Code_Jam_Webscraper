#include <map>
#include <queue>
#include <cmath>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define ll long long
#define INF 1000000007

using namespace std;

bool vis[15];

void solve(int n) {
    memset(vis, false, sizeof(vis));
    bool flg = true;
    for (int i = 1; i <= 1000000 && flg; ++ i) {
        ll ave = (ll) i * n;
        while (ave) vis[ave % 10] = true, ave /= 10;
        flg = false;
        for (int j = 0; j <= 9; ++ j) if (!vis[j]) flg = true;
        if (!flg) { printf("%lld\n", (ll) i * n); return; }
    }
    printf("INSOMNIA\n");
}

int main() {

    int T, n;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++ t) {
        scanf("%d", &n);
        printf("Case #%d: ", t);
        solve(n);
    }
    return 0;

}

