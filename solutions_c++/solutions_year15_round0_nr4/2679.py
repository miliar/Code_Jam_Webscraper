#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    int X,R,C;
    for(int t = 1; t <= T; ++t)
    {
        scanf("%d %d %d", &X, &R, &C);
        printf("Case #%d: ", t);
        if(X == 1)
        {
            printf("GABRIEL\n");
            continue;
        }
        if(X > R * C || R * C % X != 0)
        {
            printf("RICHARD\n");
            continue;
        }

        if(X == 2)
        {
            printf("GABRIEL\n");
            continue;
        }
        if(X == 3)
        {
            if(R == 1 && C == 3 || R == 3 && C == 1)
                printf("RICHARD\n");
            else
                printf("GABRIEL\n");
            continue;
        }
        if(X == 4)
        {
            if(R == 3 && C == 4 || R == 4 && C == 3 || R == 4 && C == 4)
                printf("GABRIEL\n");
            else
                printf("RICHARD\n");
            continue;
        }
    }
}
