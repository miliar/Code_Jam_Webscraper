#include <array>
#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>

#define r(_c_) begin(_c_), end(_c_)

using namespace std;

void solve () {
    double C, F, X;
    cin >> C >> F >> X;

    if (X <= C) {
        cout << 0.5 * X;
        return;
    }

    double seconds = 0;
    size_t nFarms = 0;

    double noFarm;
    double withFarm;

    while (true) {
        seconds += 1.0 / (2 +  nFarms    * F) * C;

        noFarm =   1.0 / (2 +  nFarms    * F) * (X - C);
        withFarm = 1.0 / (2 + (nFarms+1) * F) * X;
        if (noFarm < withFarm) {
            seconds += noFarm;
            break;
        } else {
            ++nFarms;
        }
    }

    cout << seconds;
    
}

int main () {
    cout << setprecision(10);
    size_t T; cin >> T;
    for (size_t i = 1; i <= T; ++i)
        { cout << "Case #" << i << ": "; solve(); cout << "\n"; }
}