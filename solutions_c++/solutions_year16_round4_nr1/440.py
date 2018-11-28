#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <numeric>

using namespace std;
typedef long long li;
typedef pair <li, li> pi;
#define rep(i, n) for(int i = 0; i < (int)(n); ++i)

const string impossible = "IMPOSSIBLE";

string winner(int r, int p, int s) {
    const int sum = r + p + s;
    if (sum == 1) {
        return string(p, 'P') + string(s, 'S') + string(r, 'R');
    }
    const int pr = (sum - 2 * s) / 2;
    const int ps = (sum - 2 * r) / 2;
    const int rs = (sum - 2 * p) / 2;
    if (pr < 0 || ps < 0 || rs < 0) {
        return impossible;
    }

    const int nr = (sum - 2 * p) / 2;
    const int np = (sum - 2 * s) / 2;
    const int ns = (sum - 2 * r) / 2;

    return winner(nr, np, ns);
}

string rebuild(char top, int level) {
    if (level == 0) {
        return string(1, top);
    }
    string next;
    if (top == 'R') {
        next = "RS";
    } else if (top == 'P') {
        next = "PR";
    } else {
        next = "SP";
    }

    vector<string> children;
    for (char c : next) {
        children.push_back(rebuild(c, level - 1));
    }
    sort(children.begin(), children.end());
    return children[0] + children[1];
}

void solve() {
    int n, r, p, s;
    cin >> n >> r >> p >> s;

    string res = winner(r, p, s);
    if (res != impossible) {
        res = rebuild(res[0], n);
    }

    cout << res << endl;
}

int main() {
    int t;
    cin >> t;
    rep(i, t) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
