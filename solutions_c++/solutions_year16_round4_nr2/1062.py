#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;
    cout << fixed << setprecision(20);

    for (int tst = 0; tst < T; tst++) {
        cout << "Case #" << tst + 1 << ": ";

        int n, k;
        cin >> n >> k;
        vector <double> p(n);

        for (int i = 0; i < n; i++) {
            cin >> p[i];
        }
        double out = 0;

        for (int i = 0; i < (1 << n); i++) {
            if (__builtin_popcount(i) == k) {
                vector <double> res;

                for (int j = 0; j < n; j++) {
                    if ((i >> j) & 1) {
                        res.push_back(p[j]);
                    }
                }
                double sum = 0;

                for (int j = 0; j < (1 << k); j++) {
                    if (__builtin_popcount(j) == k / 2) {
                        double now = 1;

                        for (int x = 0; x < k; x++) {
                            if ((j >> x) & 1) {
                                now *= res[x];
                            } else {
                                now *= (1 - res[x]);
                            }
                        }
                        sum += now;
                    }
                }
                out = max(out, sum);
            }
        }
        cout << out;
        cout << '\n';
        cout.flush();
    }
}
