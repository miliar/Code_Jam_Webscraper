#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#define ll long long
int vis[20];
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int cas;
    double c, f, x, tmp;
    scanf("%d", &cas);
    for (int t=1; t<=cas; t++) {
        scanf("%lf%lf%lf", &c, &f, &x);
        tmp=x/c;
        int l=0, r=ceil(tmp), mid, ret=0;
        while (l<=r) {
            mid=(l+r)/2;
            if ((2+(mid+1)*f)/f>=tmp) {
                ret=mid;
                r=mid-1;
            } else {
                l=mid+1;
            }
        }
        double ans=0;
        for (int i=0; i<ret; i++)
        {
            ans+=c/(2+i*f);
        }
        ans+=x/(2+ret*f);
        printf("Case #%d: ", t);
        printf("%.7lf\n", ans);
    }
    return 0;
}
