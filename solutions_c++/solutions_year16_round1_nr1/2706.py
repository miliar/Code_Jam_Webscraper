#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std; int tt;
typedef long long ll;
string st;
void solve() {
    cin >> st;
    int N = st.length();
    string ans = "";ans = ans + st[0];
    for(int i = 1; i < N; i++) {
        if(st[i] >= ans[0]) ans = st[i] + ans;
        else ans = ans + st[i];
    }
    cout << "Case #" << tt << ": " << ans << endl;
}
int main() {
    int t = 1; scanf("%d", &t);
    for(tt = 1; tt <= t; tt++) solve();
}
