#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int s[2000];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    int cas,n;
    scanf("%d",&cas);
    for (int c=1; c<=cas; c++)
    {
        int cmax=0;
        scanf("%d",&n);
        for (int i=1; i<=n; i++)
            {
                scanf("%d",&s[i]);
                cmax=max(s[i],cmax);
            }
        int ans=1000000;
        for (int i=1;i<=cmax;i++)
        {
            int cnt=i;
            for (int j=1;j<=n;j++)
            if (s[j]>i)
            {
                cnt=cnt+(s[j]+i-1)/i-1;
            }
            ans=min(ans,cnt);
        }
        printf("Case #%d: %d\n", c, ans);
    }
    return 0;
}
