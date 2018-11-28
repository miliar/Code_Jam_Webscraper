#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        long long m, r, r1, r2, a, ans = 0;

        cin >> r >> m;
        r2 = r;
        r1 = r + 1;
        a = r1 * r1 - r2 * r2;
        while (m >= a)
        {
            m = m - a;
            ans ++;
            r2 += 2;
            r1 += 2;
            a = r1 * r1 - r2 * r2;

        }
        cout << "Case #" << i << ": " << ans << endl;
    }
}
