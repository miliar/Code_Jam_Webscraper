#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i=0;i<int(n);++i)
#define out(x) cout<<#x"="<<x<<endl
double r[123], c[123];
int sgn(double x){
    if (fabs(x)<1e-8) return 0;
    return x>0?1:-1;
}
int main(){
    int T;
    scanf("%d",&T);
    REP(tt,T){
        int n; double v, x;
        double ans=-1;
        scanf("%d%lf%lf",&n,&v,&x);
        REP(i,n)scanf("%lf%lf",r+i,c+i);
        if(n==2 && sgn(c[0]-c[1])==0){
            n=1;
            r[0]+=r[1];
        }
        if(n==1){
            if(sgn(c[0]-x)==0)ans=v/r[0];
        } else {
            if(c[1]<c[0]){
                swap(c[0],c[1]);
                swap(r[0],r[1]);
            }
            // c[1] > c[0]
            if(sgn(c[0]-x)==0){
                ans=v/r[0];
            } else if(sgn(c[1]-x)==0){
                ans=v/r[1];
            } else if(c[0]<x && x<c[1]){
                //out("here");
                double t0, t1;
                t1 = (x*v/c[0]/r[0] - v/r[0])/(c[1]*r[1]/c[0]/r[0]-r[1]/r[0]);
                t0 = v/r[0] - t1*r[1]/r[0];
                //out(t0);
                //out(t1);
                assert(t0>-1e-8);
                assert(t1>-1e-8);
                ans = max(t0, t1);
            }
        }
        printf("Case #%d: ", tt+1);
        if(ans<0)puts("IMPOSSIBLE");
        else printf("%.10lf\n", ans);
    }
}
