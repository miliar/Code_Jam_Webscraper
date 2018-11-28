#include<bits/stdc++.h>
#define pb push_back
#define sz(x) (int)x.size()
#define scf scanf
#define ptf printf
#define fst first
#define scd second
#define forp(i,j,k) for(int i=j;i<k;i++)
#define form(i,j,k) for(int i=j;i>k;i--)
using namespace std;
typedef long long LL;

const double eps=1e-10;

int T;double C,F,X;

inline int sgn(double x){return x>eps?1:(x<-eps?-1:0);}
inline int cmp(double x,double y){return sgn(x-y);}


double cc(int x)
{
    double res=0.0;
    forp(i,0,x+1)res+=C/(2+F*i);
    res+=X/(2+F*x+F);
    return res;
}

int main()
{
    //freopen("1.in","r",stdin);
    //freopen("1.out","w",stdout);
    scf("%d",&T);
    forp(tcnt,0,T)
    {
        scf("%lf%lf%lf",&C,&F,&X);
        ptf("Case #%d: ",tcnt+1);
        if(cmp(X,C)<=0){ptf("%.7f\n",X/2.0);continue;}
        int xx=floor(X/C-1-2/F);
        double ans=min(cc(xx),cc(xx+1));
        ptf("%.7f\n",ans);
    }
    return 0;
}
