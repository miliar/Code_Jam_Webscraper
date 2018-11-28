#include <bits/stdc++.h>

using namespace std;
/*
const int n = 16;
const int j = 50;

void solve(long long x, int curN = 0) {

}
*/

long long t, k, c, s;

long long sumK;

inline long long getIndex(long long i) {
    // always i-th block, in the end - min(i+1, k)-th symbol
    return sumK * i + min(i + 1, k - 1);
}

int main() {
// #ifndef KEKMDA
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
// #endif
    cin >> t;
    t++;
    vector<long long> ans;
    vector<bool> checked;
    for (int tc = 1; tc < t; ++tc) {
        cin >> k >> c >> s;
        cout << "Case #" << tc << ": ";
        if (c == 1 || s == k) {
            if (s < k) {
                cout << "IMPOSSIBLE\n";
            } else {
                for (int i = 0; i < k; ++i) {
                    cout << i + 1 << " ";
                }
                cout << "\n";
            }
            continue;
        }
        sumK = 0;
        for (int i = 1; i < c; ++i) {
            sumK += pow(k, c - i);
        }
        ans.clear();
        checked.resize(k + 5, false);
        for (int i = 0; i < k; i += 2) {
            ans.push_back(getIndex(i) + 1);
        }
        if (ans.size() > s) {
            cout << "IMPOSSIBLE\n";
        } else {
            for (auto t : ans) {
                cout << t << " ";
            }
            cout << "\n";
        }
    }
    return 0;
}
