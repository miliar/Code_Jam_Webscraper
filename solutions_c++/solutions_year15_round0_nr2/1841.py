#include <cstdio>
#include <algorithm>
using namespace std;

const int maxn = 1100;
int p[maxn];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int T = 1; T <= cas; T ++) {
        int n;
        scanf("%d", &n);
        int ans = 0;
        for (int i = 0; i < n; i ++) {
            scanf("%d", &p[i]);
            ans = max(ans, p[i]);
        }
        for (int limit = 1; limit <= ans; limit ++) {
            int tmp = limit;
            for (int i = 0; i < n; i ++) {
                tmp += (p[i] + limit - 1) / limit - 1;
            }
            ans = min(ans, tmp);
        }
        printf("Case #%d: %d\n", T, ans);
    }
    return 0;
}
