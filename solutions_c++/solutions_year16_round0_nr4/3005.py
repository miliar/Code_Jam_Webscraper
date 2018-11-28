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

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tests;
    cin >> tests;

    FOR (t, tests) {
        int k, c, s;
        cin >> k >> c >> s;
        i64 p = 1;
        while (--c) p *= k;
        cout << "Case #" << t + 1 << ":";
        FOR (i, k) cout << " " << i * p + 1;
        cout << endl;
    }

    return 0;
}
