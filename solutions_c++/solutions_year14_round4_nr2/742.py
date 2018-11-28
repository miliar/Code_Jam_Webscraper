#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
#define inf 2000000000
#define ll long long
#define Max 1005

using namespace std;

int n,a[Max],b[Max],l[Max],r[Max],p[Max];
map <int,int> mymap;
int dp[Max][Max];

int f(int x,int a)
{
    if(x==n+1) return 0;

    if(dp[x][a]!=-1) return dp[x][a];

    int i,j,k,b,rr,w,pos;

    b=n-x+a;
    pos=p[x];

    rr=f(x+1,a+1)+l[pos];
    w=f(x+1,a)+r[pos];

    return dp[x][a]=min(rr,w);
}

int main()
{
    int i,j,k,T,cas,ret=0;

    freopen("B-large(3).in","r",stdin);
    freopen("b-large.txt","w",stdout);

    scanf("%d",&T);

    for(cas=1;cas<=T;cas++)
    {
        scanf("%d",&n);

        for(i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
            l[i]=r[i]=0;
        }

        for(i=1;i<=n;i++)
        {
            for(j=1;j<i;j++) if(a[j]>a[i]) l[i]++;
            for(j=i+1;j<=n;j++) if(a[j]>a[i]) r[i]++;
        }


        mymap.clear();

        for(i=1;i<=n;i++)
        {
            b[i]=a[i];
            mymap[a[i]]=i;
        }

        sort(b+1,b+n+1);

        for(i=1;i<=n;i++)
        {
            p[i]=mymap[b[i]];
        }

        memset(dp,-1,sizeof(dp));

        printf("Case #%d: %d\n",cas,f(1,1));
    }

    return 0;
}
