#include<cstdio>
#include<algorithm>
using namespace std;
const int MAXN=105;
const double EPS=1e-5;
struct pipe {
    double r,c;
    pipe(double _r=0,double _c=0):r(_r),c(_c) {}
    bool operator<(const pipe &oth) const {
        return c<oth.c;
    }
} s[MAXN];
int main() {
    //freopen("B-small-attempt2.in","r",stdin);
    //freopen("B-small-attempt2.out","w",stdout);
    int t,n;
    double v,x,ans;
    scanf("%d",&t);
    for(int cas=1; cas<=t; ++cas) {
        scanf("%d%lf%lf",&n,&v,&x);
        for(int i=0; i<n; ++i)
            scanf("%lf%lf",&s[i].r,&s[i].c);
        sort(s,s+n);
        printf("Case #%d: ",cas);
        if(s[0].c>x+EPS||s[n-1].c<x-EPS)
            puts("IMPOSSIBLE");
        else {
            if(n==1)
                ans=v/s[0].r;
            else if(s[0].c==s[n-1].c)
                ans=v/(s[0].r+s[n-1].r);
            else
                ans=max((x-s[0].c)/(s[n-1].c-s[0].c)*v/s[n-1].r,(x-s[n-1].c)/(s[0].c-s[n-1].c)*v/s[0].r);
            printf("%.9f\n",ans);
        }
    }
}
