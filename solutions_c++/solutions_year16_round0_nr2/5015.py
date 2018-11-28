#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <bitset>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <queue>
#include <stack>
#include <assert.h>
#include <iomanip>

using namespace std;

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define mplus(x, y) ((x) == -1 || (y) == -1) ? -1 : ((x) + (y))
#define mmax(x, y) ((x) == -1 || (y) == -1) ? -1 : max((x), (y))
#define mmin(x, y) ((x) == -1) ? (y) : ((y) == -1) ? (x) : min((x), (y))

#define checkbit(n, k) (((1L << (k)) & (n)) != 0)

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)

#define debug(x) cerr << "> " << #x << ": " << (x) << endl;

typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;

const int64 MOD = 1000000007;

int64 foo(string s) {
    int n = s.length();
    vector<int> dp(n + 1);
    vector<int> dm(n + 1);
    for (int i = 1; i <= n; ++i) {
        if (s[i - 1] == '+') {
            dp[i] = dp[i - 1];
            dm[i] = dp[i - 1] + 1;
        } else {
            dm[i] = dm[i - 1];
            dp[i] = dm[i - 1] + 1;
        }
    }
    return dp[n];
}

int main() {
     // freopen("input.txt", "rt", stdin);
    // freopen("output.txt", "wt", stdout);

	int testCount;
    cin >> testCount;

    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
        string s;
        cin >> s;
        auto res = foo(s);
        if (res < 0) {
            cout << "Case #" << testNumber << ": " << "INSOMNIA" << endl;    
        } else {
            cout << "Case #" << testNumber << ": " << res << endl;
        }
    }

    return 0;
}
