#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;
    int n;
    int plate[1005];
    scanf("%d", &t);
    int movecnt;
    int eatcnt;
    int ans;
    for (int cases = 1; cases <= t; ++cases)
    {
        movecnt = 0;
        eatcnt = 0;
        scanf("%d", &n);
        for (int i=0;i<n;++i)
            scanf("%d", &plate[i]);

        sort(plate, plate+n);

        ans = plate[n-1];

        for (int eatcnt = 1; eatcnt<plate[n-1]; ++eatcnt)
        {
            movecnt = 0;
            for (int i=n-1;i>=0;--i)
            {
                if (plate[i]>eatcnt)
                {
                    movecnt += ceil(plate[i]*1.0/eatcnt) - 1;
                }
                else break;
            }
            if (movecnt + eatcnt < ans)
            {
                ans = movecnt + eatcnt;
            }
        }
        printf("Case #%d: %d\n",cases, ans);
    }
    return 0;
}
