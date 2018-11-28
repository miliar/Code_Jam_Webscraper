#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <set>
#include <map>
#include <numeric>
#include <cstdio>
#include <cstring>
#include <iomanip>

using namespace std;

#define pb push_back
#define f first
#define s second
typedef long long ll;
typedef pair<int, int> pint;
typedef pair<long long, long long> plint;
typedef vector<int> vint;
typedef vector<vector<int>> vvint;
typedef vector<long long> vlint;
typedef vector<vector<long long>> vvlint;
typedef vector<pair<int, int>> vpint;
typedef vector<pair<long long, long long>> vplint;

ifstream in("D-small-attempt0.in");
ofstream out("output.txt");

typedef vector<map<char, int>> trie;

int add(trie &b, const string &str)
{
    int res = 0;
    int v = 0;
    for (char c : str) {
        auto it = b[v].find(c);
        if (it != b[v].end()) {
            v = it->second;
        } else {
            int w = b.size();
            b[v][c] = w;
            b.emplace_back();
            v = w;
            ++res;
        }
    }
    return res;
}

int check(int m, int n, const vint &t, const vector<string> &s)
{
    int res = n;
    vector<trie> tries(n, trie(1));
    for (int i = 0; i < m; ++i) {
        res += add(tries[t[i]], s[i]);
    }
    /*if (t == vint{0, 1, 1, 0}) {
        cerr << res << endl;
    }*/
    return res;
}

void go(int i, int m, int n, vint &t, vint &cnt, int &res_max, int &res_cnt, const vector<string> &s)
{
    if (i == m) {
        if (*min_element(cnt.begin(), cnt.end()) == 0) {
            return;
        }
        int res = check(m, n, t, s);
        if (res > res_max) {
            res_max = res;
            res_cnt = 1;
        } else if (res == res_max) {
            ++res_cnt;
        }
        return;
    }

    for (int v = 0; v < n; ++v) {
        t[i] = v;
        ++cnt[v];
        go(i + 1, m, n, t, cnt, res_max, res_cnt, s);
        --cnt[v];
    }
}

void solve()
{
    int m, n;
    in >> m >> n;
    vector<string> s(m);
    for (auto &str : s) {
        in >> str;
    }
    vint t(m, -1);
    vint cnt(n, 0);
    int res_max = -1, res_cnt = 0;
    go(0, m, n, t, cnt, res_max, res_cnt, s);
    out << res_max << " " << res_cnt;
}

int main()
{
    int cases;
    in >> cases;
    for (int z = 0; z < cases; ++z) {
        out << "Case #" << z + 1 << ": ";
        solve();
        out << endl;
    }

    return 0;
}
