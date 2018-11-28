#include <bits/stdc++.h>

using namespace std;

string s;

int cnt[300];
string name[] = {
"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE",
};

int order[] = {0, 8, 6, 7, 5, 4, 3, 2, 1, 9};
char who[]   = {'Z', 'G', 'X', 'S', 'V', 'F', 'H', 'W', 'O', 'E'};

void solve(int test_id) {
    memset(cnt, 0, sizeof(cnt) );
    cin >> s;
    for (int i = 0; i < s.length(); i++) {
        cnt[ s[i] ]++;
    }
    vector<int> ans;
    for (int i = 0; i < 10; i++) {
        int d = order[i];
        int o = cnt[ who[i] ];
        for (int j = 1; j <= o; j++) {
            ans.push_back(d);
        }
        for (int j = 0; j < name[d].length(); j++) {
            cnt[ name[d][j] ] -= o;
        }
    }
    sort(ans.begin(), ans.end() );
    cout << "Case #" << test_id <<": ";
    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i];
    }
    cout << "\n";
}

int main () {
    freopen("A-large1.in", "r", stdin);
    freopen("A-large1.out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        solve(i);
    }
    return 0;
}
