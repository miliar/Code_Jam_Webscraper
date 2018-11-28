#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;
int a[109][109];
int L[109], R[109];
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, cot = 1;
    scanf("%d", &T);
    while(T --)
    {
        int n, m;
        scanf("%d%d", &n, &m);
        for(int i = 1; i <= n; ++ i)
        {
            for(int j = 1; j <= m; ++ j) scanf("%d", &a[i][j]);
        }
        for(int i = 1; i <= n; ++ i)
        {
            L[i] = -1;
            for(int j = 1; j <= m; ++ j)
            {
                L[i] = max(L[i], a[i][j]);
            }
        }
        for(int j = 1; j <= m; ++ j)
        {
            R[j] = -1;
            for(int i = 1; i <= n; ++ i)
            {
                R[j] = max(R[j], a[i][j]);
            }
        }
        int ans = 1;
        for(int i = 1; i <= n; ++ i)
        {
            for(int j = 1; j <= m; ++ j)
            {
                if(L[i] > a[i][j] && R[j] > a[i][j])
                {
                    ans = 0;
                }
            }
        }
        printf("Case #%d: ", cot ++);
        if(ans) puts("YES");
        else puts("NO");
    }
    return 0;
}
