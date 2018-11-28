#include <stdio.h>

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int t, k;
    int m, n;
    int height[101][101];
    scanf("%d", &t);

    for(k = 1 ; k <= t ; k++)
    {
        scanf("%d%d", &n, &m);
        int i, j;
        for(i = 0 ; i < n ; i++)
            for(j = 0 ; j < m ; j++)
                scanf("%d", &height[i][j]);

        bool ans = true;
        for(i = 0 ; i < n ; i++)
        {
            for(j = 0 ; j < m ; j++)
            {
                // x_dir
                bool x_dir = true;

                for(int x = 0 ; x < n ; x++)
                    if(height[x][j] > height[i][j])
                    {
                        x_dir = false;
                        break;
                    }
                if(x_dir)
                    continue;

                bool y_dir = true;
                for(int y = 0 ; y < m ; y++)
                    if(height[i][y] > height[i][j])
                    {
                        y_dir = false;
                        break;
                    }

                if(y_dir == false)
                {
                    ans = false;
                    break;
                }
            }
        }

        if(ans)
            printf("Case #%d: YES\n", k);
        else
            printf("Case #%d: NO\n", k);
    }
    return 0;
}
