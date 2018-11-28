#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include<iomanip>
#define Mod (1000000007LL)
#define eps (1e-12)
#define Pi (acos(-1.0))
using namespace std;
int n;
double A[1100],B[1100];
bool fb[1100];
int ans1,ans2;
int a[1100];
int y;
void work(int id)
{
    int sx=0;
    for(int i=1;i<=n;i++)
    {
        if(fb[i])
        {
            if(A[id]<B[i])
            {
                fb[i]=false;
                ans1++;
                return ;
            }
            else if(!sx) sx=i;
        }
    }
    fb[sx]=false;
}
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    int cas=0;
    while(T--)
    {
        memset(fb,true,sizeof(fb));
        memset(a,0,sizeof(a));
        ans1=ans2=0;
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
        scanf("%lf",&A[i]);
        for(int i=1;i<=n;i++)
        scanf("%lf",&B[i]);
        sort(A+1,A+n+1);
        sort(B+1,B+n+1);
        for(int i=n;i>0;i--)
        {
            work(i);
        }
        ans1=n-ans1;
        for(int i=1;i<=n;i++)
        {
            a[i]=a[i-1];
            while(a[i]<n&&A[i]>B[a[i]+1]) a[i]++;
        }
        //printf("a[1]=%d %d\n",a[0],a[1]);
        for(int i=1;i<=n;i++)
        {
            a[i]=min(a[i],a[i-1]+1);
            ans2=max(ans2,a[i]);
        }
        printf("Case #%d: %d %d\n",++cas,ans2,ans1);
    }

    return 0;
}
