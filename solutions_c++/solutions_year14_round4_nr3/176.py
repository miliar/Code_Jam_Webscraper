#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <memory.h>

using namespace std;

struct rect
{
    int x1, x2, y1, y2;
    rect()
    {
        
    }
    rect(int x1, int y1, int x2, int y2) : x1(x1), y1(y1), x2(x2), y2(y2)
    {}
};

int len(int a, int b, int c, int d)
{
    if (c < a || (c == a && b < d))
    {
        swap(a, c);
        swap(b, d);
    }
    if (c <= b + 1)
        return 0;
    return c - b - 1;
}

int len(rect r1, rect r2)
{
    int a = len(r1.x1, r1.x2, r2.x1, r2.x2), b = len(r1.y1, r1.y2, r2.y1, r2.y2);
    if (a == 0)
        return b;
    if (b == 0)
        return a;
    return max(a, b);
}

bool used[2000];
long long d[2000];

int solve(vector<rect> &g)
{
    memset(used, 0, sizeof(used));
    for (int i = 0; i < g.size(); ++i)
        d[i] = 1000000000;
    d[g.size() - 2] = 0;
    for (int t = 0; t < g.size(); ++t)
    {
        int v = -1;
        for (int i = 0; i < g.size(); ++i)
            if (!used[i] && (v == -1 || (d[i] < d[v])))
                v = i;
        used[v] = true;
        for (int i = 0; i < g.size(); ++i)
            d[i] = min(d[i], d[v] + len(g[i], g[v]));
    }
    return d[g.size() - 1];

}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int q = 0; q < t; ++q)
    {
        printf("Case #%d: ", q + 1);
        int n, w, h;
        scanf("%d%d%d", &w, &h, &n);
        vector<rect> g(n);
        for (int i = 0; i < n; ++i)
            scanf("%d%d%d%d", &g[i].x1, &g[i].y1, &g[i].x2, &g[i].y2);
        g.push_back(rect(-1, -1, -1, 1000000000));
        g.push_back(rect(w, -1, w, 1000000000));
        printf("%d\n", solve(g));
    }
    return 0;

}
