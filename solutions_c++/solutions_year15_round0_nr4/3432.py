#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("in4.txt", "r", stdin);
    freopen("out4.txt", "w", stdout);
    int Tcase;
    scanf("%d", &Tcase);

    for(int tc = 1; tc <= Tcase; tc++)
    {
        int x,r,c;
        scanf("%d %d %d", &x, &r, &c);

        int grid = r*c;
        if(x > grid || (grid) % x != 0)
        {
            printf("Case #%d: RICHARD\n", tc);
            continue;
        }
        else if(x == 3)
        {
            if((grid) == 3)
            {
                printf("Case #%d: RICHARD\n", tc);
                continue;
            }
            else if(grid % 3 == 0)
            {
                printf("Case #%d: GABRIEL\n", tc);
                continue;
            }
        }
        else if(x == 4)
        {
            if(grid == 4 || grid == 8)
            {
                printf("Case #%d: RICHARD\n", tc);
                continue;
            }
            else if(grid == 12 || grid == 16)
            {
                printf("Case #%d: GABRIEL\n", tc);
                continue;
            }
        }
        else if(x < 3 && grid % x == 0)
        {
                printf("Case #%d: GABRIEL\n", tc);
                continue;
        }
    }
    return 0;
}
