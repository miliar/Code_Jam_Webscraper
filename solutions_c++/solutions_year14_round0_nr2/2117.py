#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int T;
    double C, F, X;
    cin >> T;
    for (int i=1; i<= T; i++) {
        cin >> C >> F >> X;
        double min = X / 2.0, overhead = 0.0;
        for (double j=0; j<X/C; j++) {
            min = fmin(min, overhead + X/(2.0+F*j));
            overhead += C / (2.0+F*j);
        }
        cout.precision(7);
        cout << "Case #" << i << ": " << fixed << min << endl;
    }
}