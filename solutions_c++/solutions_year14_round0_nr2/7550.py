#include <iostream>
#include <stdio.h>

using namespace std;

int main() {
    int n = 0, p = 0;
    double c = 0, f = 0, x = 0, best, fab, sum1, sum2;
    cin >> p;
    for (int i = 0; i < p; i++) {
        cin >> c;
        cin >> f;
        cin >> x;
        sum1 = 0;
        sum2 = 0;
        fab = 0;
        n = -1;
        best = x / 2;
        while (true) {
            n++;
            sum1 = fab + x / (2 + n * f);
            fab = fab + c / (2 + n * f);
            sum2 = fab + x / (2 + (n + 1) * f);
            if (sum1 > sum2) {
                continue;
            } else {
                best = sum1;
                break;
            }
        }
        printf("Case #%d: %.7f\n", i+1, best);
    }

    return 0;
}