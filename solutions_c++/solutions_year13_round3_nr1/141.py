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

template<class T> void checkMax(T &a, T b)
{
    a = max(a, b);
}
template<class T> void checkMin(T &a, T b)
{
    a = min(a, b);
}

const int N = 1000005;
char str[N];
int idx[26], sum[N], x[N];
void init()
{
    memset(idx, 0, sizeof(idx));
    idx['a' - 'a'] = 1;
    idx['e' - 'a'] = 1;
    idx['i' - 'a'] = 1;
    idx['o' - 'a'] = 1;
    idx['u' - 'a'] = 1;
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t, cas = 1, i, j, m;
    init();
    scanf("%d", &t);
    while(t--)
    {
        scanf("%s%d", str, &m);
        int n = strlen(str);
        for(i = n - 1; i >= 0; i--)
        {
            sum[i] = 1 - idx[str[i] - 'a'];
            if(sum[i] == 1 && i + 1 < n)
                sum[i] += sum[i + 1];
        }
        for(i = n - 1; i >= 0; i--)
        {
            if(sum[i] >= m)
                x[i] = i;
            else
                x[i] = INF;
            if(i + 1 < n)   x[i] = min(x[i], x[i + 1]);
        }
        LL ans = 0;
        for(i = 0; i < n; i++)
        {
          //  printf("%d %d\n", i, x[i]);
            ans += max(0, n - (x[i] + m) + 1);
        }
        printf("Case #%d: %I64d\n", cas++, ans);
    }
    return 0;
}
