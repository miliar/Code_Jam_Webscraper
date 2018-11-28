#include <iostream>
#include <cstdio>

using namespace std;

int n, k, c, s, pos;

long long choose(int r, long long b)
{
    if (!r) return 0;
    ++pos;
    return b * (pos - 1) + choose(r - 1, b / k);
}

int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
    {
        scanf("%d%d%d", &k, &c, &s);
        long long x = 1;
        for (int j = 0; j < c; ++j) x *= k;
        if (s * c < k)
        {
            printf("Case #%d: IMPOSSIBLE\n", i + 1);
        }
        else
        {
            printf("Case #%d: ", i + 1);
            pos = 0;
            while (pos < k)
                cout << choose(min(c, k - pos), x / k) + 1 << ' ';
            cout << '\n';
        }
    }
    return 0;
}