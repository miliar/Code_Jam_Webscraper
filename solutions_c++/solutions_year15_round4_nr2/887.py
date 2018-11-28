#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <bitset>
#include <stack>
#include <string>
#include <map>
#include <assert.h>
#include <time.h>


#define abs(x) ((x)>=0?(x):-(x))
#define i64 long long
#define u32 unsigned int
#define u64 unsigned long long
#define clr(x,y) memset(x,y,sizeof(x))
#define pb(x) push_back(x)
#define SZ(x) x.size()
#define PI acos(-1.0)
#define sqr(x) ((x)*(x))
#define MP(x,y) make_pair(x,y)
#define EPS 1e-8



#define pii pair<int,int>
#define FFF freopen("test","r",stdin)
#define all(a) a.begin(),a.end()

using namespace std;


void output(i64 x)
{
    if(x<0) putchar('-'),x=-x;
    if(x==0)
    {
        putchar('0');
        return;
    }
    int a[20],num=0;
    while(x) a[++num]=x%10,x/=10;
    while(num>0) putchar('0'+a[num--]);
}

inline i64 myInt()
{
    char c=getchar();
    while(!isdigit(c)&&c!='-') c=getchar();
    int flag=1;
    if(c=='-') flag=-1,c=getchar();
    i64 x=0;
    while(isdigit(c))
    {
        x=(x*10)+(c-'0');
        c=getchar();
    }
    if(-1==flag) return -x;
    return x;
}

const int INF=1e9;
const int mod=100007;
const int N=111;

double V,X;
double a[N],b[N];
int n;

double cal(int p)
{
    if(fabs(b[p]-X)<1e-6) return V/a[p];
    return 1e15;
}

double cal(int p,int q)
{
    if(fabs(b[p]-b[q])<1e-6)
    {
        if(fabs(b[p]-X)<1e-6) return V/(a[p]+a[q]);
        return 1e15;
    }
    double t2=(b[p]*V-V*X)/(a[q]*(b[p]-b[q]));
    double t1=(V-a[q]*t2)/a[p];

    if(t1<-1e-9||t2<-1e-9) return 1e15;
    return max(t1,t2);

}

double cal()
{
    n=myInt();
    scanf("%lf%lf",&V,&X);
    for(int i=1;i<=n;i++) scanf("%lf%lf",&a[i],&b[i]);
    double ans=1e15;
    for(int i=1;i<=n;i++)
    {
        double tmp=cal(i);
        ans=min(ans,tmp);
        for(int j=i+1;j<=n;j++)
        {
            double tmp=cal(i,j);
            ans=min(ans,tmp);
        }
    }
    return ans;
}

int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("out","w",stdout);

  //  FFF;

    int T=myInt();
    int num=0;
    while(T--)
    {
        printf("Case #%d: ",++num);
        double ans=cal();
        if(ans>1e10) puts("IMPOSSIBLE");
        else printf("%.9lf\n",ans);
    }
}

