#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

int a[2005], sum[2005];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, ca=1;
    scanf("%d", &t);
    while(t--)
    {
        int n;
        scanf("%d", &n);
        for(int i=0;i<=n;i++)
        {
            scanf("%1d", &a[i]);
            sum[i]=(i? sum[i-1]+a[i]:a[i]);
        }
        printf("Case #%d: ", ca++);
        int ans=0;
        for(int i=1;i<=n;i++)
            if(a[i])
            {
                if(sum[i-1]+ans<i)
                    ans+=(i-sum[i-1]-ans);
            }
        printf("%d\n", ans);
    }
    return 0;
}
