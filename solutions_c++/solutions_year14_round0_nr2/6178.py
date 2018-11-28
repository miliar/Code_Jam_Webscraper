#include "1b.h"

using namespace std;





int main(){
    
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        
        double C, F, X;
        cin >> C >> F >> X;
        double rate = 2, time =X/rate, sink_time = 0;
        bool miao = true;
        while (miao) {
            double t = sink_time + C/rate + X/(rate + F);
            
            if (t  < time) {
                time = t;
                sink_time += C/rate;
                rate += F;
            } else {
                miao = false;
            }
            
        }
        cout.precision(7);
        cout << "Case #" << i+1 << ": " <<time << endl;
    }
    
    
}