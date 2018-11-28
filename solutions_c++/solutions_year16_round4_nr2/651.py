#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int t;
int n, k;
double p[20];

void solve(int x) {
    cin >> n >> k;
    for (int i = 0; i < n; i++) cin >> p[i];
    double pu = 0;
    for (int b = 0; b < (1<<n); b++) {
        if (__builtin_popcount(b) != k) continue;
        vector<double> u;
        for (int i = 0; i < n; i++) {
            if (b&(1<<i)) u.push_back(p[i]);
        }
        double uu = 0;
        for (int z = 0; z < (1<<k); z++) {
            if (__builtin_popcount(z) != k/2) continue;
            double pp = 1;
            for (int i = 0; i < k; i++) {
                if (z&(1<<i)) {
                    pp *= u[i];
                } else {
                    pp *= (1-u[i]);
                }
            }
            uu += pp;
        }
        pu = max(pu,uu);
    }
    printf("Case #%i: %.12f\n", x, pu);
}

int main() {
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
}
