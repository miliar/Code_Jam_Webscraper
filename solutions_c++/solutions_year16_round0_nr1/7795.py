#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <vector>
#include <string>
#define LL long long

using namespace std;

const int maxN = 1000005;
int p[maxN];

void check(int k, int &vis)
{
    int now;
    while (k)
    {
        now = k%10;
        vis = vis | (1<<now);
        k /= 10;
    }
}

int cal(int k)
{
    int val = k, vis = 0, to = (1<<10)-1;
    for (;;)
    {
        check(val, vis);
        if (vis == to)
            return val;
        val += k;
    }
}

void init()
{
    p[0] = -1;
    for (int i = 1; i < maxN; ++i)
        p[i] = cal(i);
}

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    init();
    int T, n;
    scanf("%d", &T);
    for (int times = 1; times <= T; ++times)
    {
        scanf("%d", &n);
        if (p[n] != -1) printf("Case #%d: %d\n", times, p[n]);
        else printf("Case #%d: INSOMNIA\n", times);
    }
    return 0;
}
