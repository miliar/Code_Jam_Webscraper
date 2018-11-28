#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

long long myPow(long long a, long long b)
{
    long long ans = 1;

    for (int i = 1; i <= b; ++i)
        ans *= a;

    return ans;
}

long long f(long long st, long long en, int k, int c)
{
    long long ans = 0, wt = myPow(k, c - 1);

    for (int i = 1, j = st; i <= c; ++i)
    {
        ans += wt * (j - 1);

        if (j < k)
            ++j;

        wt /= k;
    }

    return ans + 1;
}

int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt");

    long long t, k, c, s;

    in >> t;

    for (int i = 1; i <= t; ++i)
    {
        in >> k >> c >> s;
        out << "Case #" << i << ": ";

        if (c * s < k)
            out << "IMPOSSIBLE\n";

        else
        {
            for (int j = 1; j <= (k + c - 1) / c; ++j)
            {
                long long st = (j - 1) * c + 1, en = min(st + c - 1, k);

                out << f(st, en, k, c) << ' ';
            }

            out << endl;
        }
    }
}
