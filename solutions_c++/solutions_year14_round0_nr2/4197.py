#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("infile.in", "r", stdin);
    freopen("outfile.txt", "w", stdout);
    double v, t, x,f, b;
    int n, i;

    cin >> n;
    for (i = 1; i <= n; i++) {
        cin >> b;
        cin >> f;
        cin >> x;
        v = 2;
        t = 0;
            while (1) {
                if ((x/v) > (b/v + x/(v+f))) {
                    t = t + b/v;
                    v = v+f;
                } else {
                    t = t + x/v;
                    break;
                }
            }
            printf("Case #%d: %.7lf\n", i, t);
    }

    return 0;
}


