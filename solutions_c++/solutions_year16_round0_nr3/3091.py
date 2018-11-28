#include <bits/stdc++.h>
using namespace std;

int n = 16, j = 50;

long b(int k, int r)
{
    long v = 0;
    for (long i = 0, p = 1; i < n; i++, p *= r)
        if (k & (1 << i))
            v += p;
    return v;
}

long pr(long k)
{
    for (long i = 2, i2 = 4, d = 3; i2 <= k; i++, d += 2, i2 += d)
        if (k % i == 0)
            return i;
    return 0;
}

bool f(int k)
{
    vector<long> div(9);
    for (int i = 2; i <= 10; i++)
        if (!(div[i - 2] = pr(b(k, i))))
            return false;
    for (int i = n - 1; i >= 0; i--)
        cout << (k & (1 << i) ? '1' : '0');
    for (long x : div)
        cout << ' ' << x;
    cout << '\n';
    return true;
}

int main()
{
    cout << "Case #1:\n";
    for (int i = (1 << (n - 1)) + 1, v = 0; i < 1 << n && v < j; i += 2)
        v += f(i);
}
