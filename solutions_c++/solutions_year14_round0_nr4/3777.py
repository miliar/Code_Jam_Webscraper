#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T,n,i,u = 0,p,o,s,ed;
    scanf("%d", &T);
    while (T--) {
        scanf("%d", &n);
        double p[n],q[n];
        for (i = 0; i < n; i++)
            scanf("%lf", &p[i]);
        for (i = 0; i < n; i++)
            scanf("%lf", &q[i]);
        sort(p,p+n);
        sort(q,q+n);
        ed = n-1;
        o = 0;
        for (i = n-1; i >= 0; i--) {
            if (p[ed] > q[i]) {
                ed--;
                o++;
            }
        }
        s = 0;ed = n-1;
        for (i = n-1; i >= 0; i--) {
            if (p[i] > q[ed])
                s++;
            else
                ed--;
        }
        u++;
        printf("Case #%d: %d %d\n", u, o, s);
    }
}
