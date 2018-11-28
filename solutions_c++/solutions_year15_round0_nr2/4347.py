#include <bits/stdc++.h>
using namespace std;
struct scanner {
    template <class T>
    inline operator T() { T a; cin >> a; return a; }
    inline auto operator() () -> scanner { return scanner(); }
    template <class C>
    auto operator() (C const& c) -> C { C r(c.size()); for (auto& i : r) cin >> i; return r; }
} sc;

auto main() -> int {
    int const T = sc;
    for (auto t = 1; t <= T; t++) {
        int const D = sc;
        auto const& P = sc(vector<int>(D));
        int res = 1e9;
        for (auto i = 1; i <= 10; i++) {
            auto const Del = accumulate(begin(P), end(P), 0,
                    [i](int d, int n) { return d+(n-1)/i; });
            res = min(res, i+Del);
        }
        cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}
