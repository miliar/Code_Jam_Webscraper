#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int t;
    double c, f, x, time, time2, rate, t0;
    cin >> t;
    for (int case_num=1; case_num<=t; case_num++) {
        rate = 2.0;
        t0 = 0.0;
        cin >> c >> f >> x;
        time = x/rate;
        for (int farms=0; true; farms++) {
            t0 += c/rate;
            rate = rate+f;
            time2 = x/rate+t0;
            if (time2 >= time) {
                break;
            }
            time = time2;
        }
        cout << "Case #" << case_num << ": ";
        cout << fixed << setprecision(10) << time << endl;
    }
    return 0;
}
