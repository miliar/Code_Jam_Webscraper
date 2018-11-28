#include <set>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

const int maxn = 1024;
int a[maxn];
int l[maxn], r[maxn];

int solve() {
    memset(a, 0, sizeof(a));
    memset(l, 0, sizeof(a));
    memset(r, 0, sizeof(a));

    int n, s;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%d", a + i);
    }

    for (int i = 0; i < n; ++i)
        for (int j = i + 1; j < n; ++j) {
            if (a[i] < a[j]) {
                r[i] ++;
            } else if (a[i] > a[j]) {
                l[j] ++;
            }
        }

    int ans = 0;
    for (int i = 0; i < n; ++i) ans += min(l[i], r[i]);

    return ans;
}

int main() {
    freopen("B-large.in", "r", stdin);
    int T;
    scanf("%d", &T);
    for (int i  = 1; i <= T; ++i)  {
        printf("Case #%d: %d\n", i, solve());
    }
    return 0;
}
