#include <bits/stdc++.h>

using namespace std;

int main() {
    int caseNum;
    cin >> caseNum;
    for (int caseIdx = 0; caseIdx < caseNum; ++caseIdx) {
        cout << "Case #" << caseIdx+1 << ": ";

        string s;
        cin >> s;
        string ans = "";
        for (int i = 0; i < s.size(); ++i) {
            if (ans == "") {
                ans += s[i];
            } else {
                if (s[i] >= ans[0]) {
                    ans = s[i] + ans;
                } else {
                    ans = ans + s[i];
                }
            }
        }

        cout << ans << endl;
    }

    return 0;
}
