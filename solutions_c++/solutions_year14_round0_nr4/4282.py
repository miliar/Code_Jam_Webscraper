#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

double a[10000],b[10000];

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("1.out","w",stdout);
    int n,i,j,k,t,T,ans1,ans2,p1,p2;
    scanf("%d",&T);
    for (t=1;t<=T;t++)
    {
        scanf("%d",&n);
        for (i=1;i<=n;i++)
            scanf("%lf",&a[i]);
        for (i=1;i<=n;i++)
            scanf("%lf",&b[i]);
        sort(a+1,a+1+n);
        sort(b+1,b+1+n);

        ans1=0;
        p1 = p2 = 1;
        while (p1<=n && p2<=n)
        {
            if (a[p1]>b[p2])
            {
                ans1++;
                p1++;
                p2++;
            }
            else p1++;
        }


        ans2=0;
        p1 = p2 = 1;
        while (p1<=n && p2<=n)
        {
            if (a[p1]<b[p2])
            {
                ans2++;
                p1++;
                p2++;
            }
            else p2++;
        }
        ans2 = n-ans2;
        printf("Case #%d: %d %d\n",t,ans1,ans2);

    }
    return 0;
}
