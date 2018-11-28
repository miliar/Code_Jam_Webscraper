#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

class Solver {
public:
    double C, F, X;
    int T, curTest;
    void getData() {
        cin >> C >> F >> X;
    }
    void solve() {
        int k = max(0, (int)((X * F - 2 * C) / (C * F)));
        //cout << "k = " << k << endl;
        //return;
        double t = 0;
        for(int i = 1; i <= k; i++) {
            double curT = t + 1.0 * C / (2 + F * (i - 1));
            t = curT;
        }
        double result = t + 1.0 * X / (2 + F * k);
        printf("Case #%d: %.7lf\n", curTest, result);
    }
    void run() {
        cin >> T;
        for(int i = 0; i < T; i++) {
            curTest = i + 1;
            getData();
            solve();
        }
    }
};
int main()
{
    //freopen("input.txt", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    Solver* s = new Solver();
    s->run();
    return 0;
}
