#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int have[10];
int sum = 0;

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        memset(have, 0, sizeof(have));
        sum = 0;
        long long x;
        cin >> x;
        if (x == 0)
            printf("Case #%d: INSOMNIA\n", i + 1);
        else
        {
            long long j = 1;
            for (; sum < 10; ++j)
            {
                long long q = j * x;
                while (q > 0)
                {
                    sum += (have[q % 10] == 0);
                    have[q % 10] = 1;
                    q /= 10;
                }
            }
            printf("Case #%d: %I64d\n", i + 1, (j - 1) * x);
        }
    }
    return 0;
}
