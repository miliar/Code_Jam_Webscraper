#include <iostream>
#include <climits>
#include <list>
#include <vector>
#include <algorithm>
using namespace std;

#define is_set(bit, mask) (((mask) & (1 << (bit))) != 0)

int solve(int r, int c, int n) {
    int rc = r * c;
    int result = INT_MAX;
    for (int mask = (1 << rc) - 1; mask >= 0; --mask) {
        int mask_n = 0;
        for (int i = 0; i < rc; ++i) {
            if (is_set(i, mask)) {
                mask_n += 1;
            }
        }
        if (mask_n != n) {
            continue;
        }
        int option = 0;
        for (int i = 0; i < rc; ++i) {
            if (!is_set(i, mask)) {
                continue;
            }
            // i = ir * c + ic
            auto ir = i / c;
            auto ic = i % c;
            if (ic + 1 < c && is_set(i + 1, mask)) {
                option += 1;
            }
            if (ir + 1 < r && is_set(i + c, mask)) {
                option += 1;
            }
        }
        result = min(result, option);
    }
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int r, c, n;
        cin >> r >> c >> n;
        cout << "Case #" << t << ": " << solve(r, c, n) << "\n";
    }
    return 0;
}
