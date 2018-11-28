#include <bits/stdc++.h>

#define mp make_pair
#define pb push_back
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define what_is(x) cerr << #x << ": " << x << endl;

using namespace std;

const int inf = 1000000;
int T, D;
int p[1000];

int main() {
    #ifdef LOCAL
        freopen("input", "r", stdin);
        freopen("output", "w", stdout);
    #endif

    int mx = 0;

    scanf("%d", &T);
    forn(t, T) {
        scanf("%d", &D);
        forn(i, D) {
            scanf("%d", p + i);
            mx = max(mx, p[i]);
        }

        int ans = inf;
        int res = 0;
        for (int k = 1; k <= mx; k++) {
            res = 0;
            forn(i, D) {
                res += max(0, (p[i] + k - 1) / k - 1);
            }

            ans = min(ans, res + k);
        }

        printf("Case #%d: %d\n", t + 1, ans);
    }

}
