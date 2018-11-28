#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
using namespace std;
#define Rep(i,n) for (int i=0;i<(n);i++)
#define For(i,l,r) for (int i=(l);i<=(r);i++)
#define PB push_back
#define MP make_pair
int T,n,ans,ma,l,r,mid;
int a[2005];



bool ok(int mv,int tm)
{
    int tp=0;
    Rep(i,n)
    {
        tp+=(a[i]-1)/tm;
    }
    return tp<=mv;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("2.out","w",stdout);

    scanf("%d",&T);
    For(C,1,T)
    {
        scanf("%d",&n);
        ma=0;
        Rep(i,n)
        {
            scanf("%d",&a[i]);
            ma=max(ma,a[i]);
        }
        ans=ma;
        For(mv,1,ma)
        {
            l=1; r=ma;
            while (l<r)
            {
                mid=l+r>>1;
                if (ok(mv,mid)) r=mid; else l=mid+1;
            }
            ans=min(ans,l+mv);
        }
        printf("Case #%d: %d\n",C,ans);

    }


    return 0;
}
