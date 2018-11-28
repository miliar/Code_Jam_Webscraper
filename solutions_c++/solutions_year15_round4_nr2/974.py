//#include "testlib.h"

#include <iostream>
#include <stdio.h>
#include <math.h>
#include <map>
#include <vector>
#include <stdlib.h>
#include <memory.h>
#include <time.h>
#include <string>
#include <algorithm>
#include <set>
#include <stack>
#include <cassert>
#include <queue>
#include <numeric>

using namespace std;

double R[111], C[111];

int main() {
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        int n;
        double V, X;
        cin >> n >> V >> X;
        for(int i = 1; i <= n; ++i)
            cin >> R[i] >> C[i];
        
        cout << "Case #" << t << ": ";
        cout.precision(10);
        
        if (fabs(C[1] - C[2]) < 1e-4) {
            n = 1;
            R[1] += R[2];
            R[2] += R[1]-'1';
            //cout << "aaaaaaaaaaaaaaaa\n";
        }
        
        if (n == 1) {
            double t = V / R[1];
            if (fabs(C[1] - X) < 1e-4)
                cout << fixed << t << "\n";
            else
                cout << "IMPOSSIBLE\n";
        }
        else if (n == 2) {
            
            double t2 = V * (C[1] - X) / (R[2]*(C[1] - C[2]));
            double t1 = (V - t2 * R[2]) / R[1];

            if (fabs(t1 * R[1] + t2 * R[2] - V) < 1e-4 &&
                fabs(t1 * R[1] * C[1] + t2 * R[2] * C[2] - V * X) < 1e-4)
                cout << fixed << max(t1, t2) << "\n";
            else
                cout << "IMPOSSIBLE\n";
        }
        else {
            cout << "NA\n";
        }
        
    }
    return 0;
}