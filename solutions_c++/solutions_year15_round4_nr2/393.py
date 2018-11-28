#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

const double EPS = 1e-9;
const int MAXN = 111;

int n;
double v, x;
double r[MAXN], c[MAXN];
double a[2][MAXN];

double check(double t) {
    for (int it = 0; it < 2; it++) {
        double min_value = a[it][n];
        double max_value = a[it][n];
        for (int i = 2; i < n; i++) {
            if (fabs(a[it][i] ) < EPS) {
                continue;
            }

            if (a[it][i] > 0) {
                max_value += t * a[it][i];
            } else {
                min_value += t * a[it][i];
            }
        }
        min_value = max(min_value, 0.0);
        max_value = min(max_value, t);
        // cerr << t << " " << it << " " << min_value << " " << max_value << "\n";
        if (min_value > max_value) {
            return false;
        }
    }
    return true;
}

void solve() {
	cin >> n;
    cin >> v >> x;
    for (int i = 0; i < n; i++) {
        cin >> r[i] >> c[i];
        c[i] -= x;
    }

    bool flag = true;
    for (int i = 0; i < n; i++) {
        if (fabs(c[i] ) > EPS) {
            flag = false;
        }
    }

    if (flag) {
        double sr = 0.0;
        for (int i = 0; i < n; i++) {
            sr += r[i];
        }
        cout << v / sr << "\n";
        return;
    }

    if (n == 1) {
        cout << "IMPOSSIBLE\n";
        return;
    }
    
    for (int i = 0; i < n; i++) {
        a[0][i] = r[i] * c[i];
        a[1][i] = r[i]; 
    }
    a[0][n] = 0;
    a[1][n] = v;

    for (int it = 0; it < 2; it++) {

        int pos = it;
        for (int i = it; i < n; i++) {
            if (fabs(a[it][i] ) > fabs(a[it][pos] ) ) {
                pos = i;
            }
        }
        if (it < pos) {
            swap(a[0][it], a[0][pos] );
            swap(a[1][it], a[1][pos] );
        }
        double norm = a[it][it];
        for (int i = it; i <= n; i++) {
            a[it][i] /= norm;
        }
        double coef = -a[it ^ 1][it];
        for (int i = it; i <= n; i++) {
            a[it ^ 1][i] += coef * a[it][i];
        }
    }

    for (int it = 0; it < 2; it++) {
        for (int i = 2; i < n; i++) {
            a[it][i] = -a[it][i];
        }
    }

    /*double left = 0.0, right = 1e9;

    for (int it = 0; it < 200; it++) {
        double middle = 0.5 * (left + right);

        if (check(middle) ) {
            right = middle;
        } else {
            left = middle;
        }
    }*/

    if (a[0][n] >= 0.0 && a[1][n] >= 0.0) {
        cout << max(a[0][n], a[1][n] ) << "\n";
    } else {
        cout << "IMPOSSIBLE\n";
    }

    // cerr << "Left = " << left << "\n";
    // cerr << "Right = " << right << "\n";

    // if (left > 1e9 - 1e8) {
    //     cout << "IMPOSSIBLE\n";
    // } else {
    //     cout << left << "\n";
    // }
}

int main() {
    cout << fixed << setprecision(10);
	int cases; cin >> cases;
	for (int i = 0; i < cases; i++) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}