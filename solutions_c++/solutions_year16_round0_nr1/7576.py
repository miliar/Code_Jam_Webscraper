#include <cstdio>
#include <queue>
#include <string>
#include <map>
#include <cstring>
#include <algorithm>
#include <iostream>
#define MAXINT 2147483647 
using namespace std;
int n, casenum;
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &casenum);
    for (int icn = 0; icn != casenum; ++icn)
    {
        scanf("%d", &n);
        if (n == 0)
        {
            printf("Case #%d: INSOMNIA\n", icn + 1);
            continue;
        }
        int cnt = 0;
        int t = 1;
        while (cnt != ((1 << 10) - 1)) {
            int cur = t * n;
            while (cur) {
                int mk = 1 << (cur % 10);
                cnt = mk | cnt;
                cur = cur / 10;
            }
            t++;
        }
        printf("Case #%d: %d\n", icn + 1, (t - 1) * n);
    }
    return 0;
}