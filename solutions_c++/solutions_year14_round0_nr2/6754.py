#include <cstdio>
#include <iostream>
#include <fstream>
using namespace std;

#define INF (0x3f3f3f3f)


int main() {

    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);

    int tests;
    double c, f, x;

    cin >> tests;
    for(int t = 1; t <= tests; t++) {
        cin >> c >> f >> x;
        double rate = 2, time = 0;
        double sol = x / rate;
        for(int numf = 0; sol > time; numf++) {      
            sol = min(sol, time + x / rate);
            time += c / rate;
            rate += f;
        }
        
        printf("Case #%d: %.8lf\n", t, sol);
    }


    return 0;
}
