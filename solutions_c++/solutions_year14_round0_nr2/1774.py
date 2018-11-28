#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int cs = 1; cs <= T; ++cs)
    {
        double C, F, X;
        cin >> C >> F >> X;
        int nmax = (int) ((F * (X - C) - 2 * C) / (F * C)) + 1;
        double ans = X / 2, p = 0;
        for (int i = 1; i <= nmax; ++i)
        {
            p += (C / (2 + (i - 1) * F));
            ans = min(ans, p + X / (2 + i * F));
        }
        cout << "Case #" << cs << ": " << setprecision(7) << fixed << ans << endl;
    }
}
