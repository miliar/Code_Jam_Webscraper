#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

typedef double ld;

ifstream in("input-b.txt");
ofstream out("output-b.txt");

ld solve(ld cost, ld extraGain, ld target) {
    ld gain = 2, timeSpent = 0;
    while (true) {
        ld timeToBuy = cost / gain + target / (gain + extraGain);
        ld timeToWin = target / gain;
        if (timeToWin < timeToBuy) {
            timeSpent += timeToWin;
            break;
        } else {
            timeSpent += cost / gain;
            gain += extraGain;
        }
    }
    return timeSpent;
}

int main() {
    out.precision(8);
    int t;
    ld c, f, x;
    in >> t;
    for (int i = 0; i < t; i++) {
        in >> c >> f >> x;
        x = solve(c, f, x);
        out << "Case #" << i + 1 << ": " << fixed << x << '\n';
    }
    return 0;
}
