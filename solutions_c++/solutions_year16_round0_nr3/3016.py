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

void solve(int n, int j) {
    vector<int64_t> g;
    g.reserve(n);
    vector<int64_t> ds;
    ds.reserve(9);
    unordered_set<int64_t> gs;

    for (int _j = 0; _j < j; ++_j) {
        TRY:
        g.clear();
        ds.clear();

        // randomly generate g
        g.push_back(1);
        for (int i = 0; i < n-2; ++i) g.push_back(rand() % 2);
        g.push_back(1);

        // determine the representations and divisors for each base
        for (int b = 2; b <= 10; ++b) {
            int64_t m = 1;
            int64_t r = 0;
            for (int i = n-1; i >= 0; --i, m *= b) {
                r += m * g[i];
            }

            // avoid duplicates
            if (b == 2) {
                if (gs.count(r)) goto TRY;
                gs.insert(r);
            }

            for (int d = 11; d < 10000; ++d) {
                if (r % d == 0) {
                    ds.push_back(d);
                    break;
                }
            }
            if (ds.size() != b - 1) goto TRY;
        }

        assert(ds.size() == 9);

        for (int i = 0; i < g.size(); ++i) {
            cout << g[i];
        }
        for (int i = 0; i < ds.size(); ++i) {
            cout << " " << ds[i];
        }
        cout << endl;
    }
}

int main() {
    srand(time(0));
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        int n, j;
        cin >> n >> j;
        cout << "Case #" << (i+1) << ":" << endl;
        solve(n, j);
    }
    return 0;
}
