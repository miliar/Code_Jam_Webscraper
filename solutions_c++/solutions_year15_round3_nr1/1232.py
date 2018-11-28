#include <cmath>
#include <cstdio>
#include <vector>
#include <stack>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("o/p.txt", "w", stdout);
    int t, i;
    scanf("%d",&t);
    for (i = 1; i <= t; i++)
    {
        int R, C, W;
        scanf("%d",&R);
        scanf("%d",&C);
        scanf("%d",&W);
        int hits1, hits2, totalHits;
//        if (C == 1)
//        {
//            printf(Case #%d: %d\n",i, 1);
//        }
//        else if (C == 2)
//        {
//            if (W == 2)
//            {
//                printf(Case #%d: %d\n",i, 2);
//            }
//            else
//            {
//                printf(Case #%d: %d\n",i, 2);
//            }
//        }
//        else
//        {
        hits1 = (C/W) * R;
        if (C % W == 0)
        {
            hits2 = W-1;
        }
        else
        {
            hits2 = W;
        }
        totalHits = hits1 + hits2;
        printf("Case #%d: %d\n",i, totalHits);
//        }
    }
    return 0;
}
