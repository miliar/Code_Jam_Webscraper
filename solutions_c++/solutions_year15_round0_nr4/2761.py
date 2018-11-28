#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
bool ck(int k, int n, int m) {
    if (n > m) swap(n, m);
    if ((n * m) % k) return false;
    if (k > n && k > m) return false;
    if (n + 1 + n <= k) return false;
    if (k < 4) return true;
    if (k == 4 && n > 2) return true;
    return false;
}
int main() {
    int T, ri = 1, n, m, k;
    freopen("D-small-attempt3.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d%d", &k, &n, &m);
        printf("Case #%d: %s\n", ri++, ck(k, n, m)?"GABRIEL":"RICHARD");
    }
    return 0;
}
