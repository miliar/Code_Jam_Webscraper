#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <string>
#include <string.h>
#include <sstream>
#include <stdlib.h>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

int main() {
    int _T;
    scanf("%d\n", &_T);

    for (int _ = 1; _ <= _T; _++) {
        printf("Case #%d: ", _);
        cout.precision(15);
        cout << fixed;

        double c, f, x;
        cin >> c >> f >> x;

        if (x <= c) {
            cout << x / 2 << endl;
            continue;
        }

        double result = x / 2;
        double v = 2;
        double curtime = 0;
        int iter = 500;
        while (true) {
            double need = c / v;
            curtime += need ;
            v += f;
            if (curtime + x / v <= result) {
                result = curtime + x / v;
            }
            else {
                --iter;
                if (iter < 0) break;
            }
        }

        cout << result << endl;
    }
    
    return 0;
}
