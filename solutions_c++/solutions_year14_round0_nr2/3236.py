#include <iostream>
#include <set>
#include <algorithm>
#include <iterator>
#include <iomanip>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    cout << fixed << setprecision(7);
    for(int t=1; t<=T; ++t) {
        cout << "Case #" << t << ": ";

        double C, F, X;
        cin >> C >> F >> X;
        int n = max(0.,(X*F-2*C)/C/F);
        double res = X/(2+n*F);
        for(int i=0; i<n; ++i)
            res += C/(2+i*F);
        cout << res;

        cout << endl;
    }
}
