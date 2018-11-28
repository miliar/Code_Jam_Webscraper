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

struct Event {
    char ty;
    int id;
    int num;
};

const int MAXN = 20;
const int INF = 10000000;

int n;
Event e[MAXN];
vector<int> ids;
int dp[MAXN][1 << 15][MAXN];
int ones[1 << 15];

int calc(int k, int mask, int cnt) {
    if (k == n) {
        return ones[mask] + cnt;
    }
    int& res = dp[k][mask][cnt];
    if (res != -1) return res;
    res = INF;
    if (e[k].ty == 'L') {
        if (e[k].id > 0) {
            if ((mask & (1 << e[k].num)) == 0) return res;
            return res = calc(k + 1, mask ^ (1 << e[k].num), cnt);
        } else {
            if (mask == 0 && cnt == 0) return res;
            if (cnt > 0) res = min(res, calc(k + 1, mask, cnt - 1));
            forv(i, ids) {
                if (mask & (1 << i)) {
                    res = min(res, calc(k + 1, mask ^ (1 << i), cnt));
                }
            }
        }
        return res;
    } else {
        if (e[k].id > 0) {
            if (mask & (1 << e[k].num)) return res;
            return res = calc(k + 1, mask | (1 << e[k].num), cnt);
        } else {
            res = min(res, calc(k + 1, mask, cnt + 1));
            forn(i, n) if ((mask & (1 << i)) == 0) res = min(res, calc(k + 1, mask ^ (1 << i), cnt));
        }
        return res;
    }
}

void solve(int tc) {
    cerr << "Case #" << tc << ", " << clock() << " ms.\n";
    cout << "Case #" << tc << ": ";
    scanf("%d\n", &n);
    ids.clear();
    forn(mask, 1 << 15) {
        ones[mask] = 0;
        forn(i, 15) ones[mask] += ((mask >> i) & 1);
    }
    forn(i, n) {
        scanf("%c %d\n", &e[i].ty, &e[i].id);
        if (e[i].id > 0) ids.pb(e[i].id);
    }    
    sort(all(ids));
    ids.erase(unique(all(ids)), ids.end());
    forn(i, n) {
        if (e[i].id > 0) e[i].num = int(lower_bound(all(ids), e[i].id) - ids.begin());
    }
    memset(dp, 255, sizeof(dp));
    int ans = INF;
    forn(mask, (1 << ids.size())) forn(cnt, n + 1) ans = min(ans, calc(0, mask, cnt));
    if (ans == INF) {
        cout << "CRIME TIME" << endl;
    } else {
        cout << ans << endl;
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    forn(i, tc) solve(i + 1);
    return 0;
}
