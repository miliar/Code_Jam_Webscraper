#include <cstdio>
#include <algorithm>
using namespace std;

#define MAX 1005

int b, n, a[MAX];

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &b, &n);
        for (int i = 0; i < b; i++)
            scanf("%d", &a[i]);
        long long lo = 0, hi = 0x3f3f3f3f3f3f3f3fLL;
        while (lo < hi) {
            long long mi = (lo + hi) / 2;
            long long cnt = 0, on = 0;
            for (int i = 0; i < b && cnt < n; i++) {
                cnt += (mi-1) / a[i] + 1;
                on += mi % a[i] == 0 ? 1 : 0;
            }
            if (cnt + on < n)
                lo = mi + 1;
            else if (cnt >= n)
                hi = mi - 1;
            else // cnt < n && cnt + on >= n
                lo = hi = mi;
        }
        long long cnt = 0;
        for (int i = 0; i < b; i++)
            cnt += (lo-1) / a[i] + 1;
        long long pos = n - cnt;
        int last = -1;
        for (int i = 0; i < b && pos > 0; i++) {
            if (lo % a[i] == 0) {
                last = i;
                pos--;
            }
        }
        printf("Case #%d: %d\n", t, last + 1);
    }
}
