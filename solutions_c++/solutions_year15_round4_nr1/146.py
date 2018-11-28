#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <cassert>

using namespace std;

#define pb push_back
#define mp make_pair
#define REP(i, n) for (int i = 0; i < (int)(n); ++i)
#define foreach(e, x) for (__typeof(x.begin()) e = x.begin(); e != x.end(); ++e)
typedef long long LL;
typedef pair<int, int> PII;

int tt, r, c;
string s[105];

int main() {
    ios_base::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> tt;
    for (int test = 1; test <= tt; ++test) {
        cin >> r >> c;
        REP(i, r) cin >> s[i];
        int ans = 0;
        REP(i, r) if (ans != -1) REP(j, c) if (s[i][j] != '.') {
            bool uu, dd, ll, rr;
            uu = dd = ll = rr = false;
            for (int jj = j + 1; jj < c; ++jj) if (s[i][jj] != '.')
                rr = true;
            for (int jj = j - 1; jj >= 0; --jj) if (s[i][jj] != '.')
                ll = true;
            for (int ii = i + 1; ii < r; ++ii) if (s[ii][j] != '.')
                dd = true;
            for (int ii = i - 1; ii >= 0; --ii) if (s[ii][j] != '.')
                uu = true;
            if (!rr && !ll && !dd && !uu) {
                ans = -1;
                break;
            }
            char cur = s[i][j];
            if ((cur == '^' && !uu) || (cur == 'v' && !dd) || (cur == '>' && !rr) || (cur == '<' && !ll))
                ++ans;
        }
        if (ans == -1) printf("Case #%d: IMPOSSIBLE\n", test);
        else printf("Case #%d: %d\n", test, ans);
    }
	return 0;
}
