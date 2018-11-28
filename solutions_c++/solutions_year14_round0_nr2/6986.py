#include <iostream>
#include <iomanip>
using namespace std;

double magia (double c, double f, double x) {
    double rate = 2.0;
    double accum_time = 0.0;
    
    while (true) {
        double waiting = x / rate;
        double buying = (c / rate) + x / (rate + f);
        if (waiting <= buying) {
            return accum_time + waiting;
        }
        else {
            accum_time += c / rate;
            rate += f;
        }
    }
}

int main () {
    int no_cases;
    cin >> no_cases;

    cout << fixed << setprecision(7);
    for (int icase = 1; icase <= no_cases; icase++) {
        double c, f, x;
        cin >> c >> f >> x;
        cout << "Case #" << icase << ": " << magia(c, f, x) << endl;
    }
}
