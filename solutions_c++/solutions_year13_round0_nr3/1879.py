#include <iostream>
#include <stdio.h>

using namespace std;
typedef long long ll;
int n;
ll fs[50];

int check(ll num)
{
    ll x = num * num;
    int a[20];
    int b = 0;
    while (x)
    {
        a[b++] = x % 10;
        x /= 10;
    }
    for (int i = 0; i * 2 < b; ++i)
        if (a[i] != a[b - i - 1])
            return 0;
    fs[n++] = num * num;
    return 0;
}

int go(int i, ll num, int d)
{
    if (i >= d)
        check(num);
    else
        for (int j = 0; j <= 2; ++j)
            if (i + j > 0)
                go(i + 1, num * 10 + j, d);

    return 0;
}

int main()
{
    freopen("C-large-1.in", "r", stdin);
    freopen("fands.out", "w", stdout);
    for (int i = 1; i <= 8; ++i)
        go(0, 0, i);

    fs[n++] = 9;

    int nTest;
    cin >> nTest;
    for (int test = 1; test <= nTest; ++test)
    {
        ll a, b;
        cin >> a >> b;

        int res = 0;
        for (int i = 0; i < n; ++i)
            if (a <= fs[i] && fs[i] <= b)
                res++;

        cout << "Case #" << test << ": " << res << endl;
    }
    return 0;
}
