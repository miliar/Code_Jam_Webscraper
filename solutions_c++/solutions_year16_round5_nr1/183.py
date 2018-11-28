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
const int MAXL = 20005;

char s[MAXL];

int solve() {
    scanf("%s", s);
    int n = strlen(s);
    vector<char> now;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        if (n - i == szof(now)) {
            break;
        }
        
        if (szof(now) && now.back() == s[i]) {
            ans += 2;
            now.pop_back();
        } else {
            now.puba(s[i]);
        }
    }
    while (szof(now)) {
        ans += 2 - (s[n - szof(now)] != now.back());
        now.pop_back();
    }
    cout << ans * 5 << "\n";
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