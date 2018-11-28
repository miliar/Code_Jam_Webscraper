#include <iostream>
#include <set>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <cassert>
#include <climits>
#include <cmath>
#include <ctime>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <deque>
#include <time.h>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <algorithm>
#include <bitset>

#define MYLOCAL

#pragma comment(linker, "/STACK:256000000")

using namespace std;

int main() {
#ifdef MYLOCAL
    freopen("/home/maks/input.txt", "rt", stdin);
    freopen("/home/maks/output.txt", "wt", stdout);
    clock_t beginTime = clock();
#endif

    int te;
    cin >> te;

    double c, f, x, v, t;

    for (int test = 0; test < te; test++) {
        v = 2, t = 0;
        cin >> c >> f >> x;

        double t1, t2;
        while (true) {
            t1 = x / v;
            t2 = c / v + x / (v + 4);

            if (t1 < t2) {
                t += t1;
                cout << "Case #" << test + 1 << ": ";
                printf("%.6lf", t);
                cout << endl;
                break;
            }
            t += c / v;
            v += 4;
        }

    }


#ifdef MYLOCAL
    cout << endl << "time: " << double(clock() - beginTime) / CLOCKS_PER_SEC;
#endif
    return 0;
}
