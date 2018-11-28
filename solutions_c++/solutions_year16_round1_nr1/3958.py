#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

int cas;
string s;

string solve() {
    string ans = "", a, b;
    for (int i = 0; i < s.size(); i++) {
        a = ans + s[i];
        b = s[i] + ans;
        ans = max(a, b);
    }
    return ans;
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("ans.out", "w", stdout);
    cin >> cas;
    for (int t = 1; t <= cas; t++) {
        cin >> s;
        cout << "Case #" << t << ": " << solve() << endl;
    }
    return 0;
}
