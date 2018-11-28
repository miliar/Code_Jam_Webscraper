#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>

#define INF (1<<30)
#define mod 666013

using namespace std;
typedef pair<int, int> pereche;
int T, cs, i, n, c, x, r, f[15];
int bck(int pas, int a[15])
{
    if(pas > r)
        return INF;
    int i, mx = 0;
    for(i = 1; i <= 9; i++)
        if(a[i])
            mx = i;
    if(mx == 1)
        return pas;
    int f[15] = {0};
    for(i = 1; i <= 9; i++)
        f[i] = a[i + 1];
    int c = bck(pas + 1, f);

    for(i = 1; i <= 9; i++)
    {
        f[i] = a[i];
        if(f[i])
            mx = i;
    }
    f[mx]--;
    for(i = 1; i <= mx / 2; i++)
    {
        f[i]++;
        f[mx - i]++;
        int x = bck(pas + 1, f);
        if(x < c)
            c = x;
        f[i]--;
        f[mx - i]--;
    }
    return c;
}
int main()
{
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    scanf("%d", &T);
    while(T--)
    {
        cs++;
        scanf("%d", &n);
        for(i = 1; i <= 9; i++)
            f[i] = 0;
        r = 0;
        for(i = 1; i <= n; i++)
        {
            scanf("%d", &x);
            if(x > r) r = x;
            f[x]++;
        }
        c = bck(1, f);
        printf("Case #%d: %d\n", cs, c);
    }
    return 0;
}
