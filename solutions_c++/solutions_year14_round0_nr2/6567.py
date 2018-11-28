#include <iostream>
#include <cstdio>
#include <iomanip>

using namespace std;

int main()
{
    long long int t, count = 0;
    double  c, r, f, x;

    scanf("%lld", &t);

    while (t--) {
        count++;
        r = 2.0;
      //  setprecision(6);
        scanf("%lf%lf%lf", &c, &f, &x);
        double ans = 0.0, c1, x1;

        while (1) {
            c1 = c / r;
            x1 = x / (r + f);

            if (x1 + c1 >= (x / r)) {
                ans = ans + (x / r);
                //cout << "adding x : " << x1 << endl;
                break;
            } else {
                ans = ans + c1;
                //cout << "adding c : " << c1 << endl;
                r = r + f;
            }
        }

        printf("Case #%lld: %0.6lf\n", count, ans);
    }

    return 0;
}
