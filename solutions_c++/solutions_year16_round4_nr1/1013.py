#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define all(x) begin(x), end(x)
typedef long long ll;

string f = "RPS";

int nn[333];

string built(int n, int a) {
    if (n == 0) {
        string s;
        s.push_back(f[a]);
        return s;
    }
    string aa = built(n - 1, a);
    string bb = built(n - 1, (a + 2) % 3);
    if (aa > bb) {
        swap(aa, bb);
    }
    return aa + bb;
}

map<vector<int>, string> m;

vector<int> getcnt(const string &s) {
    vector<int> cnt(3);
    for (auto c : s) {
        cnt[nn[c]]++;
    }
    return cnt;
}

int main() {
    srand(time(0));
    #define task "t"
    freopen(task".in", "r", stdin);
    freopen(task".out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < 3; i++) {
        nn[f[i]] = i;
    }

    for (int i = 0; i <= 12; i++) {
        for (int x = 0; x < 3; x++) {
            string s = built(i, x);
            m[getcnt(s)] = s;
        }
    }
    for (int ii = 0; ii < t; ii++) {
        int trash;
        cin >> trash;
        vector<int> cnt(3);
        for (auto &x : cnt) {
            cin >> x;
        }
        string ans = m[cnt];
        if (ans == "") {
            ans = "IMPOSSIBLE";
        }
        cout << "Case #" << ii + 1 << ": " << ans << endl;
    }
    return 0;
}
