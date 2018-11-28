// vim:set sw=4 et smarttab:
// Round 2 2014

#include <cstdio>
#include <algorithm>

int n, a[1000];

struct comp
{
    bool operator() (const int &lhs, const int &rhs) const
    {
        return a[lhs] < a[rhs];
    }
};

void move(int from, int to)
{
    int dir;
    if (from < to)
        dir = +1;
    else
        dir = -1;
    int cur = from;
    while (cur != to)
    {
        std::swap(a[cur], a[cur + dir]);
        cur += dir;
    }
}

int solve()
{
    int index[1000];
    int st = 0, en = n - 1;
    int ret = 0;
    for (int i = 0; i < n; ++i)
    {
        for (int i = 0; i < n; ++i)
            index[i] = i;
        std::sort(index, index + n, comp());
        int cur = index[i];
        int left_cost = cur - st;
        int right_cost = en - cur;
        if (left_cost < right_cost)
        {
            move(cur, st);
            ++st;
            ret += left_cost;
        }
        else
        {
            move(cur, en);
            --en;
            ret += right_cost;
        }
    }
    return ret;
}

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
            scanf("%d", &a[i]);
        int answer = solve();
        printf("Case #%d: %d\n", tc, answer);
    }
}
