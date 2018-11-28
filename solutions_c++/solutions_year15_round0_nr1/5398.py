#include <iostream>
using namespace std;
int main() {
    int ncase;
    cin >> ncase;
    for (int i = 0; i < ncase; i++) {
        int n, ans = 0;
        string s;
        cin >> n >> s;
        for (int j = 1, cur = s[0] - '0'; j < s.size(); j++) {
            if (j > cur) {
                ans += j - cur; 
                cur += j - cur;
            }
            cur += s[j] - '0';
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
    return 0;
}
