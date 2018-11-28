#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

char s[1005];

void solve() {
    scanf("%s", s);
    int n = strlen(s);
    string ans = "";
    for(int i = 0; i < n; i ++) {
        string x = ans + s[i];
        string y = s[i] + ans;
        if(x < y) ans = y;
        else ans = x;
    }
    cout << ans << endl;
}


int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t ++) {
        printf("Case #%d: ", t);
        solve();
    }
    return 0;
}
