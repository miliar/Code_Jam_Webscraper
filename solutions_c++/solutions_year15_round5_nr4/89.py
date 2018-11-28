#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <cassert>

using namespace std;

void
process(int id)
{
    int p;
    cin >> p;
    vector< int > e(p), f(p);
    for (int i = 0; i < p; ++i) {
        cin >> e[i];
    }
    int sum = 0;
    for (int i = 0; i < p; ++i) {
        cin >> f[i];
        sum += f[i];
    }
    int n = 1;
    while ((1 << n) < sum) ++n;
    assert((1 << n) == sum);
    vector< int > ans;
    for (int i = 0; i < n; ++i) {
        vector< int > new_e, new_f;
        int min_pos = (f[0] == 1) ? 1 : 0;
        int next_val = e[min_pos];
        ans.push_back(next_val);
        int cnt = f.size();
        int l = cnt - 1, r = cnt - 1;
        while (r >= 0) {
            while (f[r]) {
                while (e[l] != e[r] - next_val) {
                    --l;
                }
                if (new_e.empty() || new_e.back() != e[l]) {
                    new_e.push_back(e[l]);
                    new_f.push_back(0);
                }
                new_f.back()++;
                f[l]--;
                f[r]--;
            }
            --r;
        }
        e = new_e;
        f = new_f;
        reverse(e.begin(), e.end());
        reverse(f.begin(), f.end());
    }
    cout << "Case #" << id << ":";
    for (auto x : ans) {
        cout << ' ' << x;
    }
    cout << '\n';
}

int
main()
{
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        process(i + 1);
    }
    return 0;
}
