#include <iostream>
#include <cstdio>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <ctime>
#include <utility>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <ctime>

using namespace std;

typedef long long LL;
template<class T> inline T Abs(const T& x) { return x < 0 ? -x : x; }
template<class T> inline T Sqr(const T& x) { return x * x; }

#define double long double


const double eps = 1e-12;


bool ThatCase = false;


void Solution2() {
    int n;
    double V, X;
    cin >> n >> V >> X;
    if (n == 1) {
        double r, c;
        cin >> r >> c;
        if (Abs(c - X) > eps) {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
        printf("%.10Lf\n", V / r);
        return;
    }
    double r1, c1, r2, c2;
    cin >> r1 >> c1 >> r2 >> c2;
    if (c1 > c2) {
        swap(r1, r2);
        swap(c1, c2);
    }
    if (c1 > X + eps || c2 < X - eps) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    if (Abs(c1 - c2) <= eps) {
        printf("%.10Lf\n", V / (r1 + r2));
        return;
    }
    double v1 = (X * V - V * c2) / (c1 - c2);
    double v2 = V - v1;
    printf("%.10Lf\n", max(v1 / r1, v2 / r2));
}


void Solution() {
    int n;
    double V, X;
    cin >> n >> V >> X;
    vector<double> r(n), c(n);
    bool hasBig = false;
    bool hasSmall = false;
    for (int i = 0; i < n; ++i) {
        cin >> r[i] >> c[i];
        if (c[i] >= X - eps) {
            hasBig = true;
        }
        if (c[i] <= X + eps) {
            hasSmall = true;
        }
    }

    /*
    if (ThatCase) {
        cerr << n << " " << V << " " << X << endl;
        for (int i = 0; i < n; ++i) {
            cerr << r[i] << " " << c[i] << endl;
        }
    }
    */

    vector<pair<double, int>> tmp;
    for (int i = 0; i < n; ++i) {
        tmp.push_back(make_pair(c[i], i));
    }
    sort(tmp.begin(), tmp.end());
    vector<double> r1 = r, c1 = c;
    for (int i = 0; i < n; ++i) {
        int index = tmp[i].second;
        r[i] = r1[index];
        c[i] = c1[index];
    }
    if (!hasBig || !hasSmall) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }

    double tl = 0.0;
    double tr = 1e10;
    for (int iter = 0; iter < 200; ++iter) {
        double tt = (tl + tr) / 2;
        double v = V;
        double mn = 0.0;
        for (int i = 0; i < n; ++i) {
            double cv = r[i] * tt;
            cv = min(cv, v);
            v -= cv;
            mn += cv * c[i];
        }
        mn /= V;
        double mx = 0.0;
        v = V;
        for (int i = n - 1; i >= 0; --i) {
            double cv = r[i] * tt;
            cv = min(cv, v);
            v -= cv;
            mx += cv * c[i];
        }
        mx /= V;
        if (v <= eps && mn <= X + eps && mx >= X - eps) {
            tr = tt;
        } else {
            tl = tt;
        }
    }
    printf("%.10Lf\n", tr);
}


int main() {
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        float startTime = clock() / CLOCKS_PER_SEC;
        cout << "Case #" << i + 1 << ": ";
        Solution();
        float endTime = clock() / CLOCKS_PER_SEC;
        cerr << "Test #" << i + 1 << ": elapsed time is " << endTime - startTime;
        cerr << endl;
        ThatCase = false;
    }

    return 0;
}


