#include <cstdio>
#include <algorithm>

double wa[2000], wb[2000];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int CAS1;
    scanf("%d", &CAS1);
    for (int CAS=1; CAS<=CAS1; CAS++)
    {
        int n;
        scanf("%d", &n);
        for (int i=1; i<=n; i++)
            scanf("%lf", &wa[i]);
        for (int i=1; i<=n; i++)
            scanf("%lf", &wb[i]);
        std::sort(wa+1, wa+1+n);
        std::sort(wb+1, wb+1+n);
        int ans = 0;
        for (int i=n, t=n; i; i--)
        {
            if (wb[t]>wa[i])
                t--;
            else
                ans++;
        }
        int ans2 = 0;
        for (int i=1, s=1, t=n; i<=n; i++)
            if (wa[i] <= wb[s])
                t--;
            else
            {
                s++;
                ans2++;
            }
        
        printf("Case #%d: %d %d\n", CAS, ans2, ans);
            
    }
    fclose(stdin);
    fclose(stdout);
    return 0;

}
