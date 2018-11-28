#include <iostream>
#include <set>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    double C, F, X;

    cin >> T;
    for (int i = 0 ; i < T; ++i) {
        cin >> C >> F >> X;

        double t = 0.0;
        double points = 0.0;
        double performance = 2.0;

        while(true) {
            double t1 = X / performance; // Without new building 
            double t2 = C / performance + X / (performance + F); 

            if (t1 < t2) {
                //cout << "Do not build" << endl;
                t += t1;
                break;
            } else {
                //cout << "Build " << t << endl;
                t += C / performance;
                performance += F;
            }
        }

        cout << fixed << setprecision(9) << "Case #" << i + 1 << ": " << t << endl;
    }
}
