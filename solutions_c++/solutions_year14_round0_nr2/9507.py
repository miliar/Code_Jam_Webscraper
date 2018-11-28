#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;



int main() {

    int numDataSets;
    double c, f, x, t0, t1;
    cin >> numDataSets;
    for(int iSet = 0; iSet < numDataSets; ++iSet) {
        cin >> c >> f >> x;
        t0 = x / 2.0;
        t1 = c / 2.0 + x / (2.0 + f);
        int k = 0;
        while(t0 > t1 && k <= 50001) {
            ++k;
            t0 = t1;
            t1 = t1 - x / (2.0 + k * f) + c / (2.0 + k * f) + x / (2.0 + (k + 1) * f);
        }
        printf("Case #%d: %.7f\n", iSet + 1, t0);
    }
    return 0;
}
