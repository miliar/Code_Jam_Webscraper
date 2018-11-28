#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

double calc(double c, double f, double x, int k)
{
    double v = 2;
    double ans = 0;
    for (int i = 0; i < k; i++)
    {
        ans += c / v;
        v += f;
    }
    ans += x / v;
    return ans;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;
    cin >> t;
    cout.precision(20);
    cout << fixed;
    for (int T = 0; T < t; T++)
    {
        double c, f, x;
        cin >> c >> f >> x;
        int k = ceil((x - c) / c - 2 / f);
        cout << "Case #" << T + 1 << ": " << calc(c, f, x, k) << endl;
    }
    return 0;
}
