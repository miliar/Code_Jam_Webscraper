#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solve2(long long m1, long long h1, long long m2, long long h2) {
    if (m1 == m2) {
        return 0;
    }
    return h2 * m2 + (360 - h1) * m1 >= 2 * 360 * m2 ? 1 : 0;
}

int main() {
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        vector< pair< int, int > > hikers;
        int n;
        cin >> n;
        for (int i = 0; i < n; ++i) {
            int d, h, m;
            cin >> d >> h >> m;
            for (int j = 0; j < h; ++j) {
                hikers.push_back(make_pair(m + j, d));
            }
        }
        sort(hikers.rbegin(), hikers.rend());
        auto ans = 0;
        if (hikers.size() > 1) {
            ans = solve2(hikers[0].first, hikers[0].second, hikers[1].first, hikers[1].second);
        }
        cout << "Case #" << t << ": " << ans << "\n";
    }
    return 0;
}
