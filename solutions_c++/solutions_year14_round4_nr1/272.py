#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int n, x, a[20000], u[20000];

int main() {
    int T;
    scanf("%d", &T);
    for (int _q = 0; _q < T; _q++) {
        scanf("%d", &n);
        scanf("%d", &x);
        rep (i, n) scanf("%d", a+i);
        sort(a, a+n);
        reverse(a, a+n);
        memset(u, 0, sizeof(u));
        int c = 0;
        rep (i, n) if (u[i] == 0) {
            int j = i+1;
            while (j < n) {
                if (u[j] == 0 && a[i] + a[j] <= x) {
                    u[j] = 1;
                    break;
                }
                j++;
            }
            c++;
        }
        printf("Case #%d: %d\n", _q+1, c);
    }
    return 0;
}
