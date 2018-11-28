#include <array>
#include <cassert>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <random>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

void solve(int64_t k, int64_t c, int64_t s) {
    if (s * c < k) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }

    vector<int64_t> pows;
    pows.reserve(c+1);
    pows.push_back(1);
    for (int i = 1; i <= c; ++i) {
        pows.push_back(pows.back() * k);
    }

    for (int64_t deduced = 0; deduced < k; ) {
        int64_t loc = 0;
        for (int i = 0; i < c; ++i) {
            auto p = min(deduced, k-1);
            deduced++;
            loc += p * pows[c-1-i];
        }
        assert(loc < pows.back());
        cout << " " << (loc+1);
    }
    cout << endl;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        int k, c, s;
        cin >> k >> c >> s;
        cout << "Case #" << (i+1) << ":";
        solve(k, c, s);
    }
    return 0;
}
