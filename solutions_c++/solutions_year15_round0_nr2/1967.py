#include <algorithm>
#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::max;
using std::vector;
using std::min;

int main() {
    int T;
    cin >> T;

    for (int iter = 1; iter <= T; ++iter) {
        int d;
        cin >> d;

        vector<long long> a(d);
        long long res = 0;
        for (int i = 0; i < d; ++i) {
            cin >> a[i];
            res = max(res, a[i]);
        }

        int m = res;

        for (int border = 1; border <= m; ++border) {
            long long cur_res = 0;
            for (int i = 0; i < d; ++i) {
                if (a[i] > border) {
                    cur_res += a[i] / border - 1;

                    if (a[i] % border) {
                        ++cur_res;
                    }
                }
            }

            res = min(res, border + cur_res);
        }

        cout << "Case #" << iter << ": " << res << "\n";
    }

    return 0;
}
