#include <iostream>
#include <vector>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define fornn(i, a, b) for (int i = (int)(a); i < (int)(b); ++i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

typedef long long i64;
typedef pair<i64, i64> pi64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;

void rec(int i, const vector<string> &s, vi &p, int &worst, int &wways, int cur) {
    if (i == s.size()) {
        bool ok = true;
        forn(j, p.size()) if (p[j] == -1) ok = false;
        if (ok && cur >= worst) {
            if (cur > worst) worst = cur, wways = 0;
            ++wways;
        }
        return;
    }
    forn(j, p.size()) {
        int pcur = cur;
        int pj = p[j];
        if (p[j] == -1) {
            cur += s[i].size() + 1;
        } else {
            int k = 0;
            while (k < s[i].size() && k < s[p[j]].size() && s[i][k] == s[p[j]][k]) ++k;
            cur += s[i].size() - k;
        }
        p[j] = i;
        rec(i + 1, s, p, worst, wways, cur);
        cur = pcur;
        p[j] = pj;
    }
}

int main() {
#ifdef LOCAL_DEFINE
//    freopen("input.txt", "rt", stdin);
//    freopen("output.txt", "wt", stdout);
#endif

    int T;
    cin >> T;
    forn(t, T) {
        int N, M;
        cin >> N >> M;
        vector<string> s(N);
        forn(i, N) cin >> s[i];
        sort(all(s));
        int worst = -1, wways = 0;
        vi p(M, -1);
        rec(0, s, p, worst, wways, 0);
        cout << "Case #" << t + 1 << ": " << worst << ' ' << wways << '\n';
    }

#ifdef LOCAL_DEFINE
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
    return 0;
}
