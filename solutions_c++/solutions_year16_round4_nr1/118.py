#include <bits/stdc++.h>

using namespace std;

const char *who = "RPS";

string get_order(string s) {
    if (s.size() == 1) return s;
    string L = get_order(s.substr(s.size() / 2));
    string R = get_order(s.substr(0, s.size() / 2));
    if (L < R) {
        return L + R;
    } else {
        return R + L;
    }
}

string check(int start, int n, int tot[]) {
    vector<int> win;
    win.push_back(start);
    for (int i = 0; i < n; ++i) {
        vector<int> new_win;
        for (int j = 0; j < win.size(); ++j) {
            int a = win[j], b = (win[j] + 2) % 3;
            new_win.push_back(a);
            new_win.push_back(b);
        }
        win = new_win;
    }
    int b[3];
    for (int i = 0; i < 3; ++i) b[i] = 0;
    for (int i = 0; i < win.size(); ++i) {//cerr << win[i] << ' ';
        b[win[i]]++;
    }
    //cerr << endl;
    for (int i = 0; i < 3; ++i) if (b[i] > tot[i]) return "";
    string ret = "";
    for (int i = 0; i < win.size(); ++i) ret += who[win[i]];
    ret = get_order(ret);
    return ret;
}

void solve() {
    int N, a[3];
    cin >> N;
    for (int i = 0; i < 3; ++i) cin >> a[i];
    string ret = "";
    for (int i = 0; i < 3; ++i) {
        string win = check(i, N, a);
        if (win.size() > 0 && (ret == "" || ret > win)) {
            ret = win;
        }
    }
    cout << (ret.size() > 0 ? ret : "IMPOSSIBLE") << endl;
}

int main() {
    int testCount;
    cin >> testCount;
    for (int testId = 1; testId <= testCount; ++testId) {
        printf("Case #%d: ", testId);
        solve();
        fflush(stdout);
        fprintf(stderr, "%d = %.15f\n", testId, clock() / (double) CLOCKS_PER_SEC);
    }
}

