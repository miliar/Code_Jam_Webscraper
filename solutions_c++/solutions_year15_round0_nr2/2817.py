#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#define MAXN 1000000

using namespace std;

int a[1001];

int main()
{
    int t,i,j,r,n,x,sum=0;
    int minn;
    freopen("B-large.in","r",stdin);
    freopen("B-large-out.txt","w",stdout);
    scanf("%d",&t);
    for(r=1;r<=t;r++)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
        }
        minn=1000;
        for(i=1;i<=1000;i++)
        {
            sum=0;
            for(j=0;j<n;j++)
            {
                sum+=(a[j]-1)/i;
            }
            minn=min(minn,sum+i);
        }
        printf("Case #%d: %d\n",r,minn);
    }
    return 0;
}
