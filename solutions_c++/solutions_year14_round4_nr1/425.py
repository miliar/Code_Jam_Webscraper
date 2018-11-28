#include <cstdio>
#include <algorithm>
#include <cassert>
using namespace std;

int cnt[707];
int main() {
    int nt;
    assert(scanf("%d", &nt) == 1);
    for (int tt = 1; tt <= nt; tt++) {
        int n, x;
        assert(scanf("%d%d", &n, &x) == 2);
        for (int i = 0; i <= x; i++) {
            cnt[i] = 0;
        }
        for (int i = 0; i < n; i++) {
            int s;
            assert(scanf("%d", &s) == 1);
            cnt[s]++;
        }
        int ans = 0;
        for (int i = x; i >= 0; i--) {
            for (int j = i; j >= 0; j--) {
                if (i + j <= x) {
                    if (i != j) {
                        int take = min(cnt[i], cnt[j]);
                        ans += take;
                        cnt[i] -= take;
                        cnt[j] -= take;
                    } else {
                        ans += cnt[i] / 2;
                        cnt[i] %= 2;
                    }
                }
            }
            ans += cnt[i];
        }
        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}
