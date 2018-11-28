#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int main()
{
    int t,k,n,m,i,j;
    double a[1005],b[1005];
    int color[1005];
    scanf("%d",&t);
    for(k=1; k<=t; k++)
    {
        scanf("%d",&n);
        for(i=0; i<n; i++)
            scanf("%lf",&a[i]);
        for(i=0; i<n; i++)
            scanf("%lf",&b[i]);
        sort(a,a+n);
        sort(b,b+n);
        int ans2=0;
        memset(color,0,sizeof(color));
        for(i=0; i<n; i++)
        {
            for(j=0;j<n;j++)
            {
                if(b[i]>a[j]&&!color[j])
                {
                    ans2++;
                    color[j]=1;
                    break;
                }
            }
        }
        printf("Case #%d: ",k);
        ans2=n-ans2;
        if(ans2==n)
        {
            printf("%d %d\n",n,n);
            continue;
        }
        int ans1=0;
        memset(color,0,sizeof(color));
        for(i=0; i<n; i++)
        {
            for(j=0;j<n;j++)
            {
                if(a[i]>b[j]&&!color[j])
                {
                    ans1++;
                    color[j]=1;
                    break;
                }
            }
        }
        printf("%d %d\n",ans1,ans2);
    }
    return 0;
}
