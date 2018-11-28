#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

bool solve()
{
    int x, r, c;
    scanf("%d%d%d", &x, &r, &c);
    if (c < r)
        swap(r, c);
    if (x <= 1)
        return 1;
    if (x == 2)
    {
        if (r * c >= 2 && r * c % 2 == 0)
            return 1;
        return 0;
    }
    if (x == 3)
    {
        if (r == 2 && c == 3)
            return 1;
        if (r == 3 && c == 3)
            return 1;
        if (r == 3 && c == 4)
            return 1;
        return 0;
    }
    if (x == 4)
    {
        if (r == 3 && c == 4)
            return 1;
        if (r == 4 && c == 4)
            return 1;
        return 0;
    }
}

int main()
{
    int t;
    freopen("1.txt", "r", stdin);
    freopen("2.txt", "w", stdout);
    scanf("%d", &t);
    for (int tt = 1; tt <= t; ++tt)
    {
        printf("Case #%d: ", tt);
        puts(solve() ? "GABRIEL" : "RICHARD");
    }
    return 0;
}