#include <iostream>
#include <iomanip>

using namespace std;
const long double EPS =  1e-9;

long double abs(long double a) {
    return a < 0 ? -a : a;
}

long double r[1005];
long double c[1005];

int T, N;
long double V, X;

int main() {
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cin >> N >> V >> X;

        for(int i = 0; i < N; i++) {
            cin >> r[i] >> c[i];
        }

        long double ans;
        //cerr << "Starting\n";
        if(N == 1) {
            //cerr << "Only one\n";

            if(abs(c[0] - X) < EPS) {
                ans = V/r[0];
            } else {
                ans = -1;
            }
        } else {
            // Two ins
            if(abs(c[0] - c[1]) < EPS) {
                //cout << "Same temp\n";
                if(abs(c[0] - X) < EPS) {
                    long double newR = r[0] + r[1];
                    ans = V/newR;
                } else {
                    ans = -1;
                }
            } else {
                // Different temps
                long double v0 = V*X - V*c[1];
                v0 /= (c[0] - c[1]);
                long double v1 = V - v0;
                
//                cout << "Volumes are " << v0 << " and " << v1 << "\n";

                if(v0 < -EPS || v1 < -EPS) {
                    ans = -1;
                } else {
                    ans = max(v0/r[0], v1/r[1]);
                }
            }
        }
        
        cout << "Case #" << t << ": ";
        if(ans < 0) {
            if(N == 2) {
                long double l = min(c[0], c[1]);
                long double r = max(c[0], c[1]);
                if(l < X && X < r) {
                    // Yey
                    cout << t << " messed up\n";
                }
            }
            cout << "IMPOSSIBLE";
        } else {
            cout << fixed << setprecision(15) << ans;
        }
        cout << "\n";
    }
    return 0;
}
