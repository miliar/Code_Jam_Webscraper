#include <cstdio>
#include <cassert>
#include <algorithm>
using namespace std;

const int INF = 1 << 28;

int a[1010];
int b[1010];
int f[1010];

int main() {
    int nt;
    assert(scanf("%d", &nt) == 1);
    for (int tt = 1; tt <= nt; tt++) {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &a[i]);
            b[i] = a[i];
        }
        sort(b + 0, b + n);
        for (int i = 0; i < n; i++) {
            a[i] = lower_bound(b + 0, b + n, a[i]) - b;
        }
        int ans = 0;
        for (int cur = 0; cur < n; cur++) {
            int pos = -1;
            for (int i = 0; i < n; i++) {
                if (a[i] == cur) {
                    pos = i;
                    break;
                }
            }
            int cnt0 = 0;
            int cnt1 = 0;
            for (int i = 0; i < pos; i++) {
                if (a[i] > cur) {
                    cnt0 = pos - i;
                    break;
                }
            }
            for (int i = n - 1; i > pos; i--) {
                if (a[i] > cur) {
                    cnt1 = i - pos;
                    break;
                }
            }
            if (cnt0 < cnt1) {
                ans += cnt0;
                while (cnt0 > 0) {
                    cnt0--;
                    swap(a[pos - 1], a[pos]);
                    pos--;
                }
            } else {
                ans += cnt1;
                while (cnt1 > 0) {
                    cnt1--;
                    swap(a[pos], a[pos + 1]);
                    pos++;
                }
            }
        }
        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}
