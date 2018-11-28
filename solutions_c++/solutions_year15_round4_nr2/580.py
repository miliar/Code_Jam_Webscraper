#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <deque>
#include <sstream>
#include <iomanip>
using namespace std;
#define rep(i,n) for (int i = 0; i < (int)(n); i++)
typedef long long ll;
typedef pair <int, int> PII;
const int N = 105;
const double eps = 1e-6;
double R, C;
double r[N], c[N];

int sgn(double x) {
    if (x < -eps) return -1;
    if (x > eps) return 1;
    return 0;
}

int main() {
    int Tc, n;
    cin >> Tc;
    rep (ri, Tc) {
        cin >> n >> R >> C;
        rep (i, n) {
            cin >> r[i] >> c[i];
        }
        printf("Case #%d: ", ri + 1);
        double ans = 1e100;
        rep (i, n) {
            if (sgn(c[i] - C) == 0) {
                ans = min(ans, R / r[i]);
            }
        }
        rep (i, n) {
            rep (j, n) if (i != j && c[i] != c[j]) {
                double need = R * C;
                double a = c[i];
                double b = c[j];
                double x = (R * C - b * R) / (a - b);
                double y = R - x;
                //cout << "Enter\n";
                if (x >= 0 && y >= 0) {
                    ans = min(ans, max(x / r[i], y / r[j]));
                } 
            } else if (i != j && c[i] == c[j] && c[i] == C) {
                ans = min(ans, R / (r[i] + r[j]));
            }
        }
        if (ans > 1e50) {
            puts("IMPOSSIBLE");
        } else {
            printf("%.12f\n", ans);
        }
    }
}

