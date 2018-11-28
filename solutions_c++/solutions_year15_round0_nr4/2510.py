#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <ctime>
#include <cassert>
using namespace std;

#ifdef LOCAL
    #define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
    #define eprintf(...) 0
#endif

const int HARD[][4] =
{
    {0, 1, 1, 1},
    {0, 0, 1, 1},
    {0, 1, 1, 1},
    {0, 0, 1, 1},
    {0, 0, 1, 1},
    {0, 0, 0, 1},
    {0, 0, 1, 1},
    {0, 1, 0, 1},
    {0, 0, 0, 0},
    {0, 0, 1, 0}
};

void solve()
{
    int x, r, c;
    scanf("%d%d%d", &x, &r, &c);
    x--; r--; c--;
    if (r > c)
        swap(r, c);

    int cur = 0;
    for (int i = 0; i < 4; i++)
        for (int j = i; j < 4; j++)
        {
            if (r == i && c == j)
            {
                printf("%s\n", HARD[cur][x] ? "RICHARD" : "GABRIEL");
                return;
            }
            cur++;
        }

    throw;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }

    eprintf("time = %.3lf\n", (double) clock() / CLOCKS_PER_SEC);

    return 0;
}
