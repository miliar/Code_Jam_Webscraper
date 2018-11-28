#include <iostream>
#include <array>
#include <vector>
#include <unordered_map>
#include <set>
using namespace std;

array<int, 10> digit_count(int64_t i) {
    array<int, 10> ret;
    ret.fill(0);
    if (i == 0) {
        ret[0] += 1;
        return ret;
    }
    while (i != 0) {
        int64_t j = i / 10;
        int64_t d = i - 10*j;
        i = j;
        ret[d]++;
    }
    return ret;
}

int64_t solve(int64_t n) {
    array<int, 10> ds;
    ds.fill(0);
    int cds = 0;
    for (int i = 1; ; i++) {
        auto dns = digit_count(i * n);
        for (int j = 0; j < 10; ++j) {
            if (dns[j] > 0 && ds[j] == 0) {
                ds[j]++;
                cds++;
            }
        }
        if (cds == 10) return i * n;
    }
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        int n;
        cin >> n;
        if (n < 1) {
            cout << "Case #" << (i+1) << ": INSOMNIA" << endl;
        } else {
            auto ans = solve(n);
            cout << "Case #" << (i+1) << ": " << ans << endl;
        }
    }
    return 0;
}
