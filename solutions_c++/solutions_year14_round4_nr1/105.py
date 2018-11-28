#include <set>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

const int maxcnt = 800;
int cnt[maxcnt];
int rem[maxcnt];

int solve() {
    memset(cnt, 0, sizeof(cnt));
    memset(rem, 0, sizeof(rem));
    int n, x, s;
    scanf("%d%d", &n, &x);
    while (n--) {
        scanf("%d", &s);
        cnt[s] ++;
    }

    int ans = 0;
    for (int i = maxcnt - 1; i > 0; --i) {
        if (cnt[i] < rem[i]) {
            rem[i - 1] += rem[i] - cnt[i];
        } else {
            int dt = cnt[i] - rem[i];
            if (i * 2 <= x) {
                ans += dt / 2;
                dt %= 2;
            }
            ans += dt;
            rem[min(x - i, i-1)] += dt;
        }
        rem[i] = 0;
    }
    return ans;
}

int main() {
    freopen("A.txt", "r", stdin);
    int T;
    scanf("%d", &T);
    for (int i  = 1; i <= T; ++i)  {
        printf("Case #%d: %d\n", i, solve());
    }
    return 0;
}
