#include<stdio.h>
#include<string.h>
#include<math.h>
#include<string>
#include<algorithm>
#include<iostream>
#include<queue>
#include<stack>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<cmath>
#include<deque>
#include<time.h>
#pragma comment(linker, "/STACK:1024000000,1024000000")
using namespace std;
#define cl(x,v); memset(x,v,sizeof(x));
#define llINF 1ll<<60
#define INF 1<<29
#define EPS 1e-8
#define MID int mid=(l+r)>>1; int ls=o<<1; int rs=o<<1|1;
#define pii pair<int,int>
#define pli pair<long long,int>
#define pll pair<long long,long long>
#define pss pair<short,short>
#define F first
#define S second
#define PB push_back
#define BR puts("");
#define SCn scanf("%d",&n)
#define SCnm scanf("%d%d",&n,&m)
#define rep(i,s,n) for(int i=(s);i<=(n);++i)
#define rrep(i,s,n) for(int i=(s);i>=(n);--i)
#define TSC int T; scanf("%d",&T);
#define PI acos(-1.0)
#define test printf("test\n");
#define db double
typedef unsigned long long ull;
typedef long long ll;
int n;
int a[1005];
int Min,Max;
int fun(int x)
{
    int ret=0;
    for(int i=0;i<n;i++){
        ret+=(a[i]-1)/x;
    }
    return ret+x;
}
int solve(int l,int r)
{
        if(l==r)return fun(l);
        int mid=(l+r)>>1;
        int midmid=(mid+r)>>1;
        int y1=fun(mid);
        int y2=fun(midmid);
     //   printf("%d %d\n",l,r);
    //    printf("%d %d %d %d\n",mid,midmid,y1,y2);
        if(l==r-1)return min(fun(l),fun(r));
        if(y1<y2)
        {
            r=midmid;
            return solve(l,r);
        }
        else if(y1>y2)
        {
            l=mid;
            return solve(l,r);
        }
        else
        {
            return min(solve(l,midmid),solve(mid,r));
        }

    return fun(l);
}
int main()
{
     int T;
    scanf("%d",&T);
    int Case=1;
    while(T--)
    {
        scanf("%d",&n);
        Min=INF;
        Max=-1;
        for(int i=0;i<n;i++){
            scanf("%d",&a[i]);
            Min=min(Min,a[i]);
            Max=max(Max,a[i]);
        }

        printf("Case #%d: %d\n",Case++,min(solve(1,Max),Max));
    }
    return 0;
}

