#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
#define sz(A) (int((A).size()))

int64 rev(int64 x)
{
    string s;

    while (x > 0)
    {
        s += '0' + x % 10;
        x /= 10;
    }
    int64 res = 0;

    for (int i = 0; i < sz(s); i++)
        res = res * 10 + s[i] - '0';
    return res;
}

int64 reach(int64 x, int64 first)
{
    int64 copy = x, num = 0, pow10 = 1;

    while (x > 0)
    {
        num++;
        x /= 10;
        pow10 *= 10;
    }
    x = copy;
    pow10 /= 10;
    int64 half = 0, nowpow = 1;

    for (int i = 0; i < num / 2; i++)
    {
        half += x / pow10 * nowpow;
        nowpow *= 10;
        x %= pow10;
        pow10 /= 10;
    }

    if (half < 10)
        return x;
    else if (x < first)
        return reach(copy - x - 1, first) + x + 1;
    else
        return half + x - (first == 1 ? 0 : first);
}

int64 solve(int64 n)
{
    if (n < 10)
    {
        return n;
    }

    int64 num = 0, copy = n, res = 0, pow10 = 1;

    while (n >= 100)
    {
        n /= 10;
        num++;
        pow10 *= 10;
        res += 19 + reach(10 * pow10 - 9, 9) - 1;
    }
    int64 first = n / 10;
    n = copy;

    if (first == 1)
    {
        res += 10 + reach(n, 1);
    }
    else
    {
        if (n == pow10 * 10 * first)
        {
    	    res += (first - 1) + 10 + reach(n - 1, first - 1) + (first == 2 ? 0 : 1);
        }
        else
        {
    	    res += first + 10 + reach(n, first);
        }
    }
    return res;
}

int main()
{
    ios::sync_with_stdio(0);

    while (0)
    {
        int64 x, first;
        cin >> x >> first;
        cout << reach(x, first);
    }

    int T;
    cin >> T;

    for (int tst = 0; tst < T; tst++)
    {
        int64 n;
        cin >> n;

        if (n % 10 != 0)
            cout << "Case #" << tst + 1 << ": " << min(solve(n), solve(rev(n)) + 1) << '\n';
        else
            cout << "Case #" << tst + 1 << ": " << solve(n) << '\n';
    }

    return 0;
}
