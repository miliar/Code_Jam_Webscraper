#include <iostream>

using namespace std;

const long long mod = 1000 * 1000 * 1000 + 7;

long long pow(long long x, long long y)
{
    long long res = 1;
    for (; y; y >>= 1)
    {
        if (y & 1)
            res = res * x % mod;
        x = x * x % mod;
    }
    return res;
}

long long Div(long long x, long long y)
{
    return x * pow(y, mod - 2) % mod;
}

int main()
{
    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++)
    {
        int n, m;
        cin >> n >> m;

        const int x[] = {1, 3, 6, 4, 12};

        long long d[128][5] = {};

        d[0][0] = 0;
        d[1][0] = 1;
        d[2][0] = 0;
        d[2][1] = m % 3 ? 0 : 3;
        d[2][2] = m % 6 ? 0 : 6;
        d[3][3] = m % 4 ? 0 : 4;

        for (int i = 4; i <= n; i++)
        {
            d[i][0] = d[i - 3][0];
            d[i][1] = ((d[i - 4][0] + d[i - 4][1]) * d[2][1] + d[i - 3][1]) % mod;
            d[i][2] = ((d[i - 4][0] + d[i - 4][1] + d[i - 4][2]) * d[2][2] + d[i - 4][2] * d[2][1] + d[i - 3][2]) % mod;
            d[i][3] = i > 4 ? ((d[i - 5][0] + d[i - 5][3]) * d[3][3] + d[i - 3][3]) % mod : 0;
            d[i][4] = i > 4 ? ((d[i - 5][1] + d[i - 5][2] + d[i - 5][4]) * d[3][3] + (d[i - 4][4] + d[i - 4][3]) * (d[2][2] + d[2][1]) + d[i - 3][4]) % mod : 0;
        }

        for (int i = 0; i <= n; i++)
        {
            for (int j = 0; j < 5; j++)
                cerr << d[i][j] << " ";
            cerr << endl;
        }

        long long ans = 0;

        for (int i = n - 4; i <= n; i += 2)
            for (int j = 0; j < 5; j++)
                if (i >= 0)
                    ans += Div(d[i][j], x[j]) * (1 + (i == n - 2));

        ans += n == 2;

        cout << "Case #" << tt << ": " << ans % mod << endl;
    }

    return 0;
}
