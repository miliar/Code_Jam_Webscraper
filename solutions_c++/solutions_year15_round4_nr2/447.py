#include <iostream>
#include <cstdio>
#include <memory.h>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

double eps = 1e-9;
typedef pair<double, double> pdd;

#define NAME "b"

void solve() {
	static int test;
    cerr << "test " << test + 1 << endl;
	double res = 1e100;
    int N;
    double NEED, X;
    cin >> N >> NEED >> X;

    vector<pdd> W(N);
    cerr << "X " << X << endl;
    cerr << "NEED " << NEED << endl;
    for (int i = 0 ; i < N; ++i) {
        cin >> W[i].second >> W[i].first;
        cerr << W[i].second << ' ' << W[i].first << endl;
    }

    sort(W.begin(), W.end());

    if (W[0].first - eps > X || W.back().first + eps < X) {
        cout << "Case #" << ++test << ": " << "IMPOSSIBLE" << endl;
        cerr << "Case #" << test << ": " << "IMPOSSIBLE" << endl;
        return;
    }

    for (int it = 0; it < 2; ++it) {

        double T = W[0].first * W[0].second;
        double V = W[0].second;

        cerr << N << endl;

        for (int i = 1; i < N; ++i) {
            double XX = T - V * X;
            double TT = T + W[i].first * W[i].second;
            double VV = V + W[i].second;

            if (fabs(XX) < eps) {
                if (fabs(W[i].first - X) < eps) {
                    T = TT; V = VV;
                    continue;
                } else {
                    break;
                }
            }

            if (XX < 0) {
                if (TT < VV * X) {
                    T = TT; V = VV; continue;
                } else {
                    double delta = fabs(XX / (TT - VV * X - XX));
                    V = V + W[i].second * delta;
                    T = T + W[i].first * delta * W[i].second;
                }
            }

            if (XX > 0) {
                if (TT > VV * X) {
                    T = TT; V = VV; continue;
                } else {
                    double delta = fabs(XX / (TT - VV * X - XX));
                    V = V + W[i].second * delta;
                    T = T + W[i].first * delta * W[i].second;
                }
            }
        }


        if (fabs(T / V / X - 1)  < eps)
            res = min(res, NEED / V);
        cerr << T / V / X << endl;

        reverse(W.begin(), W.end());
    }
    cerr << "output " << res << endl;
    cout.precision(10);
    cout << fixed;
	cout << "Case #" << ++test << ": " << res << endl;
	cerr << "Case #" << test << ": " << res << endl;
}

int main() {
    freopen(NAME".in", "r", stdin);
    freopen(NAME".out", "w", stdout);

	int t;
	cin >> t;
	while (t --> 0)
		solve();
	return 0;
}
