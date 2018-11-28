#include <bits/stdc++.h>
using namespace std;

int main()
{
    int i, t, n, j, ans1, ans2, max;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        max = 0;
        ans1 = 0;
        ans2 = 0;
        scanf("%d",&n);
        int a[n];
        for(j=0;j<n;j++)
            scanf("%d",&a[j]);
        for(j=1;j<n;j++)
        {
            if(a[j]<a[j-1])
                ans1+=(a[j-1]-a[j]);
            if(a[j-1]-a[j]>max)
                max = a[j-1]-a[j];
        }
        for(j=0;j<n-1;j++)
        {
            if(a[j]>max)
                ans2+=max;
            else
                ans2+=a[j];
        }
        printf("Case #%d: %d %d\n", i, ans1, ans2);

    }
    return 0;
}

