#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <string>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <utility>
#include <set>
#include <map>
#include <cctype>

#define FOR(i,n) for(long long int i=0; i<n; i++)
#define MP(a,b) make_pair(a,b)
#define PB(x) push_back(x)
#define SORT(a) sort(a.begin(), a.end())
#define REV(a) reverse(a.begin(), a.end())

#define COND(p,t,f) ((p)?(t):(f))

#define PI 3.14159265

using namespace std;
typedef long long int lint;
typedef unsigned long long int ulint;

bool eq(double x1, double x2) {
    return abs(x1-x2)<1e-7;
}

int main() {
    int T;
    cin >> T;
    FOR(t,T) {
        lint N;
        cin >> N;
        double V,X;
        cin >> V >> X;
        vector <double> R(N),C(N);
        FOR(i,N) cin >> R[i] >> C[i];
        cout << "Case #" << t+1 << ": ";

        if (N==2) {
            if ((C[0] < X && C[1] < X) || (C[0]>X && C[1] > X)) {
                cout << "IMPOSSIBLE" << endl;
            }
            else {
                if (eq(C[0],C[1])) {
                    N=1;
                    R[0]+=R[1];
                }
                else {
                    double v0 = (X*V - V*C[1])/(C[0]-C[1]);
                    double v1 = V-v0;
                    double t1 = v1/R[1];
                    double t0 = v0/R[0];
                    //cerr << v0 << " " << v1 << endl;
                    cout << fixed << setprecision(20) << max(t0,t1) << endl;

                }

            }
        }

        if (N==1) {
            if (eq(X,C[0])) cout << fixed << setprecision(20) << V/R[0] << endl;
            else cout << "IMPOSSIBLE" << endl;
        }



    }

}
