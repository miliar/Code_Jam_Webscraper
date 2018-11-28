#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int T;
double C, F, X;

void solve() {
    double cookiesPerSec = 2.0;
    double minTime = X / cookiesPerSec;
    double newTime, factoryTime = 0.0;

    if (C < X) {
        while (true) {
            factoryTime += C / cookiesPerSec;
            cookiesPerSec += F;
            newTime = factoryTime + X / cookiesPerSec;
            if (newTime < minTime) {
                minTime = newTime;
            }
            else {
                break;
            }
        }
    }

    cout << setiosflags(ios::fixed) << setprecision(7) << minTime << "\n";
}

int main() {
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        cin >> C >> F >> X;
        solve();
    }
}

