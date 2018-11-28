#include<cstdio>
#include<algorithm>
using namespace std;
const int N = 1013;
double a[N],b[N];
int K,sTT,n;
int main() {
    scanf("%d", &sTT);
    for (int TT = 1; TT <= sTT; ++TT) {
        scanf("%d", &n);
        for (int i = 1; i <= n; ++i) scanf("%lf", a + i);
        for (int i = 1; i <= n; ++i) scanf("%lf", b + i);
        sort(a + 1, a + n + 1);
        sort(b + 1, b + n + 1);
        K = 0;
        for (int i = 1, j = 1; i <= n && j <= n; ++i) {
            while (j <= n && a[j] <= b[i]) ++ j;
            if (j <= n) {
                ++ j;
                ++ K;
            }
        }
        printf("Case #%d: %d ", TT, K);
        K = n;
        for (int i = 1, j = 1; i <= n && j <= n; ++i) {
            while (j <= n && a[i] >= b[j]) ++ j;
            if (j <= n) {
                ++ j;
                -- K;
            }
        }
        printf("%d\n", K);
    }
    return 0;
}
