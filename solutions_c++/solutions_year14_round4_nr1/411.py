#include <iostream>
#include <algorithm>
using namespace std;
const int MAXN = 11111;
int a[MAXN];
int main() {
    int cases;
    scanf("%d", &cases);
    for (int T = 1; T <= cases; T++) {
        int n, x;
        scanf("%d %d", &n, &x);
        for (int i = 0; i < n; i++) {
            scanf("%d", &a[i]);
        }
        sort(a, a + n);
        int j = n - 1;
        int i = 0;
        int ans = 0;
        while (i <= j) {
            /*while (i + 1 < j && a[i] + a[j] <= x) {
                i++;
            }
            if (a[i] + a[j] <= x) {
                ans++;
            } else {
                ans++;
            }
            j--;*/
            if (i < j && a[i] + a[j] <= x) {
                ans++;
                i++;
                j--;
            } else {
                ans++;
                j--;
            }
        }
        printf("Case #%d: %d\n", T, ans);
    }
}