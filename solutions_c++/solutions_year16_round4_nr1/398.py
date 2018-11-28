#include <bits/stdc++.h>
using namespace std;
const int maxn = 13;

int n, a, b, c;

void solve() {
    cin >> n >> a >> b >> c;
    priority_queue<string, vector<string>, greater<string> > r, p, s;
    for (int i = 0; i < a; i++) {
        r.push("R");
    }
    for (int i = 0; i < b; i++) {
        p.push("P");
    }
    for (int i = 0; i < c; i++) {
        s.push("S");
    }
    for (int i = 0; i < n; i++) {
        int sz = 1 << (n - i);
        if (max(a, max(b, c)) > sz / 2) {
            cout << "IMPOSSIBLE";
            return;
        }
        int na = c - (sz / 2 - a);
        int nb = a - (sz / 2 - b);
        int nc = b - (sz / 2 - c);
        a = na, b = nb, c = nc;

        priority_queue<string, vector<string>, greater<string> > nr, np, ns;
        for (int i = 0; i < a; i++) {
            string rock = r.top();
            r.pop();
            string scissor = s.top();
            s.pop();
            if (rock.compare(scissor) < 0) {
                nr.push(rock + scissor);
            } else {
                nr.push(scissor + rock);
            }
        }
        for (int i = 0; i < b; i++) {
            string paper = p.top();
            p.pop();
            string rock = r.top();
            r.pop();
            if (paper.compare(rock) < 0) {
                np.push(paper + rock);
            } else {
                np.push(rock + paper);
            }
        }
        for (int i = 0; i < c; i++) {
            string scissor = s.top();
            s.pop();
            string paper = p.top();
            p.pop();
            if (scissor.compare(paper) < 0) {
                ns.push(scissor + paper);
            } else {
                ns.push(paper + scissor);
            }
        }

        r = nr, p = np, s = ns;
    }

    if (!r.empty()) {
        cout << r.top();
    } else if (!p.empty()) {
        cout << p.top();
    } else {
        cout << s.top();
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int numCases;
    cin >> numCases;
    for (int i = 1; i <= numCases; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << '\n';
    }
    return 0;
}
