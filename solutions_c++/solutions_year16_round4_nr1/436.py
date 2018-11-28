#include <bits/stdc++.h>

using namespace std;

int n, a[3];

const std::string str = "RPS";

void update(std::string& res, int winner) {
    vector<int> f[2];
    int x = 0;
    int y = 1;
    f[x].push_back(winner);
    for (int i = 0; i < n; ++i, swap(x, y)) {
        f[y].clear();
        for (int j = 0; j < (1 << i); ++j) {
            f[y].push_back(f[x][j]);
            f[y].push_back((f[x][j] + 2) % 3);
        }
    }

    vector<int> cnt(3, 0);
    for (int i = 0; i < (1 << n); ++i) {
        cnt[f[x][i]]++;
    }
    for (int i = 0; i < 3; ++i) {
        if (cnt[i] != a[i]) {
            return;
        }
    }
    std::string tmp_str = "";
    for (int i = 0; i < (1 << n); ++i) {
        tmp_str += str[f[x][i]];
    }
    for (int i = 0; i < n; ++i) {
        int len = (1 << i);
        std::string to_str = "";
        for (int j = 0; j + len + len - 1 < (1 << n); j += len * 2) {
            std::string a_str = tmp_str.substr(j, len);
            std::string b_str = tmp_str.substr(j + len, len);
            to_str += min(a_str, b_str);
            to_str += max(a_str, b_str);
        }
        tmp_str = to_str;
    }
    if (res == "") {
        res = tmp_str;
    } else {
        res = min(res, tmp_str);
    }
}

int main() {

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    cin >> T;

    for (int test = 1; test <= T; ++test) {
        cin >> n;
        for (int i = 0; i < 3; ++i) {
            cin >> a[i];
        }
        std::string res = "";
        update(res, 0);
        update(res, 1);
        update(res, 2);

        cout << "Case #" << test << ": " << (res == "" ? "IMPOSSIBLE" : res) << endl;
    }

    return 0;
}
