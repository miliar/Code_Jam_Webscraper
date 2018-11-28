#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++)
    {
        double v, x;
        int n;

        cin >> n >> v >> x;

        bool cold = false;
        bool hot = false;

        double u[128], y[128];

        for (int i = 0; i < n; i++)
        {
            cin >> u[i] >> y[i];

            cold |= y[i] <= x + 1e-7;
            hot |= y[i] >= x - 1e-7;
        }

        cout << "Case #" << tt << ": ";

        if (!cold || !hot)
        {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }

        double plusV = 0;
        double plusT = 0;
        double minusV = 0;
        double minusT = 0;
        double equalV = 0;

        for (int i = 0; i < n; i++)
            if (y[i] < x - 1e-7)
            {
                minusV += u[i];
                minusT += u[i] * (x - y[i]);
            }
            else if (y[i] > x + 1e-7)
            {
                plusV += u[i];
                plusT += u[i] * (y[i] - x);
            }
            else
                equalV += u[i];

        double m = min(plusT, minusT);

        if (m > 1e-9)
        {
            plusV /= plusT / m;
            minusV /= minusT / m;

            equalV += plusV + minusV;
        }

        cout.setf(ios::fixed);
        cout.precision(12);

        cout << v / equalV << endl;
    }

    return 0;
}
