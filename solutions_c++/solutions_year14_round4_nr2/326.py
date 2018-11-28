#include <stdio.h>
#include <algorithm>
using namespace std;
struct abc{
    int id, v;
    bool operator < (const abc &a) const{
        return v < a.v;
    }
}c[1010];
int u[1010];
int main(){
    int T, ri = 1, n, i, j, ans = 0, p;
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d", &n);
        for (i = 0; i < n; i++){
            scanf("%d", &c[i].v);
            c[i].id = i;
        }
        sort(c, c + n);
        ans = 0;
        for (i = 0; i < n; i++) u[i] = 1;
        for (i = 0; i < n; i++){
            int t = 0;
            for (j = 0; j < c[i].id; j++) t += u[j];
            ans += min(t, n - 1 - i - t);
            u[c[i].id] = 0;
        }
        printf("Case #%d: %d\n", ri++, ans);
    }
    return 0;
}
