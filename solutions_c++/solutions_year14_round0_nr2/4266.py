#include <iostream>
#include <iomanip>

using namespace std;

typedef long double ld;

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        ld c, f, x;
        cin >> c >> f >> x;

        ld totalTime = 0.0, cps = 2;
        while (x / cps > c / cps + x / (cps + f)) {
            totalTime += c / cps;
            cps += f;
        }

        totalTime += x / cps;
        cout << "Case #" << i << ": ";
        cout << setprecision(7) << fixed << totalTime << endl;
    }

    return 0;
}
