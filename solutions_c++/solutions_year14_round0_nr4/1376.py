#include <iostream>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <functional>
#include <queue>
#include <vector>
#include <cstdlib>
#include <string>
#include <set>
using namespace std;

double a[1010],b[1010];

int n;

bool check(int s)
{
    for(int i=s;i<=n;i++)
    {
        if(a[i]<b[i-s+1])
            return false;
    }
    return true;
}

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        int ans1,ans2=0,i,j,now=n;
        for(i=1;i<=n;i++)
            scanf("%lf",&a[i]);
        for(i=1;i<=n;i++)
            scanf("%lf",&b[i]);
        sort(a+1,a+1+n);
        sort(b+1,b+1+n);
        for(i=n;i>=1;i--)
        {
            for(j=now;j>=1;j--)
            {
                if(b[j]>a[i])
                {
                    ans2++;
                    now=j-1;
                    break;
                }
            }
        }
        ans2=n-ans2;
        ans1=0;
        for(i=1;i<=n;i++)
        {
            if(check(i))
            {
                ans1=n-i+1;
                break;
            }
        }
        printf("Case #%d: %d %d\n",++cas,ans1,ans2);
    }
    return 0;
}
