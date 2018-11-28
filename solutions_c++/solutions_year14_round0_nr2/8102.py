#include <iostream>
#include <set>
#include <algorithm>
#include <iterator>

using namespace std;



int main() {
    int T;
    cin >> T;
    for (int test=0; test<T; ++test) {
        double C, F, X;
        cin >> C >> F >> X;

        double cps = 2.0;
        double t = 0.0f;
        double time_to_win = t + X / cps;
        double time_to_farm = C / cps;
        double time_to_win_with_farm = time_to_farm + X/(F+cps);

        while (time_to_win_with_farm < time_to_win) {
            cps += F;
            t += time_to_farm;
            time_to_win = X / cps;
            time_to_farm = C / cps;
            time_to_win_with_farm = time_to_farm + X/(F+cps);
            
        }

        t += time_to_win;


        cout << "Case #" << test+1 << ": ";
        
        cout.precision(20);
        cout << t;

        cout << endl;

    }
}

