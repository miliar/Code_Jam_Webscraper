#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <functional>
#include <cstdint>
#include <cmath>
#include <unordered_set>
#include <unordered_map>
#include <sstream>

#define D(x) x

using namespace std;

const double INPUT_EPS = 1e-5;

int main() {
    int numCases;
    cin >> numCases;

    for (int testCase = 1; testCase <= numCases; testCase++) {
        int N;
        double V, X;
        cin >> N >> V >> X;

        double result;
        bool impossible = false;

        if (N == 1) {
            double R1, C1;
            cin >> R1 >> C1;

            if (abs(C1 - X) < INPUT_EPS) {
                result = V / R1;
            } else {
                impossible = true;
            }
        } else {
            // N == 2
            double R1, C1, R2, C2;
            cin >> R1 >> C1 >> R2 >> C2;

            if (abs(C1-C2) < INPUT_EPS) {
                if (abs(C1 - X) < INPUT_EPS) {
                    result = V / (R1+R2);
                } else {
                    impossible = true;
                } 
            } else {
                double t1 = (C2-X)/(C2-C1)*V/R1;
                double t2 = (X-C1)/(C2-C1)*V/R2;
                if (t1 < 0 || t2 < 0) {
                    impossible = true;
                } else {
                    result = max(t1, t2);
                }
            }
        }

        cout << "Case #" << testCase << ": ";
        cout << fixed << setprecision(7);
        if (impossible) {
            cout << "IMPOSSIBLE";
        } else {
            cout << result;
        }
        cout << endl;
    }
}
