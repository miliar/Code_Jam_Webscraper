#include <iostream>

using namespace std;

int main () {
    int cases;
    double c,f,x,a,b;
    cin >> cases;
    for (int caseno = 1; caseno <= cases; caseno++) {
        cout << "Case #" << caseno << ": ";
        cin >> c >> f >> x;
        a = x/2.0;
        for (int n=1;;n++) {
            b = a - x/((n-1)*f+2) + c/((n-1)*f+2) + x/(n*f+2);
            if (b>a) break;
            a = b;
        }
        cout.precision(7);
        cout << fixed << a << endl;
    }
}