#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iomanip>

using namespace std;
 
#define debug(x) cerr << "DEBUG: " << #x << " = " << x << endl
#define forn(i, n) for(int i = 0; i < (n); ++i)
#define all(x) x.begin(), x.end()
#define mp make_pair
#define pb push_back

template <typename T> inline void mn(T& x, const T& y) { if (y < x) x = y; }
template <typename T> inline void mx(T& x, const T& y) { if (x < y) x = y; }
template <typename T> inline int sz(const T& x) { return (int) x.size(); }

inline long long SUM(int l, int r, const vector<long long>& sums) {
    return sums[r] - sums[l];
}

const int N = 100;


int n;

int GIRL_DMG;
int TOWER_DMG;

int reward[N];
int hp[N];

map<int, int> dp[N][2];


void gen(bool girl, int hpLeft, int skip, vector<pair<int, bool> >& ways) {
    if (hpLeft <= 0) {
        ways.pb(mp(skip, girl));
        return;
    } 

    if (girl) {
        gen(!girl, hpLeft - GIRL_DMG, skip, ways);
        gen(!girl, hpLeft, skip + 1, ways);
    } else {
        gen(!girl, hpLeft - TOWER_DMG, skip, ways);
    }
}

int DP(int target, bool girl, int shoots) {
    if (target == n) {
        return 0;
    }
    auto it = dp[target][girl].find(shoots);
    if (it != dp[target][girl].end()) {
        return it->second;
    }
    // cout << target << ' ' << n << endl;

    int ans = 0;
    for (int before = 0; before <= shoots; ++before) {
        if (GIRL_DMG * before >= hp[target]) {
            mx(ans, DP(target + 1, girl, shoots - before) + reward[target]);
            break;
        }
    vector<pair<int, bool> > ways;
        gen(girl, hp[target] - GIRL_DMG * before, 0, ways);
        // debug(sz(ways));
        for (auto ways : ways) {
            // debug(ways.second);
            mx(ans, DP(target + 1, ways.second, shoots - before + ways.first) + (ways.second ? 0 : reward[target]));
        }

    }


    dp[target][girl][shoots] = ans;
    return ans;

}

int main() {
    // freopen("in.txt", "r", stdin);
    freopen("B-large.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    ios_base::sync_with_stdio(false);

    int nTests;
    cin >> nTests;
    forn (iTest, nTests) {
        cout << "Case #" << (iTest + 1) << ": ";
        cin >> GIRL_DMG >> TOWER_DMG >> n;

        forn (i, n) {
            cin >> hp[i] >> reward[i];
        }

        forn (i, n) {
            dp[i][0].clear();
            dp[i][1].clear();
        }

        cout << DP(0, true, 0) << endl;
    }    

    return 0;
}