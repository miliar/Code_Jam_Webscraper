#include <iostream>
#include <iomanip>
using namespace std;

double cal_min_time(double c, double f, double x, double s) {
    double min_time = x / s;
    double cur_time = 0;

    while (cur_time < min_time) {
        cur_time += c / s;
        s += f;
        if (cur_time + x / s < min_time) {
            min_time = cur_time + x / s;
        }
    }

    return min_time;
}

int main() {
    int T;
    double c, f, x;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        cin >> c >> f >> x;
        cout << "Case #" << t << ": ";
        cout << setiosflags(ios::fixed) << setprecision(7) << cal_min_time(c, f, x, 2.0) <<endl;
    }
}
