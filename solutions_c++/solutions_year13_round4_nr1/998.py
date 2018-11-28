#pragma comment(linker, "/STACK:102400000,102400000")
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

#define INF 0x3f3f3f3f
#define LL long long
#define eps 1e-8
#define lson (pos << 1)
#define rson (pos << 1 | 1)
#define A first
#define B second

template<class T> void checkMax(T &a, T b)
{
    a = max(a, b);
}
template<class T> void checkMin(T &a, T b)
{
    a = min(a, b);
}
const LL MOD = 1000002013;
const int N = 1005;
int n, m, o[N], e[N], p[N];
int x[2 * N], np, h[2 * N];
int bifind(int num)
{
    int l = 1, r = np, mid;
    while(l <= r)
    {
        mid = (l + r) / 2;
        if(x[mid] == num)   return mid;
        else if(x[mid] > num)   r = mid - 1;
        else if(x[mid] < num)   l = mid + 1;
    }
    return -1;
}
int main()
{
    int t, cas = 1, i, j;
    LL org, cur;
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A.out", "w", stdout);
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d", &n, &m);
        org = 0;
        for(i = 1; i <= m; i++)
        {
            scanf("%d%d%d", &o[i], &e[i], &p[i]);
            LL rm = e[i] - o[i];
            LL sg = ((2LL * n - rm + 1) * rm / 2) % MOD;
            org += sg * p[i] % MOD;
            org %= MOD;
            x[2 * i - 1] = o[i];
            x[2 * i] = e[i];
        }
        x[2 * m + 1] = n;
        sort(x + 1, x + 1 + 2 * m + 1);
        for(i = 1, np = 1; i <= 2 * m + 1; i++)
            if(x[i] != x[np])
                x[++np] = x[i];
        memset(h, 0, sizeof(h));
        for(i = 1; i <= m; i++)
        {
            o[i] = bifind(o[i]);
            e[i] = bifind(e[i]);
            //cout << o[i] << " " << e[i] << endl;
            for(j = o[i]; j <= e[i] - 1; j++)
                h[j] += p[i];
        }
        h[0] = h[np] = 0;
        cur = 0;
        while(1)
        {
            int maxh = 0, st = -1, ed;
            for(i = 1; i < np; i++)
            {
                if(h[i] > maxh)
                {
                    maxh = h[i];
                    st = i;
                }
            }
            if(maxh == 0)   break;
            int low = h[st - 1];
            for(i = st + 1; i <= np; i++)
                if(h[i] < maxh)
                {
                    low = max(low, h[i]);
                    ed = i;
                    break;
                }
            LL rm = x[ed] - x[st];
            LL sg = ((2LL * n - rm + 1) * rm / 2) % MOD;
            cur += sg * (maxh - low) % MOD;
            cur %= MOD;
            for(i = st; i < ed; i++)
                h[i] = low;
        }
        //cout << org << " " << cur << endl;
        LL ans = ((org - cur) % MOD + MOD) % MOD;
        printf("Case #%d: %I64d\n", cas++, ans);
    }
    return 0;
}
/*
3
6 2
1 3 1
3 6 1
6 2
1 3 2
4 6 1
10 2
1 7 2
6 9 1
*/
