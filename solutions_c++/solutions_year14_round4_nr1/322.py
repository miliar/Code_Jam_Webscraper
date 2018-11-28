#include <stdio.h>
#include <algorithm>
using namespace std;
int c[10010];
int main(){
    int T, ri = 1, n, m, i, x, ans;
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d%d", &n, &m);
        for (i = 0; i < n; i++) scanf("%d", &c[i]);
        sort(c, c + n);
        ans = 0;
        x = 0;
        for (i = n - 1; i >= x; i--){
            ans++;
            if (c[i] + c[x] <= m) x++;
        }
        printf("Case #%d: %d\n", ri++, ans);
    }
    return 0;
}
