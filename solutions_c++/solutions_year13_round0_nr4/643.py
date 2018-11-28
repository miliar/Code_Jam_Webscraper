#include <algorithm>
#include <iostream>
#include <sstream>
#include <vector>

#include <cassert>

using namespace std;

constexpr int X = 15;

int cnt;
int key_cnt[1500111][201];
bool v[1500111];

bool dfs(vector<int>& s, const vector<int>& needed, int state, int remaining)
{
    //cerr << state << endl;
    assert(state < 1500111);
    assert(state >= 0);
    if (v[state]) return false;
    v[state] = true;
    if (remaining == 0) return true;
    for (int i = 0; i < needed.size(); ++i) {
        if ((state / (1 << i)) % 2) continue;
        assert(needed[i] < 25);
        if (key_cnt[state][needed[i]]) {
            if (dfs(s, needed, state + (1 << i), remaining - 1)) {
                s.push_back(i);
                return true;
            }
        }
    }
    return false;
}

string solve()
{
    int k, n;
    cin >> k >> n;
    vector<int> s;
    vector<int> needed(n, -1);
    vector<vector<int> > a(n, vector<int>(200, 0));

    for (int i = 0; i < n; ++i) key_cnt[0][i] = 0;

    for (int i = 0; i < k; ++i) {
        int t;
        cin >> t;
        --t;
        ++key_cnt[0][t];
    }

    for (int i = 0; i < n; ++i) {
        int ti, ki;
        cin >> ti >> ki;
        --ti;
        needed[i] = ti;
        for (int j = 0; j < ki; ++j) {
            int t;
            cin >> t;
            --t;
            ++a[i][t];
        }
    }

    v[0] = false;
    for (int i = 1; i < (1 << n); ++i) {
        v[i] = false;
        int x = 0;
        while (x < n && !((i/(1 << x))%2)) ++x;
        assert(x != n);
        for (int j = 0; j < 200; ++j) {
            key_cnt[i][j] = key_cnt[i - (1 << x)][j] + a[x][j] - (needed[x] == j);
        }
    }

    if (dfs(s, needed, 0, n)) {
        stringstream r;
        reverse(s.begin(), s.end());
        for (auto& x: s) ++x;
        for (auto&& x: s) r << x << " ";
        string result = r.str();
        result.pop_back();
        return result;
    }
    return "IMPOSSIBLE";
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cnt = i;
        cout << "Case #" << i << ": " << solve() << endl;
    }
    return 0;
}
