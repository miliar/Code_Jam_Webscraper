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
// vector<pair<int, int>> foo_slow(int n, vvi& w) {
    
// }

bool process(int64 k, vector<bool>& digits) {
    if (k == 0) {
        digits[0] = true;
    } else {
        while (k != 0) {
            digits[k % 10] = true;
            k /= 10;
        }
    }

    for (int i = 0; i < 10; ++i) {
        if (!digits[i]) return false;
    }
    return true;
}

int64 foo(int n) {
    if (n == 0) return -1;

    vector<bool> digits(10);
    int64 k = n;
    while (!process(k, digits)) {
        k += n;
        assert(k < 100000000);
    }
    return k;
}

int main() {
     // freopen("input.txt", "rt", stdin);
    // freopen("output.txt", "wt", stdout);

	int testCount;
    cin >> testCount;

    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
        int n;
        cin >> n;
        auto res = foo(n);
        if (res < 0) {
            cout << "Case #" << testNumber << ": " << "INSOMNIA" << endl;    
        } else {
            cout << "Case #" << testNumber << ": " << res << endl;
        }
    }

    return 0;
}
