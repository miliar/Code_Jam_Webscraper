#include "bits/stdc++.h"
#define puba push_back
#define mapa make_pair
#define ff first
#define ss second
#define bend(_x) (_x).begin(), (_x).end()
#define szof(_x) ((int) (_x).size())
#define TASK_NAME ""

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const int MAXL = 55;

char s[MAXL];

int solve() {
    int n, l;
    scanf("%d%d", &n, &l);

    vector<string> inp;
    for (int i = 0; i < n; ++i) {
        scanf("%s", s);
        inp.puba(s);
    }
    string bad;
    scanf("%s", s);
    bad = s;
    for (auto w: inp) {
        if (w == bad) {
            cout << "IMPOSSIBLE\n";
            return 0;
        }
    }
    for (int i = 0; i < l; ++i) {
        cout << "0?";
    }
    cout << " ";
    cout << "0";
    for (int i = 0; i < l - 1; ++i) {
        cout << "1";
    }
    cout << "\n";
    return 0;
}

int main() {
    //freopen(TASK_NAME ".in", "r", stdin);
    //freopen(TASK_NAME ".out", "w", stdout);

    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }

    return 0;
}