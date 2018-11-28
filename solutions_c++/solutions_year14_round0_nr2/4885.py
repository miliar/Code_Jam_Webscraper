#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

int main() {
    int T; cin >> T;
    for (int I = 1; I <= T; I++) {
        double result = 0;

        double c,f,x; cin >> c >> f >> x;
        result = x;
        int t = 0;
        while (1) {
            double y = 0;
            for (int i = 0; i < t; i++) {
                y += c / (2 + i*f);
            }
            y += x / (2+ f*t);
            if (y < result) {
                    result = y;
                    t++;
            } else {
                    break;
            }
        }
        printf("Case #%d: %.7lf\n", I, result);
    }
}
