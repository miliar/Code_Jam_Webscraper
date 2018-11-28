#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  
    int T;
    
    cin >> T;
    
    for (int _i = 1 ; _i <= T ; _i++) {
        
        double C, F, X;
        
        cin >> C >> F >> X;
        
        double R = 2.;
        double n = 0.;
        double t = 0.;
        
        while (n < X){
            if (X/R < C/R + X/(R+F)) {
                t += X/R;
                n = X;
            }
            else {
                t += C/R;
                R += F;
            }
        }
        
        
        cout << "Case #" << _i << ": ";
        printf("%.7f\n", t);

    }
    
    return 0;
}

