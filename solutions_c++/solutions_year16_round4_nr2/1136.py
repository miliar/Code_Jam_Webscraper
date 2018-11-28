/* Task solution for GCJ 2016
 * Tested with GCC 4.8.4
 * Build command line:
 *  g++ -std=gnu++11 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>

using namespace std;

const int MAX_N = 200;

int n, k, k2;
double p[MAX_N];
bool u[MAX_N + 1];
double a[MAX_N / 2 + 1];
double ans;

static void um() {
    a[0] = 1.0;
    for (int i = 1; i <= k2; ++i) {
        a[i] = 0.0;
    }
    for (int i = 0; i < n; ++i) {
        if (u[i]) {
            double py = p[i];
            double pn = 1 - p[i];
            for (int j = k2; j; --j) {
                a[j] = a[j] * pn + a[j - 1] * py;
            }
            a[0] *= pn;
        }
    }
    double t = a[k2];
    if (t > ans) {
        ans = t;
    }
}

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    for (int T = 1; T <= TN; T++) {
        cin >> n >> k;
        k2 = k / 2;
        ans = 0;
        for (int i = 0; i < n; ++i) {
            cin >> p[i];
            u[i] = (i < k);
        }
        u[n] = false;
        um();
        for (;;) {
            int i = 0, j = 0;
            while (!u[i]) {
                ++i;
            }
            while (u[i + 1]) {
                u[i] = false;
                u[j] = true;
                ++i;
                ++j;
            }
            if (i + 1 == n) {
                break;
            }
            u[i] = false;
            u[i + 1] = true;
            um();
        }
        cout << "Case #" << T << ": " << ans << endl;
    }
    return 0;
}
