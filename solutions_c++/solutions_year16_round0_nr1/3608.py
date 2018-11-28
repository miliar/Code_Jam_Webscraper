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

i64 solve(i64 n) {
    int i = 1;
    i64 last = n;
    set<int> foundDigits;

    do {
        last = i++ * n;
        i64 k = last;
        while (k) {
            foundDigits.insert(k % 10);
            k /= 10;
        }

    } while (SIZE(foundDigits) != 10);
    return last;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    ///FOR (i, 1e6) cout << i << " " << solve(i + 1) << endl;

    int tests;
    cin >> tests;

    FOR (t, tests) {
        i64 n;
        cin >> n;

        cout << "Case #" << t + 1 << ": ";
        if (!n) {
            cout << "INSOMNIA\n";
            continue;
        }

        cout << solve(n) << endl;
    }

    return 0;
}
