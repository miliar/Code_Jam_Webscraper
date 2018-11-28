#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<string.h>
#include<math.h>
#include<limits.h>
#include<time.h>
#include<stdlib.h>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#define LL long long
using namespace std;
int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    int T, cse = 1;
    scanf("%d", &T);
    while(T--)
    {
        int d, p[1005];
        int maxx = 0;
        scanf("%d", &d);
        for(int i = 1; i <= d; i++)
        {
            scanf("%d", &p[i]);
            maxx = max(maxx, p[i]);
        }
        sort(p + 1, p + d + 1);
        int ans = maxx;
        for(int i = 1; i < maxx; i++)
        {
            int res = 0;
            int pos = upper_bound(p + 1, p + d + 1, i) - p;
            for(int j = pos; j <= d; j++)
            {
                res += (p[j] + i - 1) / i - 1;
            }
            ans = min(ans, res + i);
        }
        printf("Case #%d: %d\n", cse++, ans);
    }
    return 0;
}
