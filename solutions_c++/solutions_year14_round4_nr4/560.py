#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdio>

using namespace std;

const int md = 1e9 + 7;

map<int, int> z;

int build_trie(vector<string> & cur) {
    if (cur.size() == 0)
        return 0;
/*    cerr << "______________________________" << endl;
    for (int i = 0; i < cur.size(); ++i) {
        cerr << cur[i] << endl;
    }*/
    sort(cur.begin(), cur.end());
    int ans = cur[0].size() + 1;

    for (int i = 1; i < cur.size(); ++i) {
        bool flag = true;
        for (int j = 0; j < cur[i].size(); ++j) {
            if (j >= cur[i - 1].size() || cur[i][j] != cur[i - 1][j])
                flag = false;
            if (!flag)
                ++ans;
        }
    }
//    cerr << ans << endl;
    return ans;
}

int calc_nodes(int m, int n, vector<int> & b, vector<string> & a) {
    int ans = 0;
    for (int j = 1; j <= n; ++j) {
        vector<string> cur;
        for (int i = 0; i < m; ++i)
            if (b[i] == j)
                cur.push_back(a[i]);
        ans += build_trie(cur);
    }
    return ans;
}

void go(int m, int n, vector<int> b, vector<string> & a) {
    bool flag = true;
    for (int i = 0; i < m; ++i)
        if (b[i] == 0) {
            flag = false;
            break;
        }
    if (flag) {
        int tmp = calc_nodes(m, n, b, a);
        if (z.find(tmp) == z.end())
            z[tmp] = 0;
        ++z[tmp];
        return;
    }

    for (int i = 0; i < m; ++i)
        if (b[i] == 0) {
            for (int j = 1; j <= n; ++j) {
                b[i] = j;
                go(m, n, b, a);
                b[i] = 0;
            }
            break;
        }
}

pair<int, int> solve(int m, int n, vector<string> & a) {
    z.clear();

    vector<int> b(m);
    go(m, n, b, a);
    pair<int, int> ans;
    map<int, int>::iterator it = z.end();
    --it;
    ans.first = it->first;
    ans.second = it->second;

    return ans;
}

int main() {
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int m, n;
        cin >> m >> n;
        vector<string> a(m);
        for (int i = 0; i < m; ++i)
            cin >> a[i];
        pair<int, int> ans = solve(m, n, a);
        printf("Case #%d: %d %d\n", test, ans.first, ans.second);
    }
    return 0;
}
