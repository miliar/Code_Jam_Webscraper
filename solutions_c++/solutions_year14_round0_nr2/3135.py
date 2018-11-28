#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main() {
    freopen("bl.in", "r", stdin);
    freopen("bl.out", "w", stdout);
    int T, ca = 0;
    cin >> T;
    while (T--) {
        double C, F, X;
        cin >> C >> F >> X;
        double tot = 0;
        double ans = 1e20;
        double rate = 2;
        for (int c = 0; c < 1000000; c++) {
            ans = min(ans, tot + X / rate);
            tot += C / rate;
            rate += F;
        }
        printf("Case #%d: %.7lf\n", ++ca, ans);
    }
    return 0;
}
