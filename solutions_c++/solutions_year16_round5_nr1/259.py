#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;

const int maxn=2e4 + 4;
/*
const int maxm=1e3;
cosnt ld eps;
*/
vector<int> used(maxn);

void Solve() {
    string s;
    cin >> s;
    used.assign(maxn, 0);
    int k = 0;
    while(true) {
        char prev = 'q';
        int prev_i = -1, f = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (used[i]) continue;
            if (prev == s[i]) {
                used[prev_i] = 1;
                used[i] = 1;
                ++k;
                f = 1;
                break;
            }
            prev = s[i];
            prev_i = i;
        }
        if (!f) break;
    }
    cout << k * 5 + 5 * s.size() / 2 << "\n";
}


int main() {
    freopen("A.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; ++i) {
        printf("Case #%d: ", i);
        Solve();
    }
}
