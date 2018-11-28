#include <iostream>
#include <iomanip>

using namespace std;


int main() {

    int t;
    cin >> t;

    for(int i = 1; i<=t; i++) {
        double c, f, x;

        cin >> c >> f >> x;

        double time = 0;
        double rate = 2;

        double min = time + x / rate;
        double end = min;

        while(end <= min) {
            min = end;
            double dtime = c/rate;
            time += dtime;
            rate+=f;

            end = time + x/rate;

        }

        cout << "Case #" << i << ": " << fixed << setprecision(7) << min << endl;
    }
    return 0;
}
