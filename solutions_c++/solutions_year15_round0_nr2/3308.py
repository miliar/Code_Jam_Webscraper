#include <bits/stdc++.h>
#define rep(i,a,b) for(int i=a; i<b; ++i)
#define clr(a,b) memset(a,b,sizeof(a))
using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("gcj-qualification-b.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++ cas) {

        int d;
        scanf("%d", &d);
        vector<int> a(d);
        rep(i, 0, d) scanf("%d", &a[i]);

        int ret = INT_MAX;
        int p = INT_MIN;
        rep(i, 0, d) p = max(p, a[i]);
        rep(i, 1, p + 1) {
            int cur = 0;

            rep(j, 0, d) {
                if(a[j] > i) {
                    cur += (a[j] - 1) / i;
                }
            }

            ret = min(ret, cur + i);
        }

        printf("Case #%d: %d\n", cas, ret);
    }

    return 0;
}
