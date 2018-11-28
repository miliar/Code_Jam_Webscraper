#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;


void solve() {
    double c, f, x, k = 0, t = 0;
    double ans = -1;
    cin >> c >> f >> x;
    while (1) {
        double tmp =  x / (2.0 + k) + t;
        if (ans < 0 || ans > tmp)
            ans = tmp;
        else break;
        t += c / (2 + k);
        k += f;
    }
    printf("%.6f\n", ans);

}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        solve();
    }


}

