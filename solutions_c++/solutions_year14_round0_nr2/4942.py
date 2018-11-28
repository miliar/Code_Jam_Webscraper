#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int ca = 1; ca <= T; ca++) {
        double C, F, X;
        cin >> C >> F >> X;
        double f = 0;
        double ans = X / 2;
        int i = 1;
        while (1) {
            f += C / (2.+F*(i-1));
            double newans = f + X / (2+F*i);
            if (newans >= ans) {
                break;
            }
            ans = newans;
            i++;
        }
        printf("Case #%d: %.7lf\n", ca, ans);
    }
    return 0;
}
