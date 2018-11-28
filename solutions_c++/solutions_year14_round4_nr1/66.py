#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n, t;
int a[10005];
int u[10005];

void read() {
    scanf("%d%d", &n, &t);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &a[i]);
    }
}

void solve() {
    int ans = 0;
    memset(u, 0, sizeof u);
    sort(a + 1, a + n + 1);
    
    for (int i = n; i >= 1; i--) {
        if (!u[i]) {
            u[i] = 1;
            ++ ans;
            
            for (int j = 1; j <= n; j++) {
                if (!u[j] && a[i] + a[j] <= t) {
                    u[j] = 1;
                    break;
                }
            }
        }
    }
    
    printf ("%d\n", ans);
}

int main() {
    int cases;
    
    scanf("%d", &cases);
    for (int i = 1; i <= cases; i++) {
        read();
        printf ("Case #%d: ", i);
        solve();
    }
    
    return 0;
}
