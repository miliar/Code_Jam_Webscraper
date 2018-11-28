#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

const int MAXN = 110;
const long double EPS = 1e-7;

int T;
int n;
long double V, X;
long double R[MAXN], C[MAXN];

long double Abs(long double x) {
    return x > 0 ? x : -x;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    cout.precision(10);
    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        cin >> n >> V >> X;
        for (int i = 0; i < n; ++i)
            cin >> R[i] >> C[i];
        if (n == 1) {
            if (Abs(X - C[0]) < EPS)
                cout << fixed << V / R[0] << endl;
            else
                cout << "IMPOSSIBLE" << endl;
        } else {
            bool find = false;
            double ans = 0;
            if (Abs(X - C[0]) < EPS && Abs(X - C[1]) >= EPS)
                ans = V / R[0], find = true;
            if (Abs(X - C[1]) < EPS && Abs(X - C[0]) >= EPS)
                ans = V / R[1], find = true;
            if (Abs(X - C[0]) < EPS && Abs(X - C[1]) < EPS)
                ans = V / (R[0] + R[1]), find = true;
            
            if (find)
                cout << fixed << ans << endl;
            else {
                double temp21 = C[1] - C[0];
                double tempx1 = X - C[0];
                if (Abs(temp21) < EPS)
                    cout << "IMPOSSIBLE" << endl;
                else {
                    double v2 = V * tempx1 / temp21;
                    double v1 = V - v2;
                    if (v1 < 0 || v2 < 0)
                        cout << "IMPOSSIBLE" << endl;
                    else {
                        ans = max(v1 / R[0], v2 / R[1]);
                        cout << fixed << ans << endl;
                    }
                }
            }
        }
    }
    return 0;
}
