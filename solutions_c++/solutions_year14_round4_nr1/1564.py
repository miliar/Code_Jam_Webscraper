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
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef vector<VS> VVS;
typedef pair<int, int> PII;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);

    int tests;
    cin >> tests;

    FOR (testId, tests) {
        int n, x;
        cin >> n >> x;

        VI a(n);
        FOR (i, n) cin >> a[i];

        multiset<int> rem(ALL(a));
        int res = 0;
        while (!rem.empty()) {
            int const next = *rem.begin();
            rem.erase(rem.begin());

            if (!rem.empty()) {
                auto it = rem.lower_bound(x - next);
                if (it == rem.end() || it != rem.begin() && *it > x - next)
                    --it;
                if (*it <= x - next)
                    rem.erase(it);
            }

            ++res;
        }

        printf("Case #%d: %d\n", testId + 1, res);

    }

    return 0;
}
