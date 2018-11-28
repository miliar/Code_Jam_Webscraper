#include <iostream>
#include <sstream>
#include <string>
#include <iomanip>
#define eps 1e-9
using namespace std;

double solve() {
    double C, F, X;
    cin >> C >> F >> X;
    double t = 0, c = 0, i = 2;

    while (c < X - eps) {
        double stay = (X - c)/i;
        if (c > C - eps) {
            double buy = (X - c + C)/(i + F); 
            if (buy + eps < stay) {
                c -= C;
                i += F;
            } else {
                return t + stay;
            }
        } else {
            double to_buy = (C - c)/i;
            if (stay + eps < to_buy) {
                return t + stay;
            } else {
                c = C;
                t += to_buy;
            }
        }
    }
    return t;
}

int main() {
    int t;
    cin >> t;
    for (int qq = 1; qq <= t; qq++) {
        cout << "Case #" << qq << ": " << std::setprecision(15) << solve() << endl;
    }
}
