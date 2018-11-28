#include <stdio.h>
#include <string.h>

int n[1005];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    int cases;
    scanf("%d", &cases);
    
    for (int index = 1; index <= cases; index++)
    {
        int N, X;
        scanf("%d %d", &N, &X);
        memset(n, 0, sizeof(n));
        
        for (int i = 1; i <= N; i++)
        {
            int t;
            scanf("%d", &t);
            n[t]++;
        }
        
        int ans = 0;
        int nmin = 1;
        int nmax = X;
        for (;;)
        {
            if (nmin > nmax) break;
            
            if (n[nmax] <= 0)
            {
                nmax--;
            }
            else if (n[nmin] <= 0)
            {
                nmin++;
            }
            else
            {
                if (nmax + nmin <= X)
                {
                    ans++;
                    n[nmax]--;
                    if (n[nmin] > 0)
                    {
                        n[nmin]--;
                    }
                }
                else
                {
                    ans++;
                    n[nmax]--;
                }
            }
        }
        
        printf("Case #%d: %d\n", index, ans);
    }
    
    return 0;
}
