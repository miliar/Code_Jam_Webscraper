#include <iostream>
#include <cmath>
using namespace std;

long long r, t;

// (r+n)(n-r+1)/2 <= t
// n(n+1) <= 2t+r^2-r
// apply n = r+2x-1
// 2x^2 + (2r - 1)x - t <= 0
// apply x = (-b +/- sqrt(b2 - 4ac)) / 2a
// x1 = ((-(2r - 1) + sqrt((2r - 1)^2 + 8t)) / 4
// x2 = ((-(2r - 1) - sqrt((2r - 1)^2 + 8t)) / 4
long long solve() {
    double x1, x2;
    double bs = (2*r - 1);
    x1 = (-bs + sqrt(bs*bs + 8*t)) / 4;
    x2 = (-bs - sqrt(bs*bs + 8*t)) / 4;
    return max((long long)x1, (long long)x2);
}

int main() {
    int totalTests;
    cin >> totalTests;
    for (int test = 1; test <= totalTests; test++) {
        cin >> r >> t;
        cout << "Case #" << test << ": " << solve() << "\n";
    }
    return 0;
}
