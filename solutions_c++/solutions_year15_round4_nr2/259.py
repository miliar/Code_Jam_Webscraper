#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <ctype.h>
#include <limits.h>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <stack>
#include <set>
#include <bitset>
#define CLR(a) memset(a, 0, sizeof(a))
#define REP(i, a, b) for(int i = a;i < b;i++)
#define REP_D(i, a, b) for(int i = a;i <= b;i++)

typedef long long ll;

using namespace std;

const int maxn = 110;
struct node
{
    double rate, tempture;
};
node a[maxn], b[maxn];
bool cmp_shang(node a, node b)
{
    return a.tempture < b.tempture;
}
bool cmp_xia(node a, node b)
{
    return a.tempture > b.tempture;
}
double rate[maxn], tempture[maxn], v, mubiaot;
int n;

int check(double limit)
{
    double now_v = 0, now_t = 0, left_v;
    for(int i = 1;i <= n;i++)
    {
        if(a[i].rate*limit + now_v  + 1e-12<= v)
        {
            now_t = (now_v*now_t + a[i].rate*limit*a[i].tempture)/(now_v+a[i].rate*limit);
            now_v = now_v+a[i].rate*limit;
        }
        else
        {
            left_v = v - now_v;
            now_t = (now_v*now_t + left_v*a[i].tempture)/(now_v+left_v);
            now_v = v;
        }
    }
    if(now_t - 1e-12 > mubiaot)
        return 0;
    if(now_v + 1e-12 < v)
        return 0;
    now_v = 0;
    now_t = 0;
    for(int i = 1;i <=n;i++)
    {
        if(b[i].rate*limit + now_v  + 1e-12<= v)
        {
            now_t = (now_v*now_t + b[i].rate*limit*b[i].tempture)/(now_v+b[i].rate*limit);
            now_v = now_v+b[i].rate*limit;
        }
        else
        {
            left_v = v - now_v;
            now_t = (now_v*now_t + left_v*b[i].tempture)/(now_v+left_v);
            now_v = v;
        }
    }
    if(now_t + 1e-12 < mubiaot)
        return 0;
    if(now_v + 1e-12 < v)
        return 0;
    return 1;
}

void solve()
{
    double l = 0, r = 1e9;
    while(fabs(l - r)> 1e-8)
    {
        double mid = (l + r)/2;
        if(check(mid))
        {
            r = mid;
        }
        else
        {
            l = mid;
        }
    }
    if(check(1e10) == 0)
    {
        printf("IMPOSSIBLE\n");
    }
    else
        printf("%.10lf\n", r);
}


int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("2newllllBout.txt", "w", stdout);
    int ncase;
    scanf("%d", &ncase);
    REP_D(_, 1, ncase)
    {
        printf("Case #%d: ", _);
        scanf("%d%lf%lf", &n, &v, &mubiaot);
        REP_D(i, 1, n)
        {
            scanf("%lf%lf", &a[i].rate, &a[i].tempture);
            b[i].rate = a[i].rate;
            b[i].tempture = a[i].tempture;
        }
        sort(a + 1, a + 1 + n, cmp_shang);
        sort(b +1, b + 1 + n, cmp_xia);
        solve();
    }
    return 0;
}
