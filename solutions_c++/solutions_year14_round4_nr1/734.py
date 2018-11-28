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
#define Max 10005

using namespace std;

int p,a[Max],n;

int main()
{
    int i,j,k,T,cas,ret=0,lo,hi,mid,x,y,s,d;

    freopen("A-large(5).in","r",stdin);
    freopen("a-large.txt","w",stdout);

    scanf("%d",&T);

    for(cas=1;cas<=T;cas++)
    {
        scanf("%d %d",&n,&p);

        for(i=1;i<=n;i++) scanf("%d",&a[i]);

        sort(a+1,a+n+1);

        lo=(n+1)/2;

        hi=n;

        while(lo!=hi)
        {
            mid=(lo+hi)/2;

            s=2*mid-n;
            d=mid-s;

            for(i=1;i<=d;i++)
            {
                if(a[i]+a[n-s-i+1]>p) break;
            }

            if(i<=d) lo=mid+1;

            else hi=mid;

        }

        printf("Case #%d: %d\n",cas,lo);
    }

    return 0;
}
