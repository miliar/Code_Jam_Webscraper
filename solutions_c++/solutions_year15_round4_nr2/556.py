#include <cstdio>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

const long double eps = 1e-9;

void solve() {
    int n;
    long double v, x;
    cin >> n >> v >> x;
    
    vector<long double> r(n), c(n);
    for (int i = 0; i < n; i++) {
        cin >> r[i] >> c[i];
    }
    
    if (n == 1) {
        if (fabs(x - c[0]) < eps) {
            printf("%0.9Lf", v / r[0]);
        }
        else {
            printf("IMPOSSIBLE");
        }
    }
    else if (n == 2) {
        if (x > max(c[0], c[1]) + eps || x < min(c[0], c[1]) - eps) {
            printf("IMPOSSIBLE");
        }
        else if (fabs(c[0] - c[1]) < eps) {
            printf("%0.9Lf", v / (r[0] + r[1]));
        }
        else {
            printf("%0.9Lf", max(v * (x - c[1]) / ((c[0] - c[1]) * r[0]), v * (x - c[0]) / ((c[1] - c[0]) * r[1])));
        }
    }
    else {
        printf("WHAT?");
    }
}

int main(){
#ifndef ONLINE_JUDGE
    freopen("B-small-attempt4.in.txt", "rt", stdin);
//    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    
    int t;
    cin >> t;
    
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
    
}
