#include<bits/stdc++.h>
#define scf scanf
#define ptf printf
#define forp(i,j,k) for(int i=j;i<k;i++)
#define form(i,j,k) for(int i=j;i>k;i--)
#define sz(x) (int)x.size()
#define pb push_back
#define fst first
#define scd second
#define m_p make_pair
#define pct __builtin_popcount
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
//constant integer SOLVED NOSOL INF
const int N=210,M=210,SOLVED=0,NOSOL=1,INF=2;
const double eps=1e-12,oo=1e20;

int sgn(double x)
{
    return (x>eps)-(x<-eps);
}

int cmp(double x,double y)
{
    return sgn(x-y);
}

struct Simplex_algorithm
{
    int pf[N+M],m,n;
    double a[M][N],b[M],c[N],cc[N],ans;
    void clear()
    {
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        memset(c,0,sizeof(c));
        memset(cc,0,sizeof(cc));
        memset(pf,0,sizeof(pf));
        ans=0.0;
    }
    void pivot(int x,int y)
    {
        swap(pf[x],pf[n+y]);
        ans-=c[x]*b[y]/a[y][x];
        for(int i=0;i<n;i++)if(i!=x)c[i]-=c[x]*a[y][i]/a[y][x];
        c[x]/=a[y][x];
        for(int i=0;i<m;i++)
            if(i!=y)
            {
                b[i]-=b[y]/a[y][x]*a[i][x];
                for(int j=0;j<n;j++)
                    if(j!=x)
                        a[i][j]-=a[y][j]/a[y][x]*a[i][x];
                a[i][x]/=a[y][x];
            }
        b[y]/=-a[y][x];
        for(int i=0;i<n;i++)if(i!=x)a[y][i]/=-a[y][x];
        a[y][x]=1.0/a[y][x];
    }

    int csolve(double v)
    {
        ans=v;int ch,mnn,mxc;double mn;
        for(;;)
        {
            mxc=0;
            for(int i=1;i<n;i++)
                if(c[i]>c[mxc])
                    mxc=i;
            if(c[mxc]<eps)
                return SOLVED;
            mn=oo;
            for(int i=0;i<m;i++)
                    if(a[i][mxc]<-eps)
                    {
                        v=-b[i]/a[i][mxc];
                        if(v<mn)
                        {
                            mn=v;
                            mnn=i;
                        }
                    }
            if(mn<oo)
                pivot(mxc,mnn);
            else
                return INF;
        }
        for(int i=0;i<n;i++)if(sgn(c[i])>0)return NOSOL;
        return SOLVED;
    }

    void solve(int&fg)
    {
        double mb=1.0;int mbi;
        for(int i=0;i<m;i++)if(cmp(mb,b[i])>0){mb=b[i];mbi=i;}
        if(sgn(mb)<0)
        {
            for(int i=0;i<n;i++){cc[i]=c[i];c[i]=0;}
            for(int i=0;i<m;i++)a[i][n]=1;c[n]=-1;n++;
            for(int i=0;i<n+m;i++)pf[i]=i;
            ans=0;pivot(n-1,mbi);csolve(ans);
            if(sgn(ans)<0){fg=NOSOL;return;}
            int tmp;
            for(int i=0;i<n+m;i++)
                if(pf[i]==n-1)
                    if(i>=n)pivot(0,i-n),tmp=0;else tmp=i;
            c[tmp]=0;for(int i=0;i<m;i++)a[i][tmp]=0;
            for(int i=0;i<n;i++)if(pf[i]<n-1)c[i]+=cc[pf[i]];
            for(int i=n;i<m+n;i++)
                if(pf[i]<n-1)
                {
                    ans+=b[i-n]*cc[pf[i]];
                    for(int j=0;j<n;j++)c[j]+=cc[pf[i]]*a[i-n][j];
                }
            fg=csolve(ans);return;
        }
        fg=csolve(0);return;
    }
}_;

int n;
double v,x;
double R[N],C[N];

int ok(double maxt)
{
    _.clear();
    _.m=n+4;
    _.n=n;
    forp(i,0,n)
    {
        _.a[i][i]=-1.0;
        _.b[i]=maxt;
    }
    forp(i,0,n)
    {
        _.a[n][i]=R[i];
        _.a[n+1][i]=-R[i];
        _.a[n+2][i]=R[i]*C[i];
        _.a[n+3][i]=-R[i]*C[i];
    }
    _.b[n]=-v;_.b[n+1]=v;
    _.b[n+2]=-v*x;_.b[n+3]=v*x;
    _.c[0]=1.0;
    int fg;
    fg=_.csolve(0);
    return fg==SOLVED;

}
double _c[N];
int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int T;
    scf("%d",&T);
    forp(tcnt,0,T)
    {
        scf("%d%lf%lf",&n,&v,&x);
        forp(i,0,n)
        {
            scf("%lf%lf",R+i,C+i);
            _c[i]=C[i];
        }
        sort(_c,_c+n);
        ptf("Case #%d: ",tcnt+1);
//        if(x<_c[0]||x>_c[n-1])
//        {
//            puts("IMPOSSIBLE");
//            continue;
//        }
        double l=0,r=1e10,mid;
        forp(ttt,0,200)
        {
            mid=(l+r)/2;
            if(ok(mid))r=mid;else l=mid;
        }
        if(mid>1e9)
            puts("IMPOSSIBLE");
        else
            ptf("%.10f\n",mid);
    }
    return 0;
}
