#include <cstdio>
#include <algorithm>

using namespace std;

int n, a[2000];

int main(void) {
    freopen("in", "r", stdin);
    freopen("out_b", "w", stdout);
    int kase; scanf("%d", &kase); for (int _ = 1; _ <= kase; _++) {
        scanf("%d", &n); for (int i = 1; i <= n; i++) scanf("%d", a + i);       
        int s = *max_element(a + 1, a + n + 1), Ans = s;
        for (int move = 0; move <= 10000; move++) {
            int l = 1, r = s;
            while (l <= r) {
                int mid = (l + r) >> 1, acc = 0;
                for (int i = 1; i <= n; i++) {
                    acc += a[i] > mid ? (a[i] - mid - 1) / mid + 1: 0;
                }
                if (acc > move) l = mid + 1; else r = mid - 1;
            }
            Ans = min(Ans, move + l);
        }
        printf("Case #%d: %d\n", _, Ans);
    }
    return 0;
}

