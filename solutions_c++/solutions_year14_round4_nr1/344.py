#include <cstdio>
#include <algorithm>
using namespace std;
const int maxn = 10000;
int a[maxn];
int main() {
    int t;
    freopen("1.txt", "r", stdin);
    freopen("2.txt", "w", stdout);
    scanf("%d", &t);
    for (int c = 0 ; c < t ; ++c) {
        int n, x, v = 0;
        scanf("%d%d", &n, &x);
        for (int i = 0 ; i < n ; ++i) scanf("%d", a + i);
        sort(a, a + n);
        int l = 0, r = n - 1;
        while (l <= r) {
            if (l == r || a[l] + a[r] <= x) ++v, ++l, --r;
            else ++v, --r;
        }
        printf("Case #%d: %d\n", c + 1, v);
    }
    return 0;
}
