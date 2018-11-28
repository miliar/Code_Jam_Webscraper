#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (int)(n); i++)
typedef long long ll;
typedef pair <int, int> PII;
const int N = 8;
int Tc, m, n, cnt;
string s[N];
int ch[100000][26];
int ans, way;
int where[N];

void cr(int p) {
    memset(ch[p], 0xff, sizeof(ch[p]));
}

void ins(string s) {
    int p = 0;
    for (char c : s) {
        if (ch[p][c - 'A'] == -1) {
            cr(cnt);
            ch[p][c - 'A'] = cnt++;
        }
        p = ch[p][c - 'A'];
    }
}

int gao(const vector <string> &v) {
    if (v.empty()) return 0;
    cnt = 1;
    cr(0);
    for (const string s : v) {
        ins(s);
    }
    return cnt;
}

void solve() {
    int res = 0;
    rep (i, n) {
        vector <string> tmp;
        rep (j, m) if (where[j] == i) tmp.push_back(s[j]);
        res += gao(tmp);
    }
    if (res > ans) {
        ans = res;
        way = 1;
    } else if (res == ans) {
        way++;
    }
}

void dfs(int i) {
    if (i == m) {
        solve();
    } else {
        for (int j = 0; j < n; j++) {
            where[i] = j;
            dfs(i + 1);
        }
    }
}

int main() {
    cin >> Tc;
    rep (ri, Tc) {
        printf("Case #%d: ", ri + 1);
        cin >> m >> n;
        rep (i, m) {
            cin >> s[i];
        }
        ans = -1;
        way = 0;
        dfs(0);
        printf("%d %d\n", ans, way);
    }
}

