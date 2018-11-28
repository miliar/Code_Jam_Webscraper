#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int tc;
    cin >> tc;

    for (int _tc=1; _tc<=tc; _tc++) {
        cout << "Case #" << _tc << ": ";

        double C, F, X;
        cin >> C >> F >> X;

        double rate = 2.0; // initial rate
        double ret = 0.0;

        while(true) {
            double a1 = (C / rate) + (X / (rate + F)); // levelup
            double a2 = (X / rate); // just wait

            //cout << "* " << a1 << " " << a2 << endl;

            if (a1 <= a2) {
                ret += (C / rate);
                rate += F;
            } else {
                ret += (X / rate);
                break;
            }
        }

        printf("%.7f", ret);

        cout << endl;
    }

    return 0;
}