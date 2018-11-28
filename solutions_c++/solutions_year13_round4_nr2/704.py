#include <iostream>
#include <cstdio>

using namespace std;

int n;
long long p;
int t;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int c = 0; c < t; c++)
    {
        long long alval, canval;
        cin >> n >> p;

        long long nowval = 2;
        long long nowp = p;
        long long pow2 = 1;
        for (int i = 0; i < n - 1; i++)
            pow2 *= 2;
        if (p == pow2 * 2)
            alval = pow2 * 2 - 1;
        else
        {
            while (nowp > pow2)
            {
                nowp -= pow2;
                pow2 /= 2;
                nowval *= 2;
            }
            alval = nowval - 2;
        }

        nowp = p;
        nowval = 0;
        long long minus = 1;
        for(int i = 0; i <= n + 10; i++)
        {
            if (nowp <= minus)
            {
                canval = nowval;
                break;
            }
            long long tpow = 1;
            for (int j = 1; j < n - i; j++)
                tpow *= 2;
            nowval += tpow;
            nowp -= minus;
            minus *= 2;
        }
        canval = nowval;

        cout << "Case #" << c + 1 << ": " << alval << ' ' << canval << endl;
    }
    return 0;
}
