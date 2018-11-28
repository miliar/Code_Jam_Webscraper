#include<bits/stdc++.h>
#define MAX   111
#define FOR(i,a,b) for (int i=(a),_b=(b);i<=_b;i=i+1)
#define fi   first
#define se   second
using namespace std;
const char noAns[]="IMPOSSIBLE";
const double eps=1e-9;
double Abs(double x) {
    return (x<0?-x:x);
}
int n;
double v,t;
pair<double,double> a[MAX];
void init(void) {
    scanf("%d%lf%lf",&n,&v,&t);
    FOR(i,1,n) scanf("%lf%lf",&a[i].fi,&a[i].se);
}
void process(int tc) {
    printf("Case #%d: ",tc);
    if (n==1) {
        if (Abs(a[1].se-t)>eps) printf("%s\n",noAns);
        else printf("%.9lf\n",v/a[1].fi);
        return;
    }
    if (n==2) {
        double a1=1;
        double b1=1;
        double c1=v;
        double a2=a[1].se;
        double b2=a[2].se;
        double c2=v*t;
        double d=a1*b2-a2*b1;
        double dx=c1*b2-c2*b1;
        double dy=a1*c2-a2*c1;
        if (Abs(d)<=eps) {
            if (Abs(dx)>eps || Abs(dy)>eps) {
                printf("%s\n",noAns);
                return;
            } else {
                printf("%.9lf\n",v/(a[1].fi+a[2].fi));
                return;
            }
        } else {
            double x=dx/d;
            double y=dy/d;
            if (x<-eps || y<-eps) printf("%s\n",noAns);
            else printf("%.9lf\n",max(x/a[1].fi,y/a[2].fi));
        }
    }
}
int main(void) {
    int t;
    scanf("%d",&t);
    FOR(i,1,t) {
        init();
        process(i);
    }
    return 0;
}
