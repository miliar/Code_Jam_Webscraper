
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

#define rep(i,n) for (int i = 0; i < int(n); i++)
#define all(c) (c).begin(), (c).end()

int T;
long double C, F, X;

int main() {
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        cin >> C >> F >> X;
        long double p = 2, total = 0;
        while (true) {
            if (F*X-C*p < C*F) {
                total += X/p;
//                cout << "X/p = " << X/p << " ";
                break;
            } else {
                total += C/p;
//                cout << "C/p = " << C/p << " ";
                p += F;
            }
        }
//        cout << "\n";
        cout << fixed << setprecision(10) << total << endl;
    }
}
