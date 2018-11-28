#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++)

using namespace std;

int test;
double c, f, x, res;

double Count(int n) {
    int cnt = 0;
    double res = 0.0;
    double cps = 2.0;
    while (cnt <= n) {
        if (cnt == n) {
            res += x/cps;
            return res;
        }
        res += c/cps;
        cps += f;
        cnt++;
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &test);
    FOR(T, 1, test) {
        cin >> c >> f >> x;
        res = 123456789.0;
        int cnt = 0;
        FOR(numberOfFactory, 0, 10000) {
            double Time = Count(numberOfFactory);
            res = min(res, Time);
            if (cnt == 0 && Time < res) cnt++;
            if (cnt == 1 && Time > res) break;
        }
        printf("Case #%d: %.7lf\n", T, res);
    }
    return 0;
}

