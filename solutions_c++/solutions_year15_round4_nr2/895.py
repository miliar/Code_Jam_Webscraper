#include <bits/stdc++.h>
using namespace std;

const double EQ = 1e-8;

int main () {
    int t;
    cin >> t;
    for (int qq = 1; qq <= t; ++qq) {
        int n;
        double v, x;
        cin >> n >> v >> x;
        deque<pair<double, double>> hot, cold;
        double flow = 0;
        for (int i = 0; i < n; ++i) {
            double r, c;
            cin >> r >> c;
            if (fabs(c - x) < EQ) flow += r;
            else if (c < x) {
                cold.push_back({c,r});
            } else {
                hot.push_back({c,r});
            }
        }
        sort(begin(hot), end(hot), greater<pair<double, double>>());
        sort(begin(cold), end(cold), less<pair<double, double>>());

        cerr << " = " << flow << endl;
        while (cold.size() && hot.size()) {
            double &c0 = cold[0].first;
            double &r0 = cold[0].second;
            double &c1 = hot[0].first;
            double &r1 = hot[0].second;

            double p = (c1 - x) / (x - c0); // cold / hot
            if (r1*p < r0 + EQ) {
                // use hot
                flow += r1*(p+1);
                r0 -= r1*p;
                cerr << " h " << flow << " " << r1 << " " << r1*p << endl;
                hot.pop_front();
                if (r0 < EQ) cold.pop_front();
            } else {
                // use cold
                flow += r0*(1 + 1/p);
                r1 -= r0/p;
                cerr << " c " << flow << " " << r0/p << " " << r0 << endl;
                cold.pop_front();
                r1 -= r1*p;
                if (r1 < EQ) hot.pop_front();
            }
        }

        cout << "Case #" << qq << ": ";
        if (flow > 0) cout << fixed << setprecision(10) << v / flow << endl;
        else cout << "IMPOSSIBLE" << endl;
    }

    return 0;
}
