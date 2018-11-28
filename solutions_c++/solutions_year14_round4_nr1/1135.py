#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>

using namespace std;
int a[10009];
bool use[10009];
int main()
{
    //freopen("in.txt","r",stdin);
    int t;
    scanf("%d",&t);
    for (int cas = 1; cas <= t; ++cas)
    {
        printf("Case #%d: ",cas);
        int n, x;
        scanf("%d%d",&n,&x);
        for (int i = 1; i <= n; ++i)
        {
            scanf("%d",&a[i]);
        }
        sort(a + 1, a + 1 + n);
        memset(use, 0, sizeof(use));
        int p = 1, ans = 0;
        for (int i = n; i >=1; --i)
        {
            if (!use[i])
            {
                if (a[i] + a[p] <= x)
                {
                    use[p] = true;
                    p++;
                }
                ans++;
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}
