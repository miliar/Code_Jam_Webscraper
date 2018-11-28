#include <cstdio>
#include <algorithm>

using namespace std;

int main ()
{
    int No; scanf ("%d", &No);

    for (int _i = 0; _i < No; ++_i) {
        double c, f, x;
        scanf ("%lf%lf%lf", &c, &f, &x);

        double best = x / 2, last = 0;
        for (int i = 1; i <= x; ++i) {
            last += c / (2 + (i - 1) * f);
            best = min(best, last + x / (2 + i * f));
        }

        printf ("Case #%d: %.7lf\n", _i + 1, best);
    }

    return 0;
}

