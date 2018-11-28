#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

double solve(double c, double f, double x) {
    double ans = x / 2;
    double time = 0;
    double rate = 2;
    for (int farms = 1, fails = 0; ; ++farms) {
        time += c / rate;
        rate += f;
        double option = time + x / rate;
        if (option < ans) {
            ans = option;
        }
        else {
            ++fails;
            if (fails == 10) {
                break;
            }
        }
    }
    return ans;
}

int main() {
    cout.setf(ios_base::fixed);
    cout.precision(7);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        double c, f, x;
        cin >> c >> f >> x;
        double ans = solve(c, f, x);
        cout << ans;
        cout << "\n";
    }
    return 0;
}
