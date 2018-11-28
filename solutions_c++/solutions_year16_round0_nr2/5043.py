#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;
string a;
int n;

int get_last()
{
    int i = n - 1;
    for (; i >= 0; --i)
        if (a[i] == '-')
            break;
    return i + 1;
}

int get_last2()
{
    int i = n - 1;
    for (; i >= 0; --i)
        if (a[i] == '+')
            break;
    return i + 1;
}

void bfs()
{
    n = get_last();
    if (n <= 0)
    {
        puts("0");
        return;
    }
    int s = 0;
    while (n > 0)
    {
        if (a[0] == '+')
        {
            int m = get_last2();
            reverse(a.begin(), a.begin() + m);
            for (int i = 0; i < m; ++i)
                a[i] = 88 - a[i];
            ++s;
        }
        reverse(a.begin(), a.begin() + n);
        for (int i = 0; i < n; ++i)
            a[i] = 88 - a[i];
        ++s;
        n = get_last();
    }
    printf("%d\n", s);
}

void solve()
{
    cin >> a;
    n = a.length();
    bfs();
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