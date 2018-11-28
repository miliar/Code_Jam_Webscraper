#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>

#define MAXN
#define LSON(x) x << 1
#define RSON(x) x << 1 | 1
using namespace std;

typedef long long LL;

int num[1010];
int solve(int x, int n)
{
        int now = num[0] + x, ret = 1;
        for(int i = 1; i <= n; i ++)
        {
            if(now >= i)
                now += num[i];
            else
                ret = 0;
        }
        return ret;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t, n;
    scanf("%d",&t);

    for(int curCase = 1; curCase <= t; curCase ++)
    {
        scanf("%d", &n);
        for(int i = 0; i <= n; i ++)
            scanf("%1d", &num[i]);
        for(int i = 0; i <= n; i ++) {
            if(solve(i, n))
            {
                printf("Case #%d: %d\n", curCase, i);
                break;
            }
        }
    }
    return 0;
}
