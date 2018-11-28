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
        string s;
        cin >> n >> s;

        int invited = 0;
        int standup = 0;
        FOR (i, n + 1) {
            int const level = s[i] - '0';
            if (i == 0) {
                standup = level;
            } else {
                if (i > standup) {
                    int const add = i - standup;
                    invited += add;
                    standup += add;
                }
                standup += level;
            }
        }

        cout << "Case #" << t + 1 << ": " << invited << endl;
    }

    return 0;
}
