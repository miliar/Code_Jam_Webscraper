#include <set>
#include <map>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <cmath>
#include <bitset>
#include <vector>
#include <string>
#include <cstdio>
#include <string>
#include <fstream>
#include <sstream>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define PB push_back
#define SIZE(x) (int)x.size()
#define MP(x, y) make_pair(x, y)
#define ALL(t) (t).begin(),(t).end()
#define CLR(x, y) memset(x, y, sizeof(x))
#define FOR(i, n, m) for (int i = n; i <= m; i++)
#define ROF(i, n, m) for (int i = n; i >= m; i--)

#define RI(x) scanf ("%d", &(x))
#define RII(x, y) RI(x), RI(y)
#define RIII(x, y, z) RI(x), RI(y), RI(z)

typedef long long ll;
typedef unsigned int ui;
typedef unsigned long long ull;

const ll mod = 1e9 + 7;
const int seed = 999731;
const double eps = 1e-8;

/***********************END OF DEFINE******************************/
const int mx = 1e3 + 5;

int t;
string s;
string dp[mx][2];

void solve() {
    string tmp = "";
    FOR (i, 1, s.size()) dp[i][0] = dp[i][1] = tmp;
    dp[0][0] = dp[0][1] = tmp + s[0];
    FOR (i, 1, s.size() - 1) {
        dp[i][0] = max(tmp + s[i] + dp[i - 1][0], tmp + s[i] + dp[i - 1][1]);
        dp[i][1] = max(dp[i - 1][1] + s[i], dp[i - 1][1] + s[i]);
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("data.out", "w", stdout);
    RI(t);
    FOR (i, 0, t - 1) {
        cin >> s;
        string tmp = "";
        string res = tmp + s[0];
        FOR (i, 1, s.size() - 1) {
            if(s[i] >= res[0])
                res = s[i] + res;
            else
                res = res + s[i];
        }
        cout << "Case #" << i + 1 << ": " << res << endl;
        //solve();

        //cout << "Case #" << i + 1 << ": " << max(dp[s.size() - 1][0], dp[s.size() - 1][1]) << endl;
    }
    return 0;
}
