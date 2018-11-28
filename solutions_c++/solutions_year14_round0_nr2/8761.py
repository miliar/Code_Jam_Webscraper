#include <stdio.h>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int i, n;
double c, x, mna, cf, ct, f, t;
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> n;
    cout << fixed << setprecision(7);
    for (i = 1; i <= n; i++) {
        cin >> c >> f >> x;
        mna = x / 2;

        cf = 2;
        ct = 0;
        while (1) {
            ct += c / cf;
            cf += f;
            t = ct + x / cf;
            if (mna > t) {
                mna = t;
            }
            else{
                break;
            }
        }
        cout << "Case #" << i <<": " << mna << endl;
    }
    return 0;
}
