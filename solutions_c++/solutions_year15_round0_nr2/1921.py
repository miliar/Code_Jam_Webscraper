#include <bits/stdc++.h>

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

    ios_base::sync_with_stdio(false);

    int tests;
    cin >> tests;

    FOR (t, tests) {
        int n;
        cin >> n;

        VI p(n);
        FOR (i, n) cin >> p[i];

        sort(ALL(p));

        int best = 1e9;
        REP (remPie, 1, p[SIZE(p) - 1] + 1) {
            int wasted = remPie;
            for (auto x : p) if (x > remPie) {
                wasted += (x + remPie - 1) / remPie - 1;
            }
            best = min(best, wasted);
        }

        cout << "Case #" << t + 1 << ": " << best << endl;
    }

    return 0;
}
