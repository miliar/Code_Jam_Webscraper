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

string foo(int n, int r, int p, int s) {
    if (abs(p - r) > 1 || abs(p - s) > 1 || abs(r - s) > 1)
        return "IMPOSSIBLE";
    if (n == 1) {
        if (s == 0) return "PR";
        if (r == 0) return "PS";
        if (p == 0) return "RS";
        assert(false);
    }
    string res1, res2;
    if (p > r && p > s) {
        assert(p % 2 == 0);
        res1 = foo(n - 1, r / 2, p / 2, s / 2 + 1);
        res2 = foo(n - 1, r / 2 + 1, p / 2, s / 2);
    } else if (r > p && r > s) {
        assert(r % 2 == 0);
        res1 = foo(n - 1, r / 2, p / 2, s / 2 + 1);
        res2 = foo(n - 1, r / 2, p / 2 + 1, s / 2);
    } else if (s > p && s > r) {
        assert(s % 2 == 0);
        res1 = foo(n - 1, r / 2 + 1, p / 2, s / 2);
        res2 = foo(n - 1, r / 2, p / 2 + 1, s / 2);
    } else if (p < r && p < s) {
        assert(p % 2 == 0);
        res1 = foo(n - 1, r / 2, p / 2, s / 2 + 1);
        res2 = foo(n - 1, r / 2 + 1, p / 2, s / 2);
    } else if (r < p && r < s) {
        assert(r % 2 == 0);
        res1 = foo(n - 1, r / 2, p / 2, s / 2 + 1);
        res2 = foo(n - 1, r / 2, p / 2 + 1, s / 2);
    } else if (s < p && s < r) {
        assert(s % 2 == 0);
        res1 = foo(n - 1, r / 2 + 1, p / 2, s / 2);
        res2 = foo(n - 1, r / 2, p / 2 + 1, s / 2);
    } else {
        assert(false);
    }
    if (res1 == "IMPOSSIBLE" || res2 == "IMPOSSIBLE")
        return res1;
    if (res2 < res1)
        swap(res1, res2);
    return res1 + res2;
}

int main() {
     // freopen("input.txt", "rt", stdin);
    // freopen("output.txt", "wt", stdout);

	int testCount;
    cin >> testCount;

    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
        int n, r, p, s;
        cin >> n >> r >> p >> s;
        auto res = foo(n, r, p, s);
        cout << "Case #" << testNumber << ": " << res << endl;
    }

    return 0;
}
