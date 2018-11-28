#include <iostream>
#include <iomanip>

using namespace std;

int n, k, half;
double vals[17];
double all_yes[1 << 17];
double all_no[1 << 17];

int main() {
    int T;
    cin >> T;
    for (int case_num = 1; case_num <= T; ++case_num) {
        cin >> n >> k;
        half = k / 2;
        for (int i = 0; i < n; ++i) {
            cin >> vals[i];
        }
        all_yes[0] = 1;
        all_no[0] = 1;
        double ans = 0.0L;
        for (int mask = 1; mask < 1 << n; ++mask) {
            all_yes[mask] = 1;
            all_no[mask] = 1;
            for (int j = 0; j < n; ++j) {
                if (mask & (1 << j)) {
                    all_yes[mask] *= vals[j];
                    all_no[mask] *= (1 - vals[j]);
                }
            }

            if (__builtin_popcount(mask) == k) {
                double maskans = 0.0L;
                for (int submask = mask; submask > 0; submask = (submask - 1) & mask) {
                    if (__builtin_popcount(submask) == half) {
                        maskans += all_no[~submask & mask] * all_yes[submask];
                    }
                }

                ans = max(ans, maskans);
            }
        }

        cout << "Case #" << case_num << ": " << setprecision(10) << ans << '\n';
    }
    return 0;
}
