#include<bits/stdc++.h>
using namespace std;
int n;
int a[1005];
int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T;
    scanf("%d",&T);
    int ca = 0;
    while (T--) {
        scanf("%d",&n);
        int ans1 = 0,ans2 = 0, m = 0;
        for (int i = 0; i<n; i++) {
            scanf("%d",&a[i]);
            if (i>0) if (a[i-1]-a[i]>0) {
                ans1 += a[i-1]-a[i];
                m = max(m,a[i-1]-a[i]);
            }
        }
        for (int i = 0; i<n-1; i++)
            ans2 += min(a[i],m);

        printf("Case #%d: %d %d\n",++ca,ans1,ans2);

    }
}
