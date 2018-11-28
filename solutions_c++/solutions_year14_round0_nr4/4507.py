#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <math.h>
using namespace std;
const int maxn = 1005;
const double eps = 1e-8;
double a[maxn],b[maxn];
int v[maxn];
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int i,j,k,m,n;
    int ca;
    scanf("%d",&ca);
    int t=1;
    while(scanf("%d",&n)!=EOF)
    {
        for(i=0;i<n;i++)
            scanf("%lf",&a[i]);
        for(i=0;i<n;i++)
            scanf("%lf",&b[i]);
        printf("Case #%d: ",t++);
        sort(a,a+n);
        sort(b,b+n);
        int ans1=0,ans2=0;
        memset(v,0,sizeof(v));
        int l=0,r=n-1;
        for(i=0;i<n;i++)
        {
            int f=0;
           for(j=l;j<=r;j++)
           {
               if(!v[j]&&a[i]-b[j]>eps)
               {
                   v[l++]=1;
                   ans1++;
                   f=1;
                   break;
               }
           }
           if(f)
            continue;
            v[r--]=1;

        }
        memset(v,0,sizeof(v));
        for(i=0;i<n;i++)
        {
            int f=0;
            for(j=0;j<n;j++)
            {
                if(v[j]==0&&b[j]-a[i]>eps)
                {
                    f=1;
                    v[j]=1;
                    break;
                }
            }
            if(f)
                continue;
            for(j=0;j<n;j++)
                if(!v[j])
                    {
                        v[j]=1;
                        ans2++;
                    }
        }
        printf("%d %d\n",ans1,ans2);
    }







    return 0;
}
