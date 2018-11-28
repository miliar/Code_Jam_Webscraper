#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

int T, N, R, P, S, cas = 0;
char s[15][5000];
int cnt[256];
string ans;
vector<string> vec;

string dp[15][256];
void init() {
    dp[0]['R'] = "R";
    dp[0]['P'] = "P";
    dp[0]['S'] = "S";
    for (int n = 0; n < 12; ++n) {
        string r1 = dp[n]['R'] + dp[n]['S'];
        string r2 = dp[n]['S'] + dp[n]['R'];
        dp[n + 1]['R'] = r1 < r2 ? r1 : r2;

        string p1 = dp[n]['P'] + dp[n]['R'];
        string p2 = dp[n]['R'] + dp[n]['P'];
        dp[n + 1]['P'] = p1 < p2 ? p1 : p2;

        string s1 = dp[n]['S'] + dp[n]['P'];
        string s2 = dp[n]['P'] + dp[n]['S'];
        dp[n + 1]['S'] = s1 < s2 ? s1 : s2;
    }
}

bool check(char win) {
    ans = dp[N][win];
    memset(cnt, 0, sizeof(cnt));
    for (int i = 0; i < ans.size(); ++i) ++cnt[ans[i]];
    if (cnt['R'] != R || cnt['P'] != P || cnt['S'] != S) return false;
    vec.push_back(ans);
    return true;
}

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a_out.txt", "w", stdout);
    init();
    cin >> T;
    while (T--) {
        cin >> N >> R >> P >> S;
        vec.clear();
        check('R');
        check('P');
        check('S');
        if (vec.size()) {
            sort(vec.begin(), vec.end());
            printf("Case #%d: %s\n", ++cas, vec[0].c_str());
        } else printf("Case #%d: IMPOSSIBLE\n", ++cas);
    }
    return 0;
}
