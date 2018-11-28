#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
using namespace std;

int tt, tc;
double c, f, x;

int main() {
    cin >> tt;
    for (int tc = 1; tc <= tt; tc++) {
        cin >> c >> f >> x;

        double minn = 100000;
        double t1 = 0, tmp;
        for (int i = 0; i < 1000000; i++) {
            tmp = t1 + x / (2 + f * i);
            t1 += c / (2 + f * i);

            if (tmp < minn)
                minn = tmp;
        }
        printf("Case #%d: %.9lf\n", tc, minn);
    }

}
