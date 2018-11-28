#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int cmp(string a, string b) {
    for (int i = 0; i < (int) a.size(); ++i)
        if (a[i] > b[i]) return 1;
        else if (a[i] < b[i]) return 0;
    return 1;
}
int ok(string s, char x) {
    string t = "";
    t += x;
    for (int i = 0; i < (int) s.size(); ++i) t += s[i];
    s += x;
    if (cmp(t, s)) return 1;
    return 0;
}
int main() {
    int T, cas = 0;
    cin >> T;
    while (T--) {
        string s;
        cin >> s;
        string cur = "";
        int len = (int) s.size();
        cur += s[0];
        for (int i = 1; i < len; ++i) {
            if (ok(cur, s[i])) {
                string tmp = "";
                tmp += s[i];
                for (int j = 0; j < i; ++j) tmp += cur[j];
                cur = tmp;
            }
            else {
                cur += s[i];
            }
        }
        string ans = cur;
        printf("Case #%d: ", ++cas);
        cout << ans << endl;
    }
    return 0;
}
