#include <iostream>

#include <set>
#include <algorithm>

#include <cassert>

using namespace std;

int N;
double B0[1005], B1[1005];

pair<int, int> solve() {
    cin >> N;
    for (int i = 0; i < N; ++i) cin >> B0[i];
    for (int i = 0; i < N; ++i) cin >> B1[i];

    sort(B0, B0+N);
    sort(B1, B1+N);

    int deceit = 0;
    for (int i = 0; i < N; ++i) {
        if (B0[i] > B1[deceit]) ++deceit;
    }

    int fair = 0;
    set<double> S1(B1, B1+N);
    for (int i = 0; i < N; ++i) {
        auto it = S1.lower_bound(B0[i]);
        if (it == S1.end()) {
            ++fair;
            S1.erase(S1.begin());
        } else {
            S1.erase(it);
        }
    }

    assert(deceit >= fair);
    return {deceit, fair};
}

int T;
int main() {
    cin >> T;
    for (int tc = 1; tc <= T; ++tc) {
        auto p = solve();
        cout << "Case #" << tc << ": " << p.first << " " << p.second << "\n";
    }
    return 0;
}
