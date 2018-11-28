#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

double solve() {
    double c, f, x;
    cin >> c >> f >> x;
    int r = int(x/c);
    double ans = x/2.0;
    double d[100010];
    for (int i = 0; i <= r; ++i) {
        d[i] = c/(2+i*f);
        if (i > 0) {
            d[i] += d[i-1];
        }
    }
    for (int i = 0; i <= r; ++i) {
        ans = min(ans, d[i] + x/(2+(i+1)*f));
    }
    return ans;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        printf("Case #%d: %.7f\n", i, solve());
    }
    return 0;
}
