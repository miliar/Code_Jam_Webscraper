#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

const double EPS = 1e-7;

void solve() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        double C, F, X;
        cin >> C >> F >> X;
        
        double rate = 2;
        double best = X / rate;
        double current = 0;
        
        while (current + C / rate + EPS < best) {
            current += C / rate;
            rate += F;
            best = min(best, current + X / rate);
        }
        
        //cout.precision(7);
        //cout << "Case #" << t << ": " << best << endl;
        printf("Case #%d: %.7lf\n", t, best);
    }
}

int main(int argc, const char * argv[])
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    solve();
    return 0;
}

