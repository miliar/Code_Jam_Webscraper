#include <bits/stdc++.h>
using namespace std;

int t, n, r, p, s;

bool check(string st) {
    int a = 0, b = 0, c = 0;
    for (int i = 0; i < st.length(); i++) {
        if (st[i] == 'R') a++;
        if (st[i] == 'S') b++;
        if (st[i] == 'P') c++;
    }
    if (a != r || b != s || c != p) return 0;
    return 1;
}

string nex(string st) {
    string ret = "";
    for (int i = 0; i < st.length(); i++) {
        if (st[i] == 'R') ret += "RS";
        if (st[i] == 'P') ret += "PR";
        if (st[i] == 'S') ret += "PS";
    }
    return ret;
}

void sortstr(string& s) {
    if (s.length() == 1) return ;
    string ex = s.substr(0, s.length() / 2), ex2 = s.substr(s.length() / 2);
    sortstr(ex);
    sortstr(ex2);
    if (ex < ex2) s = ex + ex2;
    else s = ex2 + ex;
}

int main(void) {
    if (fopen("a-small.in", "r")) {
        freopen("a-small.in", "r", stdin);
        freopen("a-small.out", "w", stdout);
    }
    if (fopen("a-large.in", "r")) {
        freopen("a-large.in", "r", stdin);
        freopen("a-large.out", "w", stdout);
    }
    cin >> t;
    for (int ii = 1; ii <= t; ii++) {
        cin >> n >> r >> p >> s;
        string arr[3] = {"R", "P", "S"};
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 3; j++) arr[j] = nex(arr[j]);
        }
        for (int i = 0; i < 3; i++) sortstr(arr[i]);
        sort(arr, arr + 3);
        bool done = 0;
        for (int i = 0; i < 3 && !done; i++) {
            if (check(arr[i])) {
                cout << "Case #" << ii << ": " << arr[i] << "\n";
                done = 1;
            }
        }
        if (!done) cout << "Case #" << ii << ": IMPOSSIBLE\n";
    }
    return 0;
}
