#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int T;
double c, f, x;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("b.out", "w", stdout);
    cin >> T;
    for (int cs = 1; cs <= T; ++cs) {
        cin >> c >> f >> x;
        double ftime = 0;
        double ans = x / 2.0;
        for (int i = 1; ; ++i) {
            ftime = ftime + c / (f * (i - 1) + 2.0);
            double tans = ftime + x / (f * i + 2.0);
            if (tans < ans)
                ans = tans;
            else
                break;
        }
        printf("Case #%d: %.7lf\n", cs, ans);
    }
    return 0;
}
