#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>

using namespace std;

const double eps = 1e-10;

double foo(double c, double f, double x, double f1)
{
    double s = (double) x / f;
    double ans = 0;
    if (f >= x * 8)
        return (double) s;
    double r = foo(c, f + f1, x, f1);
    if ((s - eps) > (double)(r + (double) c / f))
        ans = ans + (double)(r + (double) c / f);
    else
        ans = ans + s;
    //cout <<  fixed << setprecision(8) << (double)ans << endl;
    return ans;
}

int main()
{
    //freopen("B-small-attempt2.in", "r", stdin);
    //freopen("B-small-attempt2.out", "w", stdout);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        double c, f, x;
        cin >> c >> f >> x;
        double ans = 0;
        ans = foo(c, 2.0, x, f);
        cout << "Case #" << i + 1 << ": " << fixed << setprecision(7) << (double) ans << endl;
    }

}
