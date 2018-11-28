#include <stdio.h>
#include <algorithm>
using namespace std;
int a[1010], b[1010];
int main(){
    int T, ri = 1, n, i, p;
    double num;
    freopen("D-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d", &n);
        for (i = 0; i < n; i++){
            scanf("%lf", &num);
            a[i] = (num + 1e-8) * 100000;
        }
        for (i = 0; i < n; i++){
            scanf("%lf", &num);
            b[i] = (num + 1e-8) * 100000;
        }
        sort(a, a + n);
        sort(b, b + n);
        printf("Case #%d: ", ri++);
        int re = 0, x = 0;
        for (i = 0; i < n; i++){
            if (a[i] > b[x]){
                re++;
                x++;
            }
        }
        printf("%d ", re);
        p = 0;
        for (i = 0; i < n; i++){
            while (p < n && a[i] > b[p]) p++;
            if (p == n) break;
            p++;
        }
        printf("%d\n", n - i);
    }
    return 0;
}
