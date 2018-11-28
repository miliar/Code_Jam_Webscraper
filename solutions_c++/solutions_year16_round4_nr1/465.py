#include <bits/stdc++.h>

using namespace std;

const int maxn = 1000;

long double a[maxn];

string error = "IMPOSSIBLE";

int n;

string get(int r, int p, int s) {
    if (r + p + s == 1) {
        if (r == 1)
            return "R";
        if (p == 1)
            return "P";
        if (s == 1)
            return "S";
    }
    int aa = p + r - s;
    if (aa < 0 || aa % 2 == 1) {
        return error;
    }
    int np = aa / 2;
    int bb = r + s - p;
    if (bb < 0 || bb % 2 == 1) {
        return error;
    }
    int nr = bb / 2;
    int cc = p + s - r;
    if (cc < 0 || cc % 2 == 1) {
        return error;
    }
    int ns = cc / 2;
    string sub = get(nr, np, ns);
    if (sub == error)
        return error;
    string ret = "";
    for (auto x : sub) {
        if (x == 'R') {
            ret.push_back('R');
            ret.push_back('S');
        }
        if (x == 'S') {
            ret.push_back('S');
            ret.push_back('P');
        }
        if (x == 'P') {
            ret.push_back('R');
            ret.push_back('P');
        }
    }
    return ret;
}

void solve() {
    int n;
    cin >> n;
    int r, p, ss;
    cin >> r >> p >> ss;
    string tmp = get(r, p, ss);
    if (tmp == error) {
        cout << tmp << endl;
        return;;
    }
    int m = tmp.size();
    string s = tmp;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j += (1 << (i + 1))) {
            int fi = j;
            int se = fi + (1 << i);
            if (se >= m)
                break;
            bool need = false;
            for (int le = 0; le < (1 << i); le++) {
                if (s[fi + le] < s[se + le])
                    break;
                if (s[fi + le] > s[se + le]) {
                    need = true;
                    break;
                }
            }
            if (need) {
                for (int le = 0; le < (1 << i); le++) {
                    swap(s[fi + le], s[se + le]);
                }
            }
        }
    }
    cout << s << endl;
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    int test;
    cin >> test;
    for (int id = 1; id <= test; id++) {
        cout << "Case #" << id << ": ";
        solve();
    }
    return 0;
}