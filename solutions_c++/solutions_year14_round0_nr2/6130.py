#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <math.h>
#include <ctype.h>
#include <algorithm>
#include <utility>
using namespace std;

typedef long long ll;

double solve(double c, double f, double x) {
    double curres, preres = 1000000000, pre = 0, cur, rate = 2;
    while (1) {
        cur = c / rate + pre;
        curres = x / rate + pre;

        if (curres > preres) break;

        rate += f;
        preres = curres;
        pre = cur;
    }
    return preres;
}

int main(void) {
    int t;
    double c, f, x, res;
    cin.sync_with_stdio(false);
#if 0
    freopen("input.in", "r", stdin);
    freopen("output.out", "w+", stdout);
#endif
    cin >> t;
    for (int test = 1; test <= t; test++) {
        cin >> c >> f >> x;

        res = solve(c, f, x);

        printf("Case #%d: %.7f\n", test, res);
        //cout << "Case #" << test << ": " << val << "\n";
    }
    return 0;
}