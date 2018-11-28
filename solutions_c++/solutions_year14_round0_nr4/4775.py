#include <iostream>
#include <cassert>
#include <vector>
#include <algorithm>

#define N 100000

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int ca = 1; ca <= T; ca++) {
        int n;
        cin >> n;
        vector<int> a, b;
        double t;
        for (int i = 0; i < n; i++) {
            cin >> t;
            a.push_back((int)(N * t));
        }
        sort(a.begin(), a.end());
        for (int i = 0; i < n; i++) {
            cin >> t;
            b.push_back((int)(N * t));
        }
        b.push_back(N);
        sort(b.begin(), b.end());
        vector<pair<int, int>> v;
        int last = 0;
        for (auto i : b) {
            v.push_back(make_pair(i, i - last - 1));
            last = i;
        }
        int ans = 0;
        for (auto i : a) {
            if (i > v[0].first && v.back().second > 0) {
                v.back().second--;
                ans++;
                int t = v[0].second;
                v.erase(v.begin());
                v[0].second += t;
            } else {
                int j;
                for (j = v.size()-2; j >= 0 && v[j].second == 0; j--);
                assert(j >= 0);
                int t = v[j].second - 1;
                v.erase(v.begin() + j);
                v[j].second += t;
            }
        }
        cout << "Case #" << ca << ": " << ans;
        b.pop_back();
        ans = 0;
        for (auto i : a) {
            if (b.back() < i) {
                ans++;
                b.erase(b.begin());
            } else {
                for (int j = 0; j < n; j++) {
                    if (b[j] > i) {
                        b.erase(b.begin() + j);
                        break;
                    }
                }
            }
        }
        cout << " " << ans << "\n";
    }
    return 0;
}
