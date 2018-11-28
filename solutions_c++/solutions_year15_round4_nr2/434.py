//tonynater

#include <cmath>
#include <cstdio>
#include <iomanip>
#include <iostream>

using namespace std;

const double eps = 1e-9;

int N;

double V, X, R1, C1, R2, C2;

int main() {
    freopen("/Users/tonynater/Downloads/B-small-attempt0.in", "r", stdin);
    freopen("/Users/tonynater/Store/Computer/Xcode_repos/Miscellaneous/GCJ_2015/R2_B/r2_b_small.out", "w", stdout);
    
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    
    cout << fixed << setprecision(9);
    
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
        cin >> N >> V >> X >> R1 >> C1;
        
        cout << "Case #" << t+1 << ": ";
        if(N == 1) {
            if(abs(C1-X) < eps) {
                cout << V/R1 << '\n';
            }else {
                cout << "IMPOSSIBLE\n";
            }
        }else if(N==2) {
            cin >> R2 >> C2;
            if(C2 < C1) {
                double tmp = R1;
                R1 = R2;
                R2 = tmp;
                
                tmp = C1;
                C1 = C2;
                C2 = tmp;
            }
            
            if(C2 < X-eps || X+eps < C1) {
                cout << "IMPOSSIBLE\n";
            }else if(abs(C1-C2) < eps) {
                cout << V/(R1+R2) << '\n';
            }else {
                double t2 = (X*V-V*C1)/(R2*C2-R2*C1);
                double t1 = (V-R2*t2)/(R1);
                cout << max(t1,t2) << '\n';
            }
        }
    }
    
    return 0;
}