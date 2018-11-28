#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

double calc(double c, double f, double x, int farmsCount) {
    double cookiesPerSecond = 2.0;
    double timeElapsed = 0.0;
    for (int i = 1; i <= farmsCount; ++i) {
        timeElapsed += c / cookiesPerSecond;
        cookiesPerSecond += f;
    }

    return timeElapsed + x / cookiesPerSecond;
}

void solve(int testNumber) {
    double c, x, f;
    cin >> c >> f >> x;

    long long left = 0, right = 1000000;
    while (left + 2 < right) {
        //cout << left << " " << right << endl;
        long long mid1 = left + ((right - left) / 3);
        long long mid2 = left + (2 * (right - left) / 3);

        double cost1 = calc(c, f, x, mid1);
        double cost2 = calc(c, f, x, mid2);

        if (cost1 < cost2) {
            right = mid2;
        } else {
            left = mid1;
        }
    }

    printf("Case #%d: %.8f\n", testNumber, min(calc(c, f, x, left + (right - left) / 2), min(calc(c, f, x, left), calc(c, f, x, right))));
}

int main() {
    int tests;
    cin >> tests;
    for (int i = 0; i < tests; i++) {
        solve(i + 1);
    }

    return 0;
}
