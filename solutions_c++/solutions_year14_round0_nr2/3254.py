#include <iostream>
#include <math.h>
#include<iomanip>

using namespace std;

double optimal_k(double C, double F, double X) {
    return (-2*C-C*F+F*X)/(C*F);
}
double cost(int k, double C, double F, double X) {
    double r = 0;
    for(int i = 0; i < k; i++) {
        r += 1/(i*F+2);
    }
    return C*r + X/(k*F+2);
}

int main(int argc, const char * argv[])
{
    int T;
    cin >> T;
    for(int nb = 1; nb <= T; nb++) {
        double C, F, X;
        cin >> C >> F >> X;
        double k = optimal_k(C, F, X);
        cout << "Case #" << nb << ": ";
        if(k<=0) {
            cout << fixed << setprecision(7) << cost(0, C, F, X) << endl;
        }
        else {
            int k0 = floor(k);
            int k1 = ceil(k);
            cout << fixed << setprecision(7) << min(cost(k0, C, F, X), cost(k1, C, F, X)) << endl;
        }
        
    }
}

