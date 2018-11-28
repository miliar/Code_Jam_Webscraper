#include <iostream>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
#include <vector>
#include <list>
#include <stack>
#include <bitset>
#include <string>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <ctime>

#define ALL(i,n)    for(i = 0; i < (n); i++)
#define FOR(i,a,b)  for(i = (a); i < (b); i++)
#define SET(p)      memset(p,-1,sizeof(p))
#define CLR(p)      memset(p,0,sizeof(p))
#define S(n)	    scanf("%d",&n)
#define P(n)	    printf("%d\n",n)
#define Sl(n)	    scanf("%lld",&n)
#define Pl(n)	    printf("%lld\n",n)
#define Sf(n)       scanf("%lf",&n)
#define Ss(n)       scanf("%s",n)
#define LL long long
#define ULL unsigned long long
#define pb push_back
using namespace std;

LL calworst(LL i,LL n,LL m)
{
    if(i==1)
        return 1;
    if(n==1)
        return 2;

    return m/2 + calworst( i/2 ,n-1,m/2);
}

LL calbest(LL i,LL n,LL m)
{
    if(i==m)
        return m;
    if(n==1)
        return 1;

    return calbest( i/2 +1 ,n-1,m/2);
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    LL ts=0,t,n,m,p,i,j,k;
    Sl(t);
    while(t--)
    {
        Sl(n);  Sl(p);

        m=((1ll) << n);

        LL left,right,mid,ans1=0,ans2=0,tmp;

        left=1; right=m;

        while(left<=right)
        {
            mid=(left+right)/2;
            tmp=calworst(mid,n,m);

            if(tmp<=p)
            {
                ans1=max(ans1,mid);
                left=mid+1;
            }
            else
                right=mid-1;
        }

        left=1; right=m;
        while(left<=right)
        {
            mid=(left+right)/2;
            tmp=calbest(mid,n,m);

            if(tmp<=p)
            {
                ans2=max(ans1,mid);
                left=mid+1;
            }
            else
                right=mid-1;
        }

        ts++;
        printf("Case #%lld: %lld %lld\n",ts,ans1-1,ans2-1);
    }
    return 0;
}

