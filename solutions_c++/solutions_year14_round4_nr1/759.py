#include <cstdio>
#include <algorithm>

using namespace std;

int a[1000000];
int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
            int n, x;
        scanf("%d%d", &n, &x);
        for (int i = 0; i < n; i++)
            scanf("%d", &a[i]);
        sort(a, a + n);
        int i = 0, j = n - 1, ans = 0;
        while (i <= j) {
            if (i == j) {
                ans++;break;
            }
            if (a[i] + a[j] <= x) {
                i++;j--;ans++;continue;
            } else {
                ans++;j--;continue;
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
