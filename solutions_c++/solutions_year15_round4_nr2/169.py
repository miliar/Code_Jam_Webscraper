#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

const double eps = 1e-10;

double lowest(const vector< pair<double, double> > &a, const vector<double> &vlim, double V) {
    int i = 0;
    double tot = 0;
    double v = V;
    while (V > 0 && i < (int) a.size()) {
        double t = min(V, vlim[i]);
        tot += t * a[i].first;
        V -= t;
        i++;
    }
    return tot / v;
}

double highest(const vector< pair<double, double> > &a, const vector<double> &vlim, double V) {
    int i = (int) a.size() - 1;
    double tot = 0;
    double v = V;
    while (V > 0 && i >= 0) {
        double t = min(V, vlim[i]);
        tot += t * a[i].first;
        V -= t;
        i--;
    }
    return tot / v;
}

int main() {
    int T;
    cin >> T;
    for (int cs = 1; cs <= T; ++cs) {
        int n;
        cin >> n;
        double V, X;
        cin >> V >> X;
        vector< pair<double, double> > a(n);
        for (int i = 0; i < n; ++i)
            cin >> a[i].second >> a[i].first;
        sort(a.begin(), a.end());

        bool fail = false;
        if (X < a[0].first || X > a.back().first)
            fail = true;

        double lo = 0, hi = 1e8;
        if (!fail) {
            for (int k = 0; k < 100; ++k) {
                double mid = (lo + hi) / 2;
                vector<double> vlim(n);
                double sum = 0;
                for (int i = 0; i < n; ++i) {
                    vlim[i] = a[i].second * mid;
                    sum += vlim[i];
                }
                if (sum + eps >= V && lowest(a, vlim, V) <= X + eps && highest(a, vlim, V) + eps >= X)
                    hi = mid;
                else
                    lo = mid;
            }
        }
        cout << "Case #" << cs << ": " << fixed << setprecision(8);
        if (fail)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << lo << endl;
    }
    return 0;
}
