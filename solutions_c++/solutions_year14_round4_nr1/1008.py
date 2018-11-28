#include <cstdio>
#include <algorithm>
using namespace std;
int a[10010];

void work() {
    int n, x, ans = 0;
    scanf("%d%d", &n, &x);
    for(int i = 0; i < n; i ++)
        scanf("%d", a + i);
    int l = 0, r = n - 1;

    sort(a, a + n);
    
    while(l < r) {
        if(a[l] + a[r] <= x) ans ++, l ++, r --;
        else r --, ans ++;
    }

    if(l == r) ans ++;

    printf("%d\n", ans);
}

int main() {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i ++)
        printf("Case #%d: ", i), work();
    return 0;
}
