#include <bits/stdc++.h>
#define MA(a,b) ((a)>(b)?(a):(b))
#define MI(a,b) ((a)<(b)?(a):(b))
#define AB(a) (-(a)<(a)?(a):-(a))
#define C first
#define R second
#define mp make_pair
#define pb push_back
#define pob pop_back
#define ep 0.00000005
#define ep22 0.000000005
using namespace std;
const int N=202;
int n;
double  v,t;
pair <double  ,double > a[N];

void input(){
    cin>>n;
    double m;
    cin>>m;
    v=m;
    cin>>m;
    t=m;

    for (int i=1;i<=n;i++)
    {
        cin>>m;
        a[i].R=m;

        cin>>m;
        a[i].C=m;

    }
}

bool ch(double d){
    long long vn=0,Q=0;
    for (int i=1;i<=n;i++) vn+=a[i].R;
    for (int i=1;i<=n;i++) Q+=a[i].R*a[i].C;
    if (vn*d<v+ep) return 0;
    int l=1;
    int r=n;
    bool fin=0;
    while (AB(Q-t*vn)>0ll && fin==0){

        if (Q>t*vn){
            if (r<l || a[r].C<=t) return 0;
            long long  x=(Q-vn*t);
            long long  xx=(a[r].C-t);

            if(x>a[r].R*xx) x=a[r].R,xx=1;
            else fin=1;

            if (fin){
                 if (d*(vn*xx-x)<1.0*v*xx+ep) return 0;
                return 1;
            }

            Q-=x*a[r].C;
            vn-=x;

            r--;
        } else {
            if (r<l || a[l].C<=t) return 0;
            long long  x=(Q-vn*t);
            long long  xx=(a[l].C-t);

            if(x>a[l].R*xx) x=a[l].R,xx=1;

            else fin=1;

            if (fin){
                if (d*(vn*xx-x)<1.0*v*xx+ep) return 0;
                return 1;
            }

            Q-=x*a[l].C;
            vn-=x;
            l++;
        }
        if (d*vn<v+ep) return 0;
    }
    return 1;
}

double sol(){
    sort(a+1,a+n+1);
    if (n==1) {
        if (a[1].C!=t) return -10;
        return 1.0*v/a[1].R;
    }
    if (a[1].C==t && a[2].C==t)      return 1.0*v/(a[1].R+a[2].R);
    if (a[1].C==t)      return 1.0*v/(a[1].R);
    if (a[2].C==t)      return 1.0*v/(a[2].R);
    if (a[1].C>t || a[2].C<t) return -10;
     /*  cout<<t<<endl;
       cout<<a[1].C<<" "<<a[1].R<<endl;
       cout<<a[2].C<<" "<<a[2].R<<endl;
       */ double  A=a[2].C-a[1].C;
        double B=max(1.0*(a[2].C-t)/a[1].R,1.0*(t-a[1].C)/a[2].R);
       // cout<<A<< " "<<B<<" "<<v<<endl;
    return B/A*v;
    /*double l=0,r=1000000000.0;
    if (!ch(r)) return -10;
    while (r-l>ep) {
        double mid=(l+r)/2;
        if (ch(mid)) r=mid; else l=mid;
    }*/
}

int main() {
    freopen("BB.in","r",stdin);
    freopen("ans.txt","w",stdout);
    int testn=1;
    cin>>testn;
    for (int test=1;test<=testn;test++){
        input();
        double ans=sol();
        if (ans>-0.1)    printf("Case #%d: %.9lf\n",test,ans);
                    else printf("Case #%d: IMPOSSIBLE\n",test);
    }

    return 0;
}
