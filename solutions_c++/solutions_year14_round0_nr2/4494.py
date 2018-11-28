#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
    int T; cin >> T;
    for(int t = 0; t < T; t++){
        double C; // cookies for a farm
        double F; // cookies a farm produces
        double X; // goal
        cin >> C >> F >> X;
        
        double f = 2.0; // production rate per second
        double y = 0.0; // elapsed time
        
        if (X <= C) {
            y = X / f;
            goto END;
        }

        y += C / f;
        while(true){
            double rem_time = (X - C) / f;
            double rem_time_with_farm = X / (f + F);

            if (rem_time_with_farm < rem_time) {
                // pay for a farm
                f += F; 
                y += C / f;
            }
            else {
                y += rem_time;
                break;
            }
        }

        END:
        cout << "Case #" << t + 1 << ": " << fixed << setprecision(7) << y << endl;
    }

    return 0;
}
