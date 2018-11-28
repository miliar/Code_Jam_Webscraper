#include<cstdio>
#include<algorithm>
using namespace std;
const int N = 113;
int a[N][N],l[N],h[N],n,m,mm,TT;
bool work() {
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            if (a[i][j] < l[i] && a[i][j] < h[j]) return 0;
    return 1;
}
int main() {
    for (scanf("%d", &TT), mm = TT; TT; --TT) {
        printf("Case #%d: ", mm-TT+1);
        scanf("%d%d", &n, &m);
        fill(l, l + N, 0);
        fill(h, h + N, 0);
        for (int x,i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j) {
                scanf("%d", &x);
                l[i] = max(l[i], x);
                h[j] = max(h[j], x);
                a[i][j] = x;
            }
        if (work()) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
