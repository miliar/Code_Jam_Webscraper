#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <ctime>
#include <float.h>

using namespace std;

#define REP(i, from, to) for (int i = (from); i < (to); ++i)
#define FOR(i, n) REP(i, 0, (n))
#define ALL(x) x.begin(), x.end()
#define SIZE(x) (int)x.size()
#define PB push_back
#define MP make_pair

typedef long long i64;

typedef vector<int>    VI;
typedef vector<VI>     VVI;
typedef vector<string> VS;
typedef vector<VS>     VVS;
typedef pair<int, int> PII;

map<pair<string, char>, int> memo;

int solve(string const& s, char sign) {
    if (SIZE(s) == 1)
        return abs((s[0] == sign) - 1);
    auto key = make_pair(s, sign);
    if (memo.count(key))
        return memo[key];

    int res = 1e9;
    string const s_ = s.substr(0, SIZE(s) - 1);
    if (s.back() == sign) {
        res = min(res, solve(s_, sign));
    }

    res = min(res, solve(s_, "+-"[sign == '+']) + 1);

    string reversed = s;
    reverse(ALL(reversed));
    FOR (i, SIZE(reversed))
        reversed[i] = "+-"[reversed[i] == '+'];

    string const reversed_ = reversed.substr(0, SIZE(reversed) - 1);
    if (reversed.back() == sign) {
        res = min(res, solve(reversed_, sign) + 1);
    }

    res = min(res, solve(reversed_, reversed.back()) + 2);

    return memo[key] = res;
}

string randomPattern(int n) {
    string s;
    FOR (i, n) s += "+-"[rand() % 2];
    return s;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tests;
    cin >> tests;

    FOR (t, tests) {
        string s;
        cin >> s;

        cout << "Case #" << t + 1 << ": " << solve(s, '+') << endl;
    }

    return 0;
}
