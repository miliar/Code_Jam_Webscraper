#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

const int maxn = 1001;

int T,N,t1,t2,b[maxn],c[maxn];
int a[maxn],d1[maxn],d2[maxn];
bool vis[11];




int main() {
    #ifndef ONLINE_JUDGE
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    #endif // ONLINE_JUDGE
    scanf("%d",&T);
    for (int kase = 1;kase <= T; kase++) {
        scanf("%d",&N);
        for (int i = 1;i <= N; i++) scanf("%d",&a[i]);
        t1 = 0; t2 = 0; int ans = N*N;
        for (int i = 0;i < (1<<N); i++) {
            t1 = 0; t2 = 0;
            for (int j = 1;j <= N; j++) c[j] = a[j];
            for (int j = 1;j <= N; j++)
                    if ((1<<(j-1)) & i) {t1++; d1[t1] = a[j]; }
                    else { t2++; d2[t2] = a[j]; }
            sort(d1+1,d1+t1+1); sort(d2+1,d2+t2+1);
            for (int j = 1;j <= t1; j++) b[j] = d1[j];
            for (int j = t2;j >= 1; j--) b[t2-j+1+t1] = d2[j];
            int tot = 0;
            for (int j = 1;j <= N; j++) {
            int w = 0;
            for (int k = j;k <= N; k++)
                if (c[k] == b[j]) {w = k; break;}
            for (int k = w;k > j; k--) { tot++; swap(c[k],c[k-1]); }
            }
            ans = min(ans,tot);
        }
        printf("Case #%d: %d\n",kase,ans);
    }
    return 0;
}
