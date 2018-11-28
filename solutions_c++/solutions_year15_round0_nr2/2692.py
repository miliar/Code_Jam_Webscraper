#include <bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define each(it,n) for(__typeof((n).begin()) it=(n).begin();it!=(n).end();++it)

using namespace std;

vector<int> v;

int memo[1005][1005];

int doit(int index, int lower) {
    if (memo[index][lower] >= 0) return memo[index][lower];
    if (index == v.size()) return lower;
    if (v[index] < lower) return lower;
    int ans = 1 << 27;
    for (int i = 0; i < 50; i++) {
        if (i + 1 > v[index]) break;
        ans = min(ans, i + doit(index + 1, max(lower, (v[index] + i) / (i + 1))));
    }
    
    return memo[index][lower] = ans;
}

void solve() {
    v = vector<int>();
    rep(i, 1005) rep(j, 1005) memo[i][j] = -1;
    int n;
    cin >> n;
    rep(i, n) {
        int a;
        cin >> a;
        v.push_back(a);
    }
    sort(v.begin(), v.end());
    reverse(v.begin(), v.end());
    
    cout << doit(0, 0) << endl;
}

int main() {
    int T;
    cin >> T;
    rep(i, T) {
        cout << "Case #" << i + 1 << ": "; 
        solve();
    }
    return 0;
}
