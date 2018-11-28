#include <iostream>
#include <stdio.h>
#include <memory.h>

using namespace std;

double c, f, x, res;


void solve() {
    double time_f, tmp;

    res = x/2; time_f = 0;
    for (int i=1; i<=x+1; i++) {
        time_f += c/(2 + (i-1)*f);
        tmp = time_f + x/(2+i*f);

        if (tmp > res) break;
        res = tmp;
    }
}

int main() {
    int i, num_test;
    
    cin >> num_test;
    for (i=1; i<=num_test; i++) {
        cin >> c >> f >> x;
        solve();
        printf("Case #%d: %.7f\n", i, res);
    }    

    return 0;
}
