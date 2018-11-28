#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

double c, f, x;
void solve () {
    cin >> c >> f >> x;

    if (x <= c) {
        printf ("%.7lf\n", x/2.0);
        return;
    }

    double res = x/2.0;
    double rate = 2.0;
    double t = c/2.0;
    for (int i = 1; i <= x; i++) {
        rate += f;
        double cur = t + x/rate;
        res = min (res, cur);
        t += c/rate;
    }
    printf ("%.7lf\n", res);
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) cout << "Case #" << i << ": ", solve();
    return 0;
}
