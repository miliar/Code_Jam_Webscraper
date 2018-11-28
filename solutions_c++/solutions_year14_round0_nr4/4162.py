#include <cstdio>
#include <algorithm>
int main()
{
    freopen("Input.txt","r",stdin);
    freopen("Output.txt","w",stdout);
    double a[1200],b[1200];
    int T,n,m;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%lf",&a[i]);
        for(int i=0;i<n;i++)
            scanf("%lf",&b[i]);
        std::sort(a,a+n);
        std::sort(b,b+n);
        int x=0,y=n-1,p=0,q=n-1,ans1=0;
        while(x<=n-1)
        {
            if(a[x]>b[p])
            {
                x++;p++;ans1++;
            }
            else
            {
                x++;
                q--;
            }
        }
        int x1=0,y1=n-1,p1=0,q1=n-1,ans2=0;
        while(p1<=n-1)
        {
            if(b[p1]>a[x1])
            {
                p1++;x1++;ans2++;
            }
            else
            {
                p1++;
            }
        }
        ans2=n-ans2;
        printf("Case #%d: %d %d\n",cas,ans1,ans2);
    }
}
