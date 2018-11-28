#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main() {
    int caseCnt = 0;
    cin >> caseCnt;
    for (int ci = 0; ci < caseCnt; ++ci) {
        string s;
        cin >> s;
        char p = s[0];
        int ans = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] != p) {
                ans++;
            }
            p = s[i];
        }
        if (s[s.size()-1] == '-') {
            ans++;
        }
        printf("Case #%d: %d\n", ci + 1, ans);
    }

    return 0;
}
