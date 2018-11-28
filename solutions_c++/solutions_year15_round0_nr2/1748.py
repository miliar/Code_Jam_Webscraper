#include <iostream>
#include <stdio.h>

using namespace std;
const int N=1010;
int f[N];

int main()
{
    int T,Case=0,ans,n,MAX;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        MAX=0;
        for (int i=1;i<=n;i++)
        {
            scanf("%d",&f[i]);
            MAX=max(MAX,f[i]);
        }

        ans=N;
        for (int i=1;i<=MAX;i++)
        {
            int temp=i;
            for (int j=1;j<=n;j++)
            if (f[j]>i)
            {
                if (f[j]%i==0) temp=temp+f[j]/i-1; else temp=temp+f[j]/i;
            }
            ans=min(ans,temp);
        }
        printf("Case #%d: %d\n",++Case,ans);
    }
    return 0;
}
