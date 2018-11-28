#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int f[1010];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int n,ans1,ans2,sum,T,Case=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        for (int i=1;i<=n;i++) scanf("%d",&f[i]);
        ans1=0;
        for (int i=2;i<=n;i++)
            if (f[i]<f[i-1]) ans1=ans1+f[i-1]-f[i];
        ans2=0,sum=0;
        for (int i=2;i<=n;i++)
            if (f[i]<f[i-1]) ans2=max(f[i-1]-f[i],ans2);
        for (int i=1;i<n;i++)
            if (f[i]>=ans2) sum=sum+ans2; else sum=sum+f[i];
        printf("Case #%d: %d %d\n",++Case,ans1,sum);
    }
    return 0;
}
