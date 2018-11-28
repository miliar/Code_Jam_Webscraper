#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    cout << fixed << setprecision(10);
    for (int testCase = 0; testCase < T; ++testCase) {
        int n, k;
        cin >> n >> k;
        vector<long double> p(n);
        for (auto &e: p) {
            cin >> e;
        }
        vector<bool> v(n);
        fill(begin(v) + n - k, end(v), true);
        vector<bool> vhalf(k);
        fill(begin(vhalf) + k - k/2, end(vhalf), true);
        long double ans = 0;
        do {
            long double p_k = 0;
            do {
                long double p_cur = 1.0l;
                int i_cur = 0;
                for (int i = 0; i < n; ++i) {
                    if (v[i]) { // in comittee
                        if (vhalf[i_cur]) { // votes yes
                            p_cur *= p[i];
                        } else {
                            p_cur *= 1.0l - p[i];
                        }
                        i_cur++;
                    }
                }
                p_k += p_cur;
            } while (next_permutation(begin(vhalf), end(vhalf)));
            if (p_k > ans) {
                ans = p_k;
            }
        } while (next_permutation(begin(v), end(v)));
        cout << "Case #" << testCase + 1 << ": " << ans << endl;
    }
    return 0;
}
