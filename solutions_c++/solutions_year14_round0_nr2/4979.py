#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<queue>
#include<algorithm>
#include<vector>
#include<map>
//#include<set>
#include<stdlib.h>
#include<ctype.h>
#include<utility>
#include<cmath>
using namespace std;
//#define REP(k,x,y) for(k=x;k<y;k++)
#pragma comment(linker, "/STACK:1024000000,1024000000")
#define eps 1e-9
#define ll long long
#define i64 __int64
#define INF 2000000000
#define pb push_back
#define sz(b) (int)b.size()
#define lson k<<1
#define rson k<<1|1
#define MOD 10007
#define CLR(t,x) memset(t,x,sizeof(t));
#define N 500005
double C,F,X;
inline int sgn(double x)
{
    return (x>eps)-(x<-eps);
}
inline double cal(int n)
{
    double dif=2,tim=0;
    for(int i=0;i<n;i++)
    {
        tim+=C/dif;
        dif+=F;
    }
    return tim+X/dif;
}
int main()
{
    //freopen("E:\\B-small-attempt2.in","r",stdin);
    //freopen("E:\\B-small-attempt2.out","w",stdout);
    int cas,tt=1;
    scanf("%d",&cas);
    while(cas--)
    {
        double ans=INF*1.0;
        scanf("%lf%lf%lf",&C,&F,&X);
        for(int i=0;;i++)
        {
            if(sgn(cal(i)-ans)<0) ans=cal(i);
            else if(sgn(cal(i)-ans)>0) break;
        }
        printf("Case #%d: %.7f\n",tt++,ans);
    }
    return 0;
}
