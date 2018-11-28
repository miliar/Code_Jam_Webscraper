#include <iostream>
#include <cstdio>


using namespace std;


int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int t;
    cin >> t;
    for (int p = 0; p < t; ++p) {
        cout << "Case #" << p + 1 << ": ";
        double c, x, f;
        double cg = 2.0;
        cin >> c >> f >> x;
        double ans1 = c / cg + x / (cg + f);
        double ans2 = x / cg;
        double cans = 0.0;

        for (; ans1 <= ans2; ) {
            cans += c / cg;
            cg += f;
            ans2 = ans1;
            ans1 = cans + c / cg + x / (cg + f);    
        }
        printf("%.13lf\n", ans2);
    }
    return 0;
}