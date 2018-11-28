#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 1000+5;
const int Inf = 1<<30;
int a[N];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, n, cas = 1;
    scanf("%d", &t);
    while(t--) {
        scanf("%d", &n);
        int mx = 0;
        for(int i = 1;i <= n; i++) {
            scanf("%d", &a[i]);
            mx = max(mx, a[i]);
        }
        int ans = Inf;
        for(int i = 1;i <= mx; i++) {
            int cur = i;
            for(int j = 1;j <= n; j++) if(a[j] > i) {
                cur += (a[j]-i+i-1)/i;
            }
            ans = min(ans, cur);
        }
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}
