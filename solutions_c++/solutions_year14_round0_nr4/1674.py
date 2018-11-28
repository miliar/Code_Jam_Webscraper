#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

const int maxn = 2000;

double a[maxn],b[maxn];

int T,n,ans1,ans2;
int main() {
    freopen("d1.in","r",stdin);
    freopen("d1.out","w",stdout);
    scanf("%d",&T);
    for (int kase = 1;kase <= T; kase++) {
        scanf("%d",&n); ans1 = ans2 = 0;
        for (int i = 1;i <= n; i++) scanf("%lf",&a[i]);
        for (int i = 1;i <= n; i++) scanf("%lf",&b[i]);
        sort(a+1,a+n+1); sort(b+1,b+n+1);
        for (int i = 0;i <= n; i++) {
            int tot = 0;
            for (int j = 1;j <= i; j++) {
                if (a[j] > b[n-j+1]) tot++;
            }
            int k = n-i;
            for (int j = n;j >= i+1; j--) {
                while (k && a[j] < b[k]) k--;
                if (k && a[j] > b[k]) { tot++; k--; }
            }
            ans1 = max(ans1,tot);
        }
        for (int i = 1;i <= n; i++) {
             double t = 1; int k = 0;
             for (int j = 1;j <= n; j++) {
                    if (b[j] > a[i] && t > b[j]) { t = b[j]; k = j;}
             }
             if (k == 0) ans2++; else b[k] = 0;
        }
        printf("Case #%d: %d %d\n",kase,ans1,ans2);
    }
    return 0;
}
