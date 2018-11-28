#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using pii = pair<int, int>;

int p[3] = {1, 2, 0};
char ta[3] = {'P', 'R', 'S'};

void minim(vector<int> &cur) {
    int n = cur.size();
    for (int l = 1; l < n; l *= 2) {
        for (int i = 0; i < n; i += 2 * l) {
            for (int j = 0; j < l; ++j) {
                if (cur[i + j] < cur[i + l + j]) break;
                if (cur[i + j] > cur[i + l + j]) {
                    for (int t = 0; t < l; ++t) {
                        swap(cur[i + t], cur[i + l + t]);
                    }
                    break;
                }
            }
        }
    }
}

void upd(vector<int> &ans, vector<int> &cur) {
    if (cur.empty()) return;
    minim(cur);
    if (ans.empty()) ans = cur;
    for (int i = 0; i < ans.size(); ++i) {
        if (ans[i] < cur[i]) return;
        if (ans[i] > cur[i]) {
            ans = cur;
            return;
        }
    }
}

void Solve() {
    int a[3], b[3], t;
    scanf("%d%d%d%d", &t, &a[1], &a[0], &a[2]);
    t = 1 << t;
    vector<int> ans;
    for (int i = 0; i < 3; ++i) {
        for (int i = 0; i < 3; ++i) b[i] = 0;
        vector<int> cur(1, i);
        while (cur.size() < t) {
            vector<int> n;
            for (auto e : cur) {
                n.push_back(e);
                n.push_back(p[e]);
            }
            cur = n;
        }
        for (auto e : cur) {
            b[e]++;
        }
        for (int i = 0; i < 3; ++i) {
            if (b[i] != a[i]) {
                cur.clear();
            }
        }
        upd(ans, cur);
    }
    if (ans.empty()) {
        printf("IMPOSSIBLE\n");
    } else {
        for (auto e : ans) {
            printf("%c", ta[e]);
        }
        printf("\n");
    }
}

int main() {
    freopen("A.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t; scanf("%d", &t);
    for(int i = 1; i <= t; ++i) {
        printf("Case #%d: ", i);
        Solve();
    }
}
