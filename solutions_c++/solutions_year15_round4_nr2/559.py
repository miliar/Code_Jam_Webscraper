#include "../../lib/include.h"

bool cmp(const pair<double,double> &a, const pair<double,double> &b) {
    if (abs(a.second - b.second) > 1e-9)
        return a.second < b.second;
    return a.first < b.first;
}

struct solver {

    solver() {
    }

    void solve(bool process, istream &cin, ostream &cout) {

        int n;
        cin >> n;
        double V, X;
        cin >> V >> X;

        vector<pair<double, double> > streams;
        for (int i = 0; i < n; i++) {
            double r, c;
            cin >> r >> c;
            streams.push_back(make_pair(r, c));
        }

        LOGIC;

        sort(all(streams), cmp);

        double mn = INFINITY;
        for (int i = 0; i < n; i++) {
            if (abs(streams[i].second - X) < 1e-9) {
                mn = min(mn, V / streams[i].first);
            }
        }

        // double temp = 0.0;
        // for (int i = 0; i < n; i++) {
        //     temp += streams[i].first * streams[i].second;
        // }
        // double denom = 0.0;
        // for (int i = 0; i < n; i++) {
        //     denom += streams[i].first;
        // }
        // temp /= denom;

        // if (abs(temp - X) < 1e-9) {
        //     double rsum = 0.0;
        //     for (int i = 0; i < n; i++) {
        //         rsum += streams[i].first;
        //     }

        //     mn = min(mn, V / rsum);
        // }


        if (size(streams) == 2) {
            double R1 = streams[0].first,
                C1 = streams[0].second,
                R2 = streams[1].first,
                C2 = streams[1].second;

            if ((C1 > X && C2 > X) || (C1 < X && C2 < X)) {

            } else if (abs(C1 - X) < 1e-9 && abs(C2 - X) < 1e-9) {

                mn = min(mn, V / (R1 + R2));

            } else {
                // double lo = 0,
                //     hi = 1e18;

                // for (int it = 0; it < 1000; it++) {
                //     double x2 = (lo + hi) / 2.0;
                //     // double x1 = (X * x2 * R2 - x2 * R2 * C2) / (R1 * C1 - X * R1);
                //     double x1 = (V - x2 * R2) / R1;
                //     double heat = (x1 * R1 * C1 + x2 * R2 * C2) / V;
                //     if (heat < X) {
                //         lo = x2;
                //     } else {
                //         hi = x2;
                //     }
                // }

                // double x2 = lo;
                // double x1 = (V - x2 * R2) / R1;

                // mn = min(mn, max(x1, x2));

                // x1 = (V - x2 * R2) / R1;
                // R1 * (x1 * R1 * C1 + x2 * R2 * C2) / (V - x2 * R2) = X
                // (V * C1 - x2 * R2 * C1 + x2 * R2 * C2) / (V - x2 * R2) = X / R1
                // V * C1 - x2 * R2 * C1 + x2 * R2 * C2 = X * (V - x2 * R2) / R1
                // V * C1 - x2 * R2 * C1 + x2 * R2 * C2 = X * V / R1 - X * x2 * R2 / R1
                // x2 * (- R2 * C1 + R2 * C2 + X * R2 / R1) = X * V / R1 - V * C1


                double denom = ((C1 - C2)*R2);

                // double denom = - R2 * C1 + R2 * C2 + X * R2 / R1;
                // assert(abs(denom) > 1e-9);
                if (abs(denom) > 1e-9) {
                    double x2 = (C1*V - V*X)/denom;
                    /* double x2 = (X * V / R1 - V * C1) / denom; */
                    double x1 = (V - x2 * R2) / R1;
                    // assert(abs((x1 * R1 + x2 * R2) - V) < 1e-9);
                    // assert(abs(((x1 * R1 * C1 + x2 * R2 * C2) / V) - X) < 1e-9);
                    mn = min(mn, max(x1, x2));
                }
            }
        }

        OUTPUT;

        if (std::isinf(mn)) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << setprecision(10) << fixed << mn << endl;
        }

    }
};

// see https://github.com/SuprDewd/GoogleCodeJamRunner
#include "../../lib/gcj.h"
