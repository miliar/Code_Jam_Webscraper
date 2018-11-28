#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
//#include<cctype>
#include<climits>
#include<iostream>
#include<string>
#include<vector>
#include<map>
//#include<list>
#include<queue>
#include<deque>
#include<algorithm>
//#include<numeric>
#include<utility>
//#include<memory>
#include<functional>
#include<cassert>
#include<set>
#include<stack>
#include<random>

const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, -1, 0, 1};
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> pii;

bool check(string s, int R, int P, int S) {
    int rc = 0, pc = 0, sc = 0;
    for (char c : s) {
        if (c == 'R') rc++;
        if (c == 'P') pc++;
        if (c == 'S') sc++;
    }
    return rc == R && pc == P && sc == S;
}

string dp[15][3];

string dfs(int n, int type) {
    string& ret = dp[n][type];
    if (ret != "") return ret;
    if (n == 0) {
        if (type == 0) return ret = "R";
        if (type == 1) return ret = "P";
        if (type == 2) return ret = "S";
    }
    ret = min(dfs(n-1, type)+dfs(n-1, (type+2)%3), dfs(n-1, (type+2)%3) + dfs(n-1, type));
    return ret;
}

void solve() {
    int N, R, P, S;
    cin >> N >> R >> P >> S;
    string ans = "|";
    string tmp = dfs(N, 0);
    if (check(tmp, R, P, S)) ans = min(ans, tmp);
    tmp = dfs(N, 1);
    if (check(tmp, R, P, S)) ans = min(ans, tmp);
    tmp = dfs(N, 2);
    if (check(tmp, R, P, S)) ans = min(ans, tmp);
    if (ans == "|") {
        cout << "IMPOSSIBLE" << endl;
    } else {
        cout << ans << endl;
    }
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": "; 
        solve();
    }
    return 0;
}
