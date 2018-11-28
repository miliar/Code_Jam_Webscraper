#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <stack>
#include <vector>
#include <queue>
#include <map>
#include <climits>
#include <cassert>
#define LL long long

using namespace std;
const int maxn = 1e3 + 10;
const int inf = 0x3f3f3f3f;
const double eps = 1e-8;
const double pi = acos(-1.0);
const double ee = exp(1.0);

char str[maxn];

int main()
{
    #ifdef LOCAL
    freopen("A-large.in", "r", stdin);
    freopen("o.out", "w", stdout);
    #endif // LOCAL
    int ncase;
    scanf("%d",&ncase);
    int ca = 1;
    while (ncase--)
    {
        int m;
        scanf("%d%s", &m, str);
        int man = str[0] - '0';
        int ans = 0;
        for(int i = 1; i <= m; i++)
        {
            int t = str[i] - '0';
            if (man < i)
            {
                ans += i - man;
                man += t + (i - man);
            }
            else
            {
                man += t;
            }
        }
        printf("Case #%d: %d\n", ca++, ans);
    }
    return 0;
}
