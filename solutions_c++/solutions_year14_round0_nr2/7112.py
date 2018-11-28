#include <iostream>
#include <fstream>
#include <limits>
#include <iomanip>
#include <vector>

using namespace std;


int main(){
    ifstream cin ("B-large.in");
    ofstream cout("B-large.out");
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++){
        double c, f, x;
        cin >> c >> f >> x;
        double r = x/2.0d;
        double a = 0;
        for (int i = 0; i < 10000000; i++){
            double seconds = 2.0f + i*f;
            double c1 = c/seconds;
            double c2 = x/seconds;

            a += c1;
            double dd = min(a + x/(2.0f+(i+1)*f), a+c2);
            r = min(dd, r);
        }

        cout << "Case #" << t << ": " << fixed << setprecision(7) << r << endl;
    }
    return 0;
}
