#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <iomanip>
using namespace std;

#define rep(i,n) for(int i=0; i<n; i++)

int main(){
    int T;
    cin >> T;
    rep(n, T) {
        double C, F, X;
        cin >> C >> F >> X;
        double cps = 2.0;
        double time = X / cps;
        double add = C / cps;
        double nTime = X / (cps+F) + add;
        while( time > nTime ) {
            time = nTime;
            cps += F;
            add += C / cps;
            nTime = X / (cps+F) + add;
        }
        cout << "Case #" << (n+1) << ": ";
        cout << fixed << setprecision(8) << time << endl;
    }
    return 0;
}
