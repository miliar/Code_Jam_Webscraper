#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int tt=1; tt<=t; tt++)
    {
        long long n, p;
        cin >> n >> p;

        long long x = 2;
        for (long long m = n, q = p; m>=0;)
        {
            if (q+q <= 1<<m)
                break;
            x = x + x;
            m--;
            q -= 1<<m;
        }
        x -= 2;

        long long y = (1<<n) - 1;
        for (long long m = n, q = p, i = 0; m>=0; i++)
        {
            if (q >= 1<<m)
                break;

            y -= 1 << i;
            m--;
        }

        if (p == 1<<n)
            x = y = p-1;

        cout << "Case #" << tt << ": " << x << " " << y << endl;
    }

    return 0;
}
