#include <iostream>
#include <stdio.h>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;
const int N=1010;
double a[N],b[N];
int c[N];

int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int o,n,cas=0;
    scanf("%d",&o);
    while (o--)
    {
        scanf("%d",&n);
        for (int i=1; i<=n; i++) scanf("%lf",&a[i]);
        for (int i=1; i<=n; i++) scanf("%lf",&b[i]);
        memset(c,0,sizeof(c));
        sort(a+1,a+n+1);
        sort(b+1,b+n+1);
        int ans1=0,ans2=0;
        for (int i=n; i>=1; i--)
        {
            int j;
            for (j=n; j>=1; j--) if (c[j]==0 && a[i]>b[j]) break;
            if (j==0) break;
            c[j]=1; ans1++;
        }
        memset(c,0,sizeof(c));
        for (int i=1; i<=n; i++)
        {
            int j;
            for (j=1; j<=n; j++) if (c[j]==0 && b[j]>a[i]) break;
            if (j<=n) c[j]=1;
            else
            {
                ans2++;
                for (j=1; j<=n; j++) if (c[j]==0) break;
                c[j]=1;
            }
        }
        printf("Case #%d: ",++cas);
        printf("%d %d\n",ans1,ans2);
    }
    return 0;
}