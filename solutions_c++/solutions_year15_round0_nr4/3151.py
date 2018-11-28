#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <map>
#include <set>
#include <vector>
#include <cstdio>
#include <cstdint>
#include <sstream>
#include <cmath>

using namespace std;

//#define RELEASE

#ifndef RELEASE
    #define debug(...) fprintf(stderr, __VA_ARGS__)
#else
    #define debug(...)
#endif

int main(int argc, char** argv) {
    // Comment this out to use as: [exe] < input.in
    //freopen("input.in", "r", stdin);

    int T;
    cin >> T;
    cin.ignore();
    debug("T = %d\n", T);

    for (int TC=1; TC <= T; ++TC) {
        int X, R, C;
        cin >> X;
        cin >> R;
        cin >> C;
        cin.ignore();

        bool ok = true;
        while (true) {
            if ((R * C) % X != 0) {
                ok = false;
                break;
            }

            if (X > max(R,C)) {
                ok = false;
                break;
            }

            int aux1, aux2;
            aux1 = X - floor(X/2.0);
            aux2 = X - aux1 + 1;

            debug("Testcase #%d: X %d, R %d, C %d; maxX %d, minX %d, min(R,C) %d\n", TC, X, R, C, max(aux1, aux2), min(aux1, aux2), min(R, C));

            if (min(aux1, aux2) > min(R, C)) {
                ok = false;
                break;
            }

            if (min(R, C) < X-1) {
                ok = false;
                break;
            }

            break;
        }

        string solution;
        if (ok) {
            solution = "GABRIEL";
        } else {
            solution = "RICHARD";
        }

        printf("Case #%d: %s\n", TC, solution.c_str());
        debug("Case #%d: %s\n", TC, solution.c_str());
    }

    return 0;
}