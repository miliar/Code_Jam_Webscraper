#include <iostream>
#include <iomanip>

using namespace std;

int main() {
        freopen("C.in", "r", stdin);
        freopen("C.out", "w", stdout);
        int T;
        cin >> T;
        for (int i = 0; i < T; i ++) {
                double C, F, X;
                cin >> C;
                cin >> F;
                cin >> X;
                double rate = 2.0;
                double expec_t = X / rate;
                double start_t = C / rate;
                while ( ( start_t + X / (rate + F) ) < expec_t ) {
                        expec_t  = start_t + X / (rate + F);
                        rate = rate + F;
                        start_t = start_t + C / rate;
                }
                cout << std::fixed;
                cout << "Case #" << i + 1 << ": " << setprecision(7) << expec_t << endl;
        } 
        return 0;
}
