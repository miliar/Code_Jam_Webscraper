#include <string>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <string.h>
#include <queue>
#include <cstdio>
#include <cassert>
#include <deque>
#include <stack>
#include <utility>
#include <numeric>
#include <ctime>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forv(i, v) forn(i, v.size())

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

const int MAXN = 15;
const int MAXV = 1000000;

int n, m;
string s[MAXN];
int best, cnt;
int num[MAXN];

int countNodes(const vector<string>& s) {
    int n = s.size();
    vector< vector<int> > next;
    next.pb(vector<int>(26, -1));
    forn(i, n) {
        int v = 0;
        forv(j, s[i]) {
            int c = s[i][j] - 'A';
            if (next[v][c] == -1) {
                next.pb(vector<int>(26, -1));
                next[v][c] = next.size() - 1;
            }
            v = next[v][c];
        }
    }
    return next.size();
}

void calc() {
    int cur = 0;
    forn(i, n) {
        vector<string> vs;
        forn(j, m) if (num[j] == i) vs.pb(s[j]);
        if (vs.empty()) return;
        cur += countNodes(vs);
    }
    if (cur > best) {
        best = cur, cnt = 0;
    }
    if (cur == best) cnt++;
}

void rec(int k) {
    if (k == m) {
        calc();
        return;
    }
    forn(i, n) {
        num[k] = i;
        rec(k + 1);
    }
}

void solve(int tc) {
    cerr << "Case #" << tc << ", " << clock() << " ms.\n";
    cout << "Case #" << tc << ": ";
    cin >> m >> n;
    forn(i, m) cin >> s[i];
    best = 0;
    cnt = 0;
    rec(0);
    cout << best << " " << cnt << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    forn(i, tc) solve(i + 1);
    return 0;
}
