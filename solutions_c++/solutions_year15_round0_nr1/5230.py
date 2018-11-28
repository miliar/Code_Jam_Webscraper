#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

struct scanner {
    template <class T>
    inline operator T() { T a; cin >> a; return a; }
    inline scanner operator() () { return scanner(); }
} sc;

int main() {
    int const T = sc;
    for (auto t = 1; t <= T; t++) {
        int const SMax = sc;
        string const S_ = sc;
        vector<int> s;
        transform(begin(S_), end(S_), back_inserter(s),
                [](char n) -> int { return n-'0'; });
        auto const N = accumulate(begin(s), end(s), 0);
        auto res = -1;
        for (auto i = 0; i <= SMax; i++) {
            auto cnt = i;
            for (auto j = 0; j < SMax+1; j++)
                if (cnt >= j) cnt += s[j];
            if (cnt == N+i) {
                res = i;
                break;
            }
        }
        cout << "Case #" << t << ": " << res << endl;
    }
	return 0;
}
