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

int64 get_divisor(int64 n) {
    if (n <= 2) return -1;
    if (n % 2 == 0) return 2;
    for (int64 k = 3; k <= n / k && k <= 10000; k += 2) {
        if (n % k == 0) return k;
    }
    return -1;
}

void foo(int n, int j) {
    vector<int> digits(n);
    digits[0] = digits[n - 1] = 1;
    vector<int64> used;
    while (j > 0) {
        int64 m = rand() % (1 << (n - 2));
        if (find(used.begin(), used.end(), m) != used.end()) continue;
        for (int i = 0 ; i < n - 2; ++i) {
            digits[i + 1] = checkbit(m, i) ? 1 : 0;
        }
        // cerr << "Trying " << m << " ";
        //     for (int i = 0; i < n; ++i) {
        //         cerr << digits[i];
        //     }
        // cerr << endl;
        vector<int64> divisors;
        bool ok = true;
        for (int d = 2; d <= 10; ++d) {
            int64 num = 0;
            for (int i = 0; i < n; ++i) {
                num *= d;
                num += digits[i];
            }
            // debug(d);
            // debug(num);
            int64 div = get_divisor(num);
            // debug(div);
            if (div < 0) {
                ok = false;
                break;
            } else {
                assert(num % div == 0);
                assert(div != 1);
                assert(div != num);
                divisors.push_back(div);
            }
        }
        if (ok) {
            assert(divisors.size() == 9);
            for (int i = 0; i < n; ++i) {
                cout << digits[i];
            }
            for (int i = 0; i < 9; ++i) {
                cout << " " << divisors[i];
            }
            cout << endl;
            --j;
            used.push_back(m);
        }
    }
}

int main() {
     // freopen("input.txt", "rt", stdin);
    // freopen("output.txt", "wt", stdout);

	int testCount;
    cin >> testCount;

    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
        int n, j;
        cin >> n >> j;
        cout << "Case #" << testNumber << ":" << endl;
        foo(n, j);
    }

    return 0;
}
