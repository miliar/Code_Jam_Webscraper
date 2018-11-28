#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <list>
#include <iterator>
#include <sstream>
#include <cmath>
#include <iomanip>
#include <cstdio>

using namespace std;

typedef vector<int> vi;
typedef vector<double> vd;

int main() {
    int T;
    cin >> T;
    for (int cs=1; cs<=T; ++cs) {
        double r = 2.0;
        double t = 0;
        double c, f, x;
        cin >> c >> f >> x;
        if (x<=c) {
            t = x/r;
            printf("Case #%d: %.7f\n", cs, t);
            continue;
        }
        int k = floor(x/c - r/f);
        for (int j=0; j<k; ++j) {
            t += c/r;
            r += f;
        }
        t += x/r;
        printf("Case #%d: %.7f\n", cs, t);
    }
}
