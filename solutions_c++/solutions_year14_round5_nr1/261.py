#include <iostream>
#include <vector>

using namespace std;

int main() {

    int tc;

    cin >> tc;

    cout.setf(ios::fixed);
    cout.precision(15);

    for (int t = 1; t <= tc; t++) {
        int n, p, q, r, s;
        cin >> n >> p >> q >> r >> s;

        vector<int> v(n);
        vector<long long> sum(n+1);

        for (int i = 0; i < n; i++) {
            v[i] = (i * (long long)p + q) % r + s;
            sum[i+1] = sum[i] + v[i];
        }

        long long best = 0;

        for (int i = 0; i < n; i++) {
            best = max(best, min(sum[i], sum.back() - sum[i]));
        }

        for (int j = 2; j < n; j++) {
            int lo = 1, hi = j;

            while (hi - lo > 1) {
                long long mid = (lo + hi) / 2;

                long long op1 = sum[mid], op2 = sum[j] - sum[mid];

                if (op1 < op2)
                    lo = mid;
                else
                    hi = mid;
            }

            best = max(best, sum.back() - max(sum.back() - sum[j],
                                              max(sum[lo], sum[j] - sum[lo])));
            best = max(best, sum.back() - max(sum.back() - sum[j],
                                              max(sum[hi], sum[j] - sum[hi])));
        }

        cout << "Case #" << t << ": " << (best / (double)sum.back()) << '\n';
    }

    return 0;
}

