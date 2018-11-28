#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)

#define DEBUG(x) { cout << #x << " = "; cout << (x) << endl; }
#define PR(a,n) { cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl; }
#define PR0(a,n) { cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl; }
using namespace std;

int m, n;
string a[11];
int ln, cnt;
int to[11];
set<string> s[11];

void attempt(int i) {
    if (i > m) {
        FOR(t,1,n) s[t].clear();
        FOR(t,1,m) {
            REP(x,a[t].length())
                s[to[t]].insert(a[t].substr(0, x+1));
        }
        int cur = 0;
        FOR(t,1,n) if (s[t].size()) {
            cur += s[t].size() + 1;
        }
        // PR(to,m);
        // DEBUG(cur);
        // FOR(i,1,m) {
        //     for(__typeof(s[i].begin()) it = s[i].begin(); it != s[i].end(); ++it)
        //         cout << *it << ' ';
        //     cout << endl;
        // }
        if (cur > ln) {
            ln = cur;
            cnt = 1;
        }
        else if (cur == ln) {
            ++cnt;
        }
        return ;
    }

    FOR(t,1,n) {
        to[i] = t;
        attempt(i+1);
    }
}

int main() {
    ios :: sync_with_stdio(false);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cin >> m >> n;
        FOR(i,1,m) cin >> a[i];

        ln = -1, cnt = 0;
        attempt(1);

        cout << "Case #" << test << ": " << ln << ' ' << cnt << endl;
    }
    return 0;
}
