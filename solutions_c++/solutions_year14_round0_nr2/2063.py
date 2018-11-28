#include <iostream>
#include <iomanip>
using namespace std;

double solve(double c, double f, double x)
{
    double r = 2;
    double t = 0;
    while (x/r > c/r + x/(r+f))
    {
        t += c/r;
        r += f;
    }
    return t + x/r;
}

int main()
{
    int t;
    cin >> t;

    cout.precision(7);
    for (int i = 0; i < t; ++i)
    {
        double c, f, x;
        cin >> c >> f >> x;
        cout << "Case #" << i + 1 << ": " << fixed << solve(c, f, x) << endl;
    }

    return 0;
}
