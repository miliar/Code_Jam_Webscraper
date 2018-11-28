#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;

long double calc(int n, long double c, long double f, long double x) {
    long double t = 0;
    for (int i = 1; i <= n; i++) {
        t += c / (2 + (i - 1) * f);
    }
    t += x / (2 + max(n, 0) * f);
    return t;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int T;
    cin >> T;
    for (int task = 1; task <= T; task++) {
        long double c, f, x;
        cin >> c >> f >> x;
        int n = (f * (x - c) - c * 2) / (c * f) + 1;
        long double t1 = calc(n - 1, c, f, x);
        long double t2 = calc(n, c, f, x);
        long double t3 = calc(n + 1, c, f, x);
        /*
        if (min(t1, t3) < t2) {
            cout << "error" << endl;
        }
        */
        printf("Case #%d: %.7lf\n", task, min(min(t1, t2), t3));
    }
    
    return 0;
}
