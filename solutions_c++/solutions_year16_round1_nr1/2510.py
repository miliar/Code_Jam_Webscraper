#include <iostream>
using namespace std;

void solve () {
    string s, ans;
    cin >> s;
    ans = "";
    for (int i=0; i<s.size(); i++) {
        if (ans == "")
            ans += s[i];
        else {
            if (ans[0] <= s[i]) ans = s[i] + ans;
            else ans = ans + s[i];
        }
    }
    cout << ans << endl;
}

int main () {
    int t;
    cin >> t;
    for (int i=1; i<=t; i++) {
        cout << "Case #" << i << ": ";
        solve ();
    }
}