#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
#define sz(A) (int((A).size()))

const double eps = 1e-5;

double run()
{
    int n;
    cin >> n;
    double v, x;
    cin >> v >> x;

    if (n == 1)
    {
        double r, c;
        cin >> r >> c;

        if (c == x)
        {
            return v / r;
        }
        else
            return -1;
    }
    else
    {
        double r1, c1, r2, c2;
        cin >> r1 >> c1 >> r2 >> c2;

        if (abs(c1 - c2) < eps)
        {
            double r = r1 + r2, c = c1;

            if (c == x)
            {
                return v / r;
            }
            else
                return -1;
        }
 
        double t1 = max(double(0), v * (x - c2) / r1 / (c1 - c2));
        double t2 = max(double(0), (v - r1 * t1) / r2);

        if (abs(t1 * r1 + t2 * r2 - v) < eps && abs((t1 * r1 * c1 + t2 * r2 * c2) / (t1 * r1 + t2 * r2) - x) < eps)
            return max(t1, t2);
        else
            return -1;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;
    cout.precision(30);
    cout << fixed;

    for (int tst = 0; tst < T; tst++)
    {
        cout << "Case #" << tst + 1 << ": ";
        double res = run();

        if (res == -1)
            cout << "IMPOSSIBLE\n";
        else
            cout << res << '\n';
    }
}
