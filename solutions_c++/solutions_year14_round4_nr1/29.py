#include <cstdio>
#include <set>
using namespace std;

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    int T;
    
    scanf("%d", &T);
    for (int tc = 1; tc <= T; ++tc) {
        int n, m; multiset<int> S;
        scanf("%d%d", &n, &m);
        for (int i = 1; i <= n; ++i) {
            int k;
            
            scanf("%d", &k);
            S.insert(k);
        }

        int ans = 0;
        for (; !S.empty(); ) {
            auto x = *S.rbegin();
            // printf("%d\n", x);
            S.erase(S.find(x));
            ++ans;
            if (S.empty()) break;
            auto y = S.upper_bound(m - x);
            if (y == S.begin()) continue;
            S.erase(--y);
        }
        printf("Case #%d: %d\n", tc, ans);
    }
    return 0;
}
