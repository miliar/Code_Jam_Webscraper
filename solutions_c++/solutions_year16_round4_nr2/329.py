#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

double ans;
vector <double> b;
int n, k, tests;
double a[210];
double f[210][210];

void update() {
    memset(f, 0, sizeof(f));
    f[0][0] = 1;
    for (int i = 0; i < k; ++ i) {
        for (int j = 0; j <= i; ++ j) {
            f[i + 1][j] += f[i][j] * (1 - b[i]);
            f[i + 1][j + 1] += f[i][j] * b[i];
        }
    }
    ans = max(ans, f[k][k / 2]);
}

int main() {
    cin >> tests;
    for (int cases = 1; cases <= tests; ++ cases) {
        ans = 0;
        cin >> n >> k;
        for (int i = 0; i < n; ++ i)
            cin >> a[i];
        sort(a, a + n);
        for (int i = 0; i + k - 1 < n; ++ i) {
            b.clear();
            for (int j = 0; j < k; ++ j) b.push_back(a[i + j]);
            update();
        }
        for (int i = 0; i < k; ++ i) {
            b.clear();
            for (int j = 0; j < i; ++ j) b.push_back(a[j]);
            for (int j = 0; j < k - i; ++ j) b.push_back(a[n - j - 1]);
            update();
        }
        printf("Case #%d: %.10f\n", cases, ans);
    }
    return 0;
}
