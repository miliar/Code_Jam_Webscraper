#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1000 + 10;

int main() {
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);
    int T, n, a;
    int nums[MAXN];
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d", &n);
        memset(nums, 0, sizeof(nums));
        for (int i = 0; i < n; ++i) {
            scanf("%d", &a);
            ++nums[a];
        }
        int ans = 0x3f3f3f3f;
        for (int i = 1; i <= 1000; ++i) {
            int cnt = 0;
            for (int j = i + 1; j <= 1000; ++j) {
                if (nums[j]) {
                    if (j % i == 0) {
                        cnt += nums[j] * (j / i - 1);
                    } else {
                        cnt += nums[j] * (j / i);
                    }
                }
            }
            if (i < 10)
            //cout << i << " " << cnt << endl;
            ans = min(ans, i + cnt);
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
