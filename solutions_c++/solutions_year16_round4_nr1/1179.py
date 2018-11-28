#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;
#define N 4099
int a[N], b[N];
int n, m;

int win(int x, int y)
{
    if ((x == 0 && y == 1) ||
        (x == 1 && y == 2) ||
        (x == 2 && y == 0))
        return x;
    return y;
}

bool check(bool debug=0)
{
    memcpy(b, a, sizeof(a));
    for (int k = 0; k < n; ++k)
    {
        int ii = 1 << k;
        if (debug)
        {
            for (int i = 0; i < m; i += ii)
                printf("%d ", b[i]);
            puts("");
        }
        for (int i = 0; i < m; i += ii * 2)
            if (b[i] != b[i + ii])
            {
                b[i] = win(b[i], b[i + ii]);
            }
        else
            return 0;
    }
    return 1;
}

void place0(int l, int r, int s)
{
    if (s == 1)
    {
        a[l] = 0;
        return;
    }
    int mid = (l + r) >> 1;
    place0(l, mid, (s >> 1) + (s & 1));
    place0(mid + 1, r, (s >> 1));
}

void place2(int l, int r, int s)
{
    if (s == 1)
    {
        a[r] = 2;
        return;
    }
    int mid = (l + r) >> 1;
    place2(l, mid, (s >> 1));
    place2(mid + 1, r, (s >> 1) + (s & 1));
}

void print()
{
    for (int i = 0; i < m; ++i)
        // printf("%d", a[i]);
        putchar(a[i] == 0 ? 'P' : a[i] == 1 ? 'R' : 'S');
    puts("");
}

void solve()
{
    int r, p, s;
    scanf("%d%d%d%d", &n, &r, &p, &s);
    if (abs(r - p) > 1 || abs(p - s) > 1 || abs(r - s) > 1)
    {
        puts("IMPOSSIBLE");
        return;
    }
    // P > R, R > S, S > P
    // 0 > 1, 1 > 2, 2 > 0
    m = 1 << n;
    for (int i = 0; i < m; ++i)
        a[i] = 1;
    if (p)
        place0(0, m - 1, p);
    if (s)
        place2(0, m - 1, s);
    print();
    return;
    for (int i = 0; i < p; ++i)
        a[i] = 0;
    for (int i = p; i < p + r; ++i)
        a[i] = 1;
    for (int i = p + r; i < p + r + s; ++i)
        a[i] = 2;
    do
    {
        if (check())
        {
            print();
            return;
        }
    }
    while (next_permutation(a, a + m));
    puts("IMPOSSIBLE");
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
        solve();
    }
    return 0;
}