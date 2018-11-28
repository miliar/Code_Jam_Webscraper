#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)

#define DEBUG(x) { cout << #x << " = "; cout << (x) << endl; }
#define PR(a,n) { cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl; }
#define PR0(a,n) { cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl; }
using namespace std;

const int MN = 1011;

int n;
string s[MN];
pair<char,int> rep[MN][MN];
int nrep[MN];

int cur[MN];

int solve() {
    FOR(i,1,n) {
        nrep[i] = 0;
        int u = 0;
        while (u < s[i].length()) {
            int v = u;
            while (v < s[i].length() - 1 && s[i][v] == s[i][v+1]) ++v;

            ++nrep[i];
            rep[i][nrep[i]] = make_pair(s[i][u], v - u + 1);
            u = v + 1;
        }
    }

    FOR(i,1,n) {
        if (nrep[i] != nrep[1]) return -1;
        FOR(u,1,nrep[1])
            if (rep[i][u].first != rep[1][u].first) return -1;
    }

    int res = 0;
    FOR(u,1,nrep[1]) {
        FOR(i,1,n) cur[i] = rep[i][u].second;
        sort(cur+1, cur+n+1);
        int to = cur[n / 2 + n % 2];
        FOR(i,1,n) res += abs(to - cur[i]);
    }
    return res;
}

int main() {
    ios :: sync_with_stdio(false);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cin >> n;
        FOR(i,1,n) cin >> s[i];
        int res = solve();
        cout << "Case #" << test << ": ";
        if (res < 0) cout << "Fegla Won\n";
        else cout << res << "\n";
    }
    return 0;
}
