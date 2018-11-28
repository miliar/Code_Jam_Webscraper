#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <iomanip>

using namespace std;

int main() {
        
    int TC;
    cin >> TC;
    for (int tc = 1; tc <= TC; tc++) {
        
        cout << "Case #" << tc << ": ";
        int N;
        double V, X, R1, C1, R2, C2;
        cin >> N >> V >> X >> R1 >> C1;
        if (N == 1) {
            if (X == C1) {
                //cout << setprecision(50) << V/R1;
                printf("%.9f", V/R1);
            } else {
                cout << "IMPOSSIBLE";
            }
        } else if (N == 2) {
            cin >> R2 >> C2;
            double ratio1 = (X-C2)/(C1-C2);
            double ratio2 = 1 - ratio1;
            //double ratio2 = (X-C1)/(C2-C1);
            if (X == C1 && X == C2) {
                printf("%.9f", V/(R1+R2));
            } else if (X == C1) {
                printf("%.9f", V/R1);
            } else if (X == C2) {
                printf("%.9f", V/R2);
            } else if (C1 > X && C2 < X || C1 < X && C2 > X/*ratio1 >= 0 && ratio2 >= 0 && C1 != C2*/) {
                //cout << setprecision(50) << max(ratio1*V/R1, ratio2*V/R2);
                printf("%.9f", max(ratio1*V/R1, ratio2*V/R2));
            } else {
                cout << "IMPOSSIBLE";
            }
        }
        cout << endl;
    }

    return 0;
}
