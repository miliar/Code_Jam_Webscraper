#include <iostream>
#include <cstdio>
using namespace std;

void solve() {
    double C, F, X, delt = 2;
    cin >> C >> F >> X;
    double base = 0, remain = X / delt;
    while (1) {
        double _base, _remain, _delt;
        _base = base + C / delt;
        _delt = delt + F;
        _remain = X / _delt;
        if (_base + _remain < base + remain) {
            base = _base;
            remain = _remain;
            delt = _delt;
        } else {
            printf("%.8lf\n", base + remain);
            return;
        }
    }
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        solve();
    }
        
}
