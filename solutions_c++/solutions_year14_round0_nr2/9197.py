//codejam2014-B-small
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <set>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);

    int T, case_number = 1;

    cin >> T;

    while (T--)
    {
        double C, F, X;

        cin >> C >> F >> X;

        double cps = 2.0, time = 0.0;
        double ans = X/cps;

        while (1)
        {
            time += C/cps;
            cps += F;

            double t = time + X/cps;

            if (t < ans)
                ans = t;
            else
                break;
        }

        cout << "Case #" << case_number++ <<": " << std::fixed << std::setprecision(7) << ans << endl;
    }

    return 0;
}