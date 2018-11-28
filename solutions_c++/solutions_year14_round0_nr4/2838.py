#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;
typedef long long ll;

#define FR(i,en) for(int i=0; i<(int)(en); i++)
#define FOR(i,st,en) for(int i=(st); i<(int)(en); i++)


int main()
{
    int t, n, w, w_max, dw, dw_max, mi;
    double d[2000];
    double m, pm;
    scanf("%d",&t);
    FR (test_cases,t) {
        printf("Case #%d: ",test_cases+1);
        scanf("%d",&n);
        FR(i,2*n) scanf("%lf",&d[i]);
        w=0;
        w_max=0;
        dw_max=0;
        pm=2.0;
        FR(i,2*n) {
            m=0.0;
            FR(j,2*n) if ((d[j]>m)&&d[j]<pm) {mi=j; m=d[j];}
            pm=m;
            if (mi < n) w++; else w--;
            if (w > w_max) w_max=w;
            if (w < dw_max) dw_max=w;
            //printf("%d %d %d %d %lf\n",i,mi,w,dw_max,pm);
        }
        printf("%d %d\n",n+dw_max,w_max);
    }
    return 0;
}
