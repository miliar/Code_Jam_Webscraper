#include <cstdio>
#include <cstring>
#include <cassert>
#include <algorithm>
using namespace std;

#define MAXN 110

int A, n, a[MAXN];

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &A, &n);
        for (int i = 0; i < n; i++)
            scanf("%d", &a[i]);
        if (A == 1) {
            printf("Case #%d: %d\n", t, n);
            continue;
        }
        sort(a, a+n);
        int ans = 500;
        for (int m = 0; m < n; m++) {
            int cnt = 0;
            int tmp = A;
            int i;
            for (i = 0; cnt < m && i < n; ) {
                if (tmp > a[i]) {
                    tmp += a[i];
                    i++;
                }
                else {
                    tmp += tmp-1;
                    cnt++;
                }
            }
            while (i < n && tmp > a[i]) {
                tmp += a[i];
                i++;
            }
            ans = min(ans, m + n-i);
        }
        printf("Case #%d: %d\n", t, ans);
    }
}
