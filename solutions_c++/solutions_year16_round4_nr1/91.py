#include <bits/stdc++.h>
using namespace std;
#define sz(x) ((int) (x).size())
#define forn(i,n) for (int i = 0; i < int(n); ++i)
typedef long long ll;
typedef long long i64;
typedef long double ld;
const int inf = int(1e9) + int(1e5);
const ll infl = ll(2e18) + ll(1e10);

int n, a[3];
int c[3];
char ch[3] = {'R', 'S', 'P'};
map<char, int> chid = {{'R', 0}, {'S', 1}, {'P', 2}};

string build(string s, int n) {
    if (n == 0)
        return s;
    string res;
    forn (i, s.size()) {
        res.push_back(s[i]);
        res.push_back(ch[(chid[s[i]] + 1) % 3]);
    }
    return build(res, n - 1);
}

void lex(string &s, int l, int r) {
    if (l + 1 == r) {
        return;
    }
    int c = (l + r) / 2;
    lex(s, l, c);
    lex(s, c, r);
    for (int i = 0; i < c - l; ++i) {
        if (s[l + i] == s[c + i])
            continue;
        if (s[l + i] > s[c + i]) {
            forn (j, c - l)
                swap(s[l + j], s[c + j]);
        }
        break;
    }
}

int test = 1;
void solve() {
    cin >> n >> a[0] >> a[2] >> a[1];
    string best;
    forn (st, 3) {
        string res = build(string(1, ch[st]), n);
        lex(res, 0, res.size());
        int c[3] = {0, 0, 0};
        forn (i, res.size()) {
            c[chid[res[i]]]++;
        }
        if (c[0] == a[0] && c[1] == a[1] && c[2] == a[2]) {
            if (best.empty())
                best = res;
            if (best > res)
                best = res;
        }
    }
    cout << "Case #" << test++ << ": ";
    if (best.empty())
        cout << "IMPOSSIBLE\n";
    else
        cout << best << '\n';
}

int main() {
    #ifdef LOCAL
    assert(freopen("a.in", "r", stdin));
    #else
    #endif
    int tn;
    cin >> tn;
    forn (i, tn)
        solve();
}
