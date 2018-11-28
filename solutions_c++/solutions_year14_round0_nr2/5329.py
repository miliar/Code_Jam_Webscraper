#include <cstdio>
#include <cfloat>
double C,F,X;
double calc(int n) {
    double A=2,ans=0;
    for(int i=0;i<n;i++) {
        ans+=C/A;
        A+=F;
    }
    return ans+(X/A);
}
void solve(int T) {
    printf("Case #%d: ",T);
    scanf("%lf %lf %lf",&C,&F,&X);
    double prv=DBL_MAX;
    for(int i=0;;i++) {
        double ret=calc(i);
        if(prv>ret) prv=ret;
        else break;
    }
    printf("%.7lf\n",prv);
}
int main() {
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++) {
        solve(i);
    }
}
