#include <bits/stdc++.h>

using namespace std;

class node {
    public:
    int j, p, s;
    node (int _j = 0, int _p = 0, int _s = 0) : j(_j), p(_p), s(_s) {};
};

int cnt[33][33];
int resMask, res;

vector <node> v;


int T, J, P, S, K;

void attempt(int index, int cur, int mask) {
    if (index == v.size()) {
        if (cur > res) {
            res = cur;
            resMask = mask;
        }
        return;
    }

    attempt(index + 1, cur, mask);

    if (cnt[v[index].j][v[index].p + J] + 1 <= K && cnt[v[index].j][v[index].s + J + P] + 1 <= K && cnt[v[index].p + J][v[index].s + J + P] + 1 <= K) {
        cnt[v[index].j][v[index].p + J]++; cnt[v[index].j][v[index].s + J + P]++; cnt[v[index].p + J][v[index].s + J + P]++;
        attempt(index + 1, cur + 1, mask | (1 << index));
        cnt[v[index].j][v[index].p + J]--; cnt[v[index].j][v[index].s + J + P]--; cnt[v[index].p + J][v[index].s + J + P]--;
    }
}

void solve() {
    resMask = 0; res = 0;
    v.clear();
    for (int i = 0; i < J; ++i)
    for (int j = 0; j < P; ++j)
    for (int k = 0; k < S; ++k)
        v.push_back(node(i, j, k));
    memset(cnt, 0, sizeof cnt);

    attempt(0, 0, 0);
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> J >> P >> S >> K;
        solve();
        cout << "Case #" << t <<": " << res << endl;
        for (int i = 0; i < v.size(); ++i)
            if (resMask & (1 << i))
                cout << v[i].j + 1 <<" "<<v[i].p + 1 <<" " << v[i].s + 1 << endl;
    }
}
