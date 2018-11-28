#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int n;
double v, x;
double r[100], c[100];
pair<double, double> t[100];

const double eps = 1e-9;

void solve() {
    cin >> n >> v >> x;
    bool pm = false, mm = false;
    double r_min = 1e9;
    for (int i = 0; i < n; ++i) {
        cin >> r[i] >> c[i];
        c[i] -= x;
        t[i] = make_pair(c[i], r[i]);
        r_min = min(r_min, r[i]);
    }
    sort(t, t + n);
    if (t[0].first > eps || t[n - 1].first < -eps) {
        cout << "Impossible";
        return;
    }
    int min_z = 0, max_z = n;
    while (t[min_z].first < -eps) {
        min_z++;
    }
    while (t[max_z - 1].first > eps) {
        max_z--;
    }
    double R = 0, Rm = 0, Rp = 0, Cm = 0, Cp = 0;
    for (int i = min_z; i < max_z; ++i) {
        R += t[i].second;
    }
    for (int i = 0; i < min_z; ++i) {
        Rm += t[i].second;
        Cm += t[i].second * t[i].first;
    }
    for (int i = max_z; i < n; ++i) {
        Rp += t[i].second;
        Cp += t[i].second * t[i].first;
    }
    if (Cp < -Cm) {
        for (int i = 0; i < n; ++i) {
            t[i].first = -t[i].first;
        }
        reverse(t, t + n);
        swap(min_z, max_z);
        max_z = n - max_z;
        min_z = n - min_z;
        swap(Cp, Cm);
        Cp = -Cp, Cm = -Cm;
        swap(Rp, Rm);
    }
    for (int i = n - 1; i >= max_z; --i) {
        if (Cp - t[i].second * t[i].first >= -Cm) {
            Rp -= t[i].second;
            Cp -= t[i].second * t[i].first;
        } else {
            Rp -= (Cp + Cm) / t[i].first;
            Cp = -Cm;
            break;
        }
    }
    cout << fixed << setprecision(10) << v / (R + Rp + Rm);
}

int main() {
    cin.tie(NULL);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }
}
