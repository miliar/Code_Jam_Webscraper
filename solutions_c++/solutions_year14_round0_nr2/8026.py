#include <iostream>
#include <limits>

using namespace std;
static int s_i = 1;

void solveProblem() {
    double c, f, x;
    double current_production = 2;

    cin >> c >> f >> x;

    if (c >= x ) {
        cout.precision(7);
        cout << fixed << (x / current_production);
    } else {
        double current_time = c / current_production;

        while (true) {
            double time_build = x / (current_production + f) + current_time;
            double time_not_build = current_time + (x - c) / current_production;
            if (time_build < time_not_build) {
                current_time = current_time + c / (current_production + f);
                current_production += f;
                continue;
            } else {
                current_time = time_not_build;
                break;
            }
        }
        cout.precision(7);
        cout << fixed << current_time;

    }

}

int main() {
    int t;
    cin >> t;
    while (t --) {
        cout << "Case #" << s_i << ": ";
        solveProblem();
        s_i ++;
        if (t != 0) {
            cout << endl;
        }
    }
}