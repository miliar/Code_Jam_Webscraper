#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

// 2 cookies per second
// C - cost per farm
// F - cookies per second per farm
// X - win condition

double doIt(double C, double F, double X) {
    double elasped_time = 0;    // Time that has elapsed
    double before_time, after_time;
    double rate = 2;
    while(1) {
        before_time = X / rate;     // Time it takes to reach end
        after_time = X / (rate + F) + (C / rate);

        if (before_time <= after_time) {
            return before_time + elasped_time;
        } else {
            elasped_time += C / rate;
            rate += F;
        }
    }
}

int main() {
    cout << fixed;
    cout << setprecision(7);

    double T, C, F, X;
    cin >> T;
    for (int i=0; i<T; ++i) {
        cin >> C >> F >> X;
        cout << "Case #" << i+1 << ": " << doIt(C, F, X) << endl;
    }
    
    return 0;
}
