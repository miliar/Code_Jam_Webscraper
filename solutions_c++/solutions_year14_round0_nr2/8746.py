#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main() {
    ifstream in ("B-large.in");
    ofstream out ("cookie_clicker_alpha.out");
    double rate, time, cost, increase, goal;
    int tests;
    in >> tests;
    for (int a = 0; a < tests; ++a) {
        time = 0.0000000;
        rate = 2.0000000;
        in >> cost >> increase >> goal;
        out << fixed;
        while (goal/rate >= cost/rate + goal/(rate + increase)) {
            time += cost/rate;
            rate += increase;
        }
        time += goal/rate;
        if (a != tests-1) {
            out << "Case #" << a+1 << ": " << setprecision(7) << time << '\n';
        }
        else {
            out << "Case #" << a+1 << ": " << setprecision(7) << time << endl;
        }
    }
    return 0;
}
