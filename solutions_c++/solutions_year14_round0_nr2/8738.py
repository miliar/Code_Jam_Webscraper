#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("infile.in", "r", stdin);
    freopen("outfile.txt", "w", stdout);

    int t;

    cin >> t;

    int p = 1;

    while (t--) {
        double c, f, x;
        cin >> c >> f >> x;
        double b = 2.0;
        double t = 0;
        while (1) {
            if (x/b > ((c/b) + x/(b + f))) {
                t += c/b;
                b += f;
            } else {
                t += x/b;
                break;
            }
        }
        printf("Case #%d: %0.7lf\n", p, t);

        p++;
    }

    return 0;
}
