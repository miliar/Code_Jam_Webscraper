#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <iomanip>

using namespace std;

#define DEBUG(x) cout << '>' << #x << ':' << (x) << endl;

int main() {
    double c, f, x;
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> c >> f >> x;
        int n = max(0, (int) ceil(x / c - 1 - 2 / f));
        double res = 0;
        for (int i = 0; i <= n - 1; ++i)
            res += c / (2 + i * f);
        res += x / (2 + n * f);
        cout << fixed << setprecision(7);
        cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}